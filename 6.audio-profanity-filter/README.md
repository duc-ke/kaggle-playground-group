# Predict stock & crypto price
* `빵형의 개발도상국`님의 `audio-profanity-filter(github)`을 리뷰하고 테스트 

## 내용
* 욕설이 들어간 음성을 자동으로 삐처리를 해주는 프로그램
* 상세 : 
  * 구글 cloud의 STT(Speech To Text)를 이용하여 음성 보이스를 text로 변환
  * 변환된 text에서 욕설 단어를 찾아서 '삐(Beep)'소리로 overlay

## 환경 셋팅
 * python version : 3.8.10
```bash
bash requirements.sh
```

## 실행
### jupyter notebook
* [st1.sample.ipynb]()
* [st2.sample2.ipynb]()

## 결과


## Links
* [audio-profanity-filter(github)](https://github.com/kairess/audio-profanity-filter)
* [Google cloud(STT) - STT(SpeechtoText) API 빠른시작](https://cloud.google.com/speech-to-text/docs/quickstart-client-libraries)
* [Google cloud(STT) - STT 오디오파일 to Text](https://cloud.google.com/speech-to-text/docs/sync-recognize)
* [Google cloud(STT) - 기본 사항](https://cloud.google.com/speech-to-text/docs/basics#select-model)
* [Google cloud(STT) - 가격 책정](https://cloud.google.com/speech-to-text/pricing)




