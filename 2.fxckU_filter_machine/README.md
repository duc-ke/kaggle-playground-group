# Fxck You Filter
* `빵형의 개발도상국`님의 `Rock-Paper-Scissors-Machine(github)`을 리뷰하고 테스트 
* 위 github에는 1.가위바위보 머신, 2.fxck u 필터 머신이 포함 되어있음. 

## 내용
* 해당 코드를 실행시, 비디오영상(캠 혹은 동영상 파일)으로 부터 손모양, 가위바위보를 인식
* 손가락욕 행위시 해당 손을 모자이크처리하여 출력 

## 환경 셋팅
 * python version : 3.8.10
 * conda env
 * 그외 환경설치는 아래 sh실행
```bash
bash requirements.sh
```

## 실행
### python script
```bash
# 1. 손 하나를 인식, 가위바위보 출력
python single.py
# 2. 두 손을 인식, 가위바위보 게임
python dual.py
# 3. 클릭마다 캠영상의 fxck u 이미지 데이터셋을 추가 수집, csv파일 생성
python gather_dataset.py
# 4. 가운데손가락 욕을 인식, 모자이크 처리
python fy_filter.py
```
### jupyter notebook
* [1.-리뷰.ipynb](https://github.com/duc-ke/kaggle-playground-group/blob/main/1.annoying_face/jupyters/st1.%EC%8A%A4%EB%85%B8%EC%9A%B0%EC%B9%B4%EB%A9%94%EB%9D%BC%EB%A6%AC%EB%B7%B0%20-%20%EB%9D%BC%EC%9D%B4%EC%96%B8%EC%96%BC%EA%B5%B4%EB%A1%9C%EB%B0%94%EA%BF%94%EC%B9%98%EA%B8%B0.ipynb)
* [2.-리뷰.ipynb](https://github.com/duc-ke/kaggle-playground-group/blob/main/1.annoying_face/jupyters/st2.%EC%96%B4%EB%85%B8%EC%9E%89%EC%98%A4%EB%A0%8C%EC%A7%80%EB%A6%AC%EB%B7%B0.ipynb)

## 결과


## Links
* [annoying-orange-face(github)](https://github.com/kairess/annoying-orange-face)
* [가운데 손가락 모자이크 알고리즘 만들기 youtube](https://youtu.be/tQeuPrX821w)
* [가위바위보 기계 만들기 - 손가락 인식 인공지능 youtube](https://youtu.be/udeQhZHx-00)
* [손가락 인식 볼륨 조절기 만들기 youtube](https://youtu.be/CJSobYHYDo4)


