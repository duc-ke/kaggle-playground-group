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
* [1.가위바위보리뷰.ipynb](https://github.com/duc-ke/kaggle-playground-group/blob/main/2.fxckU_filter_machine/jupyters/st1.%EA%B0%80%EC%9C%84%EB%B0%94%EC%9C%84%EB%B3%B4_%EC%9D%B8%EC%8B%9D%EA%B8%B0%EB%8A%A5%EB%A6%AC%EB%B7%B0.ipynb)
* [2.fxcku영상모자이크처리리뷰.ipynb](https://github.com/duc-ke/kaggle-playground-group/blob/main/2.fxckU_filter_machine/jupyters/st2.fxckU%ED%95%84%ED%84%B0%EB%A6%AC%EB%B7%B0.ipynb)

## 결과


## Links
* [Rock-Paper-Scissors-Machine(github)](https://github.com/kairess/Rock-Paper-Scissors-Machine)
* [가운데 손가락 모자이크 알고리즘 만들기 youtube](https://youtu.be/tQeuPrX821w)
* [가위바위보 기계 만들기 - 손가락 인식 인공지능 youtube](https://youtu.be/udeQhZHx-00)
* [손가락 인식 볼륨 조절기 만들기 youtube](https://youtu.be/CJSobYHYDo4)


