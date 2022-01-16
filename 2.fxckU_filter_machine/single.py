import cv2
import mediapipe as mp    # 손인식
import numpy as np

max_num_hands = 1   # 손 1개 인식
# 11가지 제스처를 인식가능, 원작자가 각 클래스의 데이터를 모음
gesture = {    
    0:'fist', 1:'one', 2:'two', 3:'three', 4:'four', 5:'five',
    6:'six', 7:'rock', 8:'spiderman', 9:'yeah', 10:'ok',
}
# 9(yeah)를 가위, 0(fist)를 주먹, 5(five)를 보 로 이용
rps_gesture = {0:'rock', 5:'paper', 9:'scissors'}

# MediaPipe hands model 
# MediaPipe website 참고 : https://google.github.io/mediapipe/solutions/hands
    # 다양한 딥러닝 모델을 제공. 가볍고 굉장히 성능 좋다.
# 손인식 - 손가락 볼륨 조절기 영상 참고
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils  # 웹캠 영상에서 연두색 뼈마디를 그림
hands = mp_hands.Hands(   # 손가락 detection 모듈 초기화
    max_num_hands=max_num_hands,  # 최대 몇개 손 인식
    min_detection_confidence=0.5,   # 감도
    min_tracking_confidence=0.5)

## 모델 2개 사용
# Gesture recognition model, 제스쳐 인식 모델
# 손가락 각도들 저장, 마지막 숫자는 라벨 (110개)
file = np.genfromtxt('data/gesture_train.csv', delimiter=',')
angle = file[:,:-1].astype(np.float32)
label = file[:, -1].astype(np.float32)

# opencv의 KNN을 사용하고 학습
knn = cv2.ml.KNearest_create()
knn.train(angle, cv2.ml.ROW_SAMPLE, label)

# 웹캠 열기
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, img = cap.read()
    if not ret:
        continue

    ## mediapipe 에 넣기 전에 전처리 필요
    # 거울형태로 좌위 뒤집혀있으므로 좌우 반전
    # BGR -> RGB
    img = cv2.flip(img, 1)   
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # 전처리 및 손 detection 모델 추론을 함께 실행
    result = hands.process(img)

    # 다시 RGB를 BGR로
    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

    # 손을 인식했다면?
    if result.multi_hand_landmarks is not None:  # mediapipe의 attribute
        # 여러개 손인식했을 수 있으니까
        for res in result.multi_hand_landmarks:
            # 손가락의 마디마디를 joint, 총 21개 x,y,z좌표 (z좌표..?)
            # res에 21개의 랜드마크 좌표가 들어가있음
            joint = np.zeros((21, 3))
            for j, lm in enumerate(res.landmark):
                joint[j] = [lm.x, lm.y, lm.z]   # (21,3) 리스트 생성

            # Compute angles between joints
            # MediaPipe website 참고 : https://google.github.io/mediapipe/solutions/hands
            # 각 joint마다 번호가 저장되어있음
            v1 = joint[[0,1,2,3,0,5,6,7,0,9,10,11,0,13,14,15,0,17,18,19],:] # Parent joint
            v2 = joint[[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20],:] # Child joint
            # 각 관절의 벡터를 생성해줌
            v = v2 - v1 # [20,3]
            # Normalize v 
            # np.linalg.norm() 벡터의 길이를 유클리디안 distance 구하는 api
            # 벡터의 길이로 정규화, 크기 1자리 벡터가 나옴?
            v = v / np.linalg.norm(v, axis=1)[:, np.newaxis]

            # Get angle using arcos of dot product
            # 15개의 각도(라디안)를 구한다고 함. 빵형도 잘 모르겠다고 함
            angle = np.arccos(np.einsum('nt,nt->n',
                v[[0,1,2,4,5,6,8,9,10,12,13,14,16,17,18],:], 
                v[[1,2,3,5,6,7,9,10,11,13,14,15,17,18,19],:])) # [15,]

            # 라디안 -> degree로 단위 변경
            angle = np.degrees(angle) # Convert radian to degree

            # Inference gesture
            # knn prediction
            data = np.array([angle], dtype=np.float32)
            ret, results, neighbours, dist = knn.findNearest(data, 3) # k가 3일때 값 구함
            # index만 필요
            idx = int(results[0][0])

            # Draw gesture result
            # idx가 만약 가위바위보 중 하나면, 결과를 표시
            if idx in rps_gesture.keys():
                cv2.putText(img, text=rps_gesture[idx].upper(), org=(int(res.landmark[0].x * img.shape[1]), int(res.landmark[0].y * img.shape[0] + 20)), fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=1, color=(255, 255, 255), thickness=2)

            # Other gestures
            # cv2.putText(img, text=gesture[idx].upper(), org=(int(res.landmark[0].x * img.shape[1]), int(res.landmark[0].y * img.shape[0] + 20)), fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=1, color=(255, 255, 255), thickness=2)

            # 손가락 마디 랜드마크 그리기
            mp_drawing.draw_landmarks(img, res, mp_hands.HAND_CONNECTIONS)

    cv2.imshow('Game', img)
    if cv2.waitKey(1) == ord('q'):
        break
