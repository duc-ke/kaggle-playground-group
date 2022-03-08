# CT Lung Segmentation(U-Net 폐 검출 segmentation)
* `빵형의 개발도상국`님의 `CT_lung_segmentation(github)`을 리뷰하고 테스트 

## 내용
* U-Net(keras) architecture를 이용한 폐 segmentation
* 상세 : 
  * kaggle 공개 데이터인 2d 폐 CT 이미지에서 폐 영역만 segmentation 
  * 모델 빌드, 학습, 예측까지 진행 

## 환경 셋팅
 * 데이터 전처리만 로컬에서 진행, 학습 및 inference는 colab이용
 * python version : 3.8.10
```bash
# 데이터 전처리 로컬에서 진행 시,
bash requirements.sh
```

## 실행
### jupyter notebook
* [st1_1_train(keras_simpleUnet)_colab.ipynb](https://github.com/duc-ke/kaggle-playground-group/blob/main/7.CT_lung_segmentation/st1_1_train(keras_simpleUnet)_colab.ipynb)
   * 아주 간단한 U-Net을 빌드하고 학습
* [st2_1_inference(keras_simpleUnet)_colab.ipynb](https://github.com/duc-ke/kaggle-playground-group/blob/main/7.CT_lung_segmentation/st2_1_inference(keras_simpleUnet)_colab.ipynb)
   * 학습된 모델을 로딩하여 예측


## 결과


## Links
* [CT_lung_segmentation(github)](https://github.com/kairess/CT_lung_segmentation)
* [Kaggle 폐 CT 데이터셋 원본 다운로드](https://www.kaggle.com/kmader/finding-lungs-in-ct-data)




