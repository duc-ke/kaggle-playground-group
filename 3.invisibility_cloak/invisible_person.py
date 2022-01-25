import cv2
import numpy as np
import mediapipe as mp
import time

is_video_file = None

####################[mediapipe 셀카 sementation 초기화]
### mediapipe, sefie-segmentation(셀카 segmentation)
mp_drawing = mp.solutions.drawing_utils
mp_selfie_segmentation = mp.solutions.selfie_segmentation
selfie_segmentation = mp_selfie_segmentation.SelfieSegmentation(model_selection=1)
###################################################

cap = cv2.VideoCapture(is_video_file if is_video_file else 0)
time.sleep(3) 

# Grap background image from first part of the video
for i in range(60):
  ret, background = cap.read()

# 동영상 기록, 저장
fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
# print(cap.get(cv2.CAP_PROP_FPS))
# print(cv2.CAP_PROP_FPS)

# ## FPS를 가져오는 코드가 에러가남(cap.get(cv2.CAP_PROP_FPS)). 고정 FPS를 전달
out = cv2.VideoWriter('videos/invisible_output.mp4', fourcc, 20, (background.shape[1], background.shape[0]))
out2 = cv2.VideoWriter('videos/invisible_original.mp4', fourcc, 20, (background.shape[1], background.shape[0]))

while(cap.isOpened()):
    ret, img = cap.read()
    if not ret:
        break

    #########################[셀카 sementation으로 mask생성]
    # mediapipe를 위해 flip, BGR2RGB
    image = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    # To improve performance, optionally mark the image as not writeable 
    image.flags.writeable = False
    results = selfie_segmentation.process(image)
    image.flags.writeable = True
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    
    
    mask1 = results.segmentation_mask
    # print(type(mask1), mask1.shape)    # np, (720, 1280)
    # print(np.unique(mask1))  # [0.0000000e+00 4.7018328e-40 4.7019029e-40 ... ]
    mask1 = np.where(mask1 > 0.1, 255, 0)
    mask1 = mask1.astype('uint8')
    ###################################################


    mask_cloak = cv2.morphologyEx(mask1, op=cv2.MORPH_OPEN, kernel=np.ones((3, 3), np.uint8), iterations=2)
    mask_cloak = cv2.dilate(mask_cloak, kernel=np.ones((3, 3), np.uint8), iterations=1)
    mask_bg = cv2.bitwise_not(mask1)
    # print(mask_bg)   # [[255 255..] [...]]
    # print(np.unique(mask_bg))  # [  0 255]
    cv2.imshow('mask_cloak', mask_cloak)

    res1 = cv2.bitwise_and(background, background, mask=mask_cloak) 
    res2 = cv2.bitwise_and(img, img, mask=mask_bg)  
    
    result = cv2.addWeighted(src1=res1, alpha=1, src2=res2, beta=1, gamma=0)

    cv2.imshow('res1', res1)
    cv2.imshow('res2', res2)

    # cv2.imshow('ori', img)
    cv2.imshow('result', result)
    out.write(result)
    out2.write(img)
    

    if cv2.waitKey(1) == ord('q'):
        break

out.release()
out2.release()
cap.release()