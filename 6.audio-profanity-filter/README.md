# audio-profanity-filter(욕설음성 삐~ 처리)
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
* [st1.SpeechToText_연결및작동확인.ipynb](https://github.com/duc-ke/kaggle-playground-group/blob/main/6.audio-profanity-filter/st1.SpeechToText_%EC%97%B0%EA%B2%B0%EB%B0%8F%EC%9E%91%EB%8F%99%ED%99%95%EC%9D%B8.ipynb)
* [st2.short_audiofile_to_text.ipynb](https://github.com/duc-ke/kaggle-playground-group/blob/main/6.audio-profanity-filter/st2.%08short_audiofile_to_text.ipynb)
* * [st3.음성파일(mp3)에서욕을자동삐처리.ipynb](https://github.com/duc-ke/kaggle-playground-group/blob/main/6.audio-profanity-filter/st3.%EC%9D%8C%EC%84%B1%ED%8C%8C%EC%9D%BC(mp3)%EC%97%90%EC%84%9C%EC%9A%95%EC%9D%84%EC%9E%90%EB%8F%99%EC%82%90%EC%B2%98%EB%A6%AC.ipynb)

## 결과


## Links
* [audio-profanity-filter(github)](https://github.com/kairess/audio-profanity-filter)
* [Google cloud(STT) - STT(SpeechtoText) API 빠른시작](https://cloud.google.com/speech-to-text/docs/quickstart-client-libraries)
* [Google cloud(STT) - STT 오디오파일 to Text](https://cloud.google.com/speech-to-text/docs/sync-recognize)
* [Google cloud(STT) - 기본 사항](https://cloud.google.com/speech-to-text/docs/basics#select-model)
* [Google cloud(STT) - 가격 책정](https://cloud.google.com/speech-to-text/pricing)




