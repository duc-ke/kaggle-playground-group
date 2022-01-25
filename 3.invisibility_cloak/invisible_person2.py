import cv2, time
import numpy as np
import mediapipe as mp

def get_hand_gesture(mp_hands):
    idx = -9
    for res in mp_hands.multi_hand_landmarks:
        joint = np.zeros((21, 3))
        for j, lm in enumerate(res.landmark):
            joint[j] = [lm.x, lm.y, lm.z]

        # Compute angles between joints
        v1 = joint[[0,1,2,3,0,5,6,7,0,9,10,11,0,13,14,15,0,17,18,19],:]
        v2 = joint[[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20],:]
        v = v2 - v1 
        # Normalize v
        v = v / np.linalg.norm(v, axis=1)[:, np.newaxis]

        # Get angle using arcos of dot product
        angle = np.arccos(np.einsum('nt,nt->n',
            v[[0,1,2,4,5,6,8,9,10,12,13,14,16,17,18],:], 
            v[[1,2,3,5,6,7,9,10,11,13,14,15,17,18,19],:])) # [15,]

        angle = np.degrees(angle) # Convert radian to degree

        # Inference gesture
        data = np.array([angle], dtype=np.float32)
        ret, results, neighbours, dist = knn.findNearest(data, 3)
        idx = int(results[0][0])
        
        # print(idx)
        print(gesture[idx])
    
    
    ## 손모양이 스파이더 제스쳐라면 True 반환
    if idx == 8 or idx == 9:
        return True
    
    return False


is_video_file = None

### mediapipe, sefie-segmentation(셀카 segmentation)
mp_drawing = mp.solutions.drawing_utils
mp_selfie_segmentation = mp.solutions.selfie_segmentation
selfie_segmentation = mp_selfie_segmentation.SelfieSegmentation(model_selection=1)

###################[손모양에 KNN 학습]
### mediapipe, hands(손 모양, 랜드마크 탐지)
gesture = {
    0:'fist', 1:'one', 2:'two', 3:'three', 4:'four', 5:'five',
    6:'six', 7:'rock', 8:'spiderman', 9:'yeah', 10:'ok', 11:'fy'
}
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
hands = mp_hands.Hands(
    max_num_hands=2,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5)
file = np.genfromtxt('data/gesture_train_fy.csv', delimiter=',')
angle = file[:,:-1].astype(np.float32)
label = file[:, -1].astype(np.float32)
knn = cv2.ml.KNearest_create()
knn.train(angle, cv2.ml.ROW_SAMPLE, label)
######################################

cap = cv2.VideoCapture(is_video_file if is_video_file else 0)
time.sleep(3)  

for i in range(60):
  ret, background = cap.read()

# 동영상 기록, 저장
fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
out = cv2.VideoWriter('videos/invisible2_output.mp4', fourcc, 20, (background.shape[1], background.shape[0]))
out2 = cv2.VideoWriter('videos/invisible2_original.mp4', fourcc, 20, (background.shape[1], background.shape[0]))


while(cap.isOpened()):
    ret, img = cap.read()
    if not ret:
        break
    
    # mediapipe를 위해 flip, BGR2RGB
    image = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    ################################[손 탐지 후, inference]
    image2 = image.copy()
    image2 = cv2.flip(image2, 1)
    hands_result = hands.process(image2)
    
    if hands_result.multi_hand_landmarks is not None:
        que_signal = get_hand_gesture(hands_result)
        print(que_signal)
    else:
        que_signal = False
    ###################################################

    if not que_signal:
        result = img
    else:
        # To improve performance, optionally mark the image as not writeable 
        image.flags.writeable = False
        results = selfie_segmentation.process(image)
        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        
        mask1 = results.segmentation_mask
        mask1 = np.where(mask1 > 0.1, 255, 0)
        mask1 = mask1.astype('uint8')

        mask_cloak = cv2.morphologyEx(mask1, op=cv2.MORPH_OPEN, kernel=np.ones((3, 3), np.uint8), iterations=2)
        mask_cloak = cv2.dilate(mask_cloak, kernel=np.ones((3, 3), np.uint8), iterations=1)
        mask_bg = cv2.bitwise_not(mask1)

        # Generate the final output
        res1 = cv2.bitwise_and(background, background, mask=mask_cloak)  # segmentation한 mask영역만 background에서 가져옴
        res2 = cv2.bitwise_and(img, img, mask=mask_bg)  # background 영역만 img에서 가져옴
        result = cv2.addWeighted(src1=res1, alpha=1, src2=res2, beta=1, gamma=0)

        # cv2.imshow('res1', res1)
        # cv2.imshow('res2', res2)

    # cv2.imshow('ori', img)
    cv2.imshow('result', result)
    
    out.write(result)
    out2.write(img)
    

    if cv2.waitKey(1) == ord('q'):
        break

out.release()
out2.release()
cap.release()