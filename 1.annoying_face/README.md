# Annoying Face
`빵형의 개발도상국`님의 `annoying-orange-face(github)`을 리뷰하고 테스트 

## 환경 셋팅
 * python version : 3.8.10
 * conda env
 * 그외 환경설치는 아래 sh실행(mac or linux 환경 권고)
   * python libs 설치 및 내부에서 쓰이는 얼굴 랜드마크 모델(dlib model) 다운로드 및 압축해제
```bash
bash requirements.sh
```

## 실행
### python script
```bash
python main.py
```
### jupyter notebook
* [1.스노우카메라리뷰.ipynb](https://github.com/duc-ke/kaggle-playground-group/blob/main/1.annoying_face/jupyters/st1.%EC%8A%A4%EB%85%B8%EC%9A%B0%EC%B9%B4%EB%A9%94%EB%9D%BC%EB%A6%AC%EB%B7%B0%20-%20%EB%9D%BC%EC%9D%B4%EC%96%B8%EC%96%BC%EA%B5%B4%EB%A1%9C%EB%B0%94%EA%BF%94%EC%B9%98%EA%B8%B0.ipynb)
 * face detection 및 라이언이미지로 얼굴 대치 
* [2.어노잉오렌지리뷰.ipynb](https://github.com/duc-ke/kaggle-playground-group/blob/main/1.annoying_face/jupyters/st2.%EC%96%B4%EB%85%B8%EC%9E%89%EC%98%A4%EB%A0%8C%EC%A7%80%EB%A6%AC%EB%B7%B0.ipynb)
 * 오렌지이미지에 face landmarks(눈, 입)오려 붙이기
* [3.스노우카메라리뷰-advanced.ipynb](https://github.com/duc-ke/kaggle-playground-group/blob/main/1.annoying_face/jupyters/st3.%EC%8A%A4%EB%85%B8%EC%9A%B0%EC%B9%B4%EB%A9%94%EB%9D%BC%EB%A6%AC%EB%B7%B0%20-%20%EB%9D%BC%EC%9D%B4%EC%96%B8%EC%96%BC%EA%B5%B4%EB%A1%9C%EB%B0%94%EA%BF%94%EC%B9%98%EA%B8%B0-advanced.ipynb)
 * 얼굴 기울기를 따라 라이언 얼굴도 함께 움직여주는 얼굴 대치 

## 결과


## Links
* [annoying-orange-face(github)](https://github.com/kairess/annoying-orange-face)
* [내 얼굴로 어노잉 오렌지 만들기 youtube](https://www.youtube.com/watch?v=9VYUXchrMcM&t=178s)
* [68 face landmark model](https://github.com/davisking/dlib-models/blob/master/shape_predictor_68_face_landmarks.dat.bz2)

