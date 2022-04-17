# FastAPI



### 사전 준비

```python
# 구글 코랩에서 fastapi 이용을 위한 installation
!pip install fastapi nest_asyncio pyngrok uvicorn
```

```python
# ngrok authtoken - 임시 도메인 할당 
!ngrok authtoken #개인 발급
```

```python
# aiofiles : 비동기 파일 입출력을 위한 라이브러리
# multipart 이용을 위한 installation
!pip install aiofiles python-multipart
```



---



### 라이브러리

```python
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, FileResponse
from pyngrok import ngrok
import nest_asyncio
from typing import Optional, List
import uvicorn
from fastapi import File, UploadFile
import os
import numpy as np
import urllib.request
import requests
import json
```



---



### code

**Naver Clova AI Speech 이용을 위한 class**

```python
class ClovaSpeechClient:
  # Clova Speech invoke URL
  invoke_url = 'url 발급'
  # Clova Speech secret key
  secret = 'key 발급'

  def req_upload(self, file, completion, callback=None, userdata=None, forbiddens=None, boostings=None,
                  wordAlignment=True, fullText=True, diarization=None):
      request_body = {
          'language': 'enko',
          'completion': completion,
          'callback': callback,
          'userdata': userdata,
          'wordAlignment': wordAlignment,
          'fullText': fullText,
          'forbiddens': forbiddens,
          'boostings': boostings,
          'diarization': diarization,
      }
      headers = {
          'Accept': 'application/json;UTF-8',
          'X-CLOVASPEECH-API-KEY': self.secret
      }
      print(json.dumps(request_body, ensure_ascii=False).encode('UTF-8'))
      files = {
          'media': open(file, 'rb'),
          'params': (None, json.dumps(request_body, ensure_ascii=False).encode('UTF-8'), 'application/json')
      }
      response = requests.post(headers=headers, url=self.invoke_url + '/recognizer/upload', files=files)
      return response
```



**FastAPI를 이용한 웹 사이트**

```python
app = FastAPI()

# 웹 페이지 첫 화면
@app.get('/')
def read_root():
  return {'Hello, This is junior naver'}


# 영상 혹은 음성 -> text로 출력
@app.post('/speech/text')
async def speech_text(files: List[UploadFile] = File(...)):
  for file in files:
    contents = await file.read()
    with open(os.path.join('/content/',file.filename), 'wb') as fp:
      fp.write(contents)
    # Naver Clova AI Speech 호출
    if __name__ == '__main__':

      res = ClovaSpeechClient().req_upload(file=(os.path.join('/content/' + file.filename)), completion='sync')

    result = res.json()['text']

  return HTMLResponse(content=F"<h1>{result}", status_code=200)



# 영상 혹은 음성 -> text -> 한국어로 번역된 text
@app.post('/speech/translation')
async def speech_text(files: List[UploadFile] = File(...)):
  for file in files:
    contents = await file.read()
    with open(os.path.join('/content/',file.filename), 'wb') as fp:
      fp.write(contents)
    
    # Naver Clova AI Speech 호출
    if __name__ == '__main__':
      res = ClovaSpeechClient().req_upload(file=(os.path.join('/content/' + file.filename)), completion='sync')
    
	result = res.json()['text']
    
    
    # Naver Cloud의 Papago text translation 호출
    client_id = "id 발급"
    client_secret = "key 발급"
    encText = urllib.parse.quote(result)
    data = "source=en&target=ko&honorific=True&text=" + encText  # 영어 한국어 설정
    url = "https://naveropenapi.apigw.ntruss.com/nmt/v1/translation"
    request = urllib.request.Request(url)
    request.add_header("X-NCP-APIGW-API-KEY-ID",client_id)
    request.add_header("X-NCP-APIGW-API-KEY",client_secret)
    response = urllib.request.urlopen(request, data=data.encode("utf-8"))
    rescode = response.getcode()
    if(rescode==200):
        response_body = response.read()
        print(response_body.decode('utf-8'))
    else:
        print("Error Code:" + rescode)
        
    mas = response_body.decode('utf-8')
    translation = mas.split('"')[-2]

  return HTMLResponse(content=F"<h1>{translation}", status_code=200)


# 영상 혹은 음성 -> text -> 한국어로 번역된 text -> 음성파일로 저장
@app.post('/speech/voice')
async def speech_text(files: List[UploadFile] = File(...)):
  for file in files:
    contents = await file.read()
    with open(os.path.join('/content/',file.filename), 'wb') as fp:
      fp.write(contents)
    
        
    # Naver Clova AI Speech 호출
    if __name__ == '__main__':
      res = ClovaSpeechClient().req_upload(file=(os.path.join('/content/' + file.filename)), completion='sync')
    
    result = res.json()['text']
    
    
        
    # Naver Cloud의 Papago text translation 호출
    client_id = "id 발급"
    client_secret = "key 발급"
    encText = urllib.parse.quote(result)
    data = "source=en&target=ko&honorific=True&text=" + encText  # 영어 한국어 설정
    url = "https://naveropenapi.apigw.ntruss.com/nmt/v1/translation"
    request = urllib.request.Request(url)
    request.add_header("X-NCP-APIGW-API-KEY-ID",client_id)
    request.add_header("X-NCP-APIGW-API-KEY",client_secret)
    response = urllib.request.urlopen(request, data=data.encode("utf-8"))
    rescode = response.getcode()
    if(rescode==200):
        response_body = response.read()
        print(response_body.decode('utf-8'))
    else:
        print("Error Code:" + rescode)
        
    mas = response_body.decode('utf-8')
    translation = mas.split('"')[-2]

    
    # Naver Clova Voice 호출
    encText = urllib.parse.quote(translation)
    data = "speaker=nara&volume=0&speed=0&pitch=0&format=mp3&text=" + encText;
    url = "https://naveropenapi.apigw.ntruss.com/tts-premium/v1/tts"
    request = urllib.request.Request(url)
    request.add_header("X-NCP-APIGW-API-KEY-ID",client_id)
    request.add_header("X-NCP-APIGW-API-KEY",client_secret)
    response = urllib.request.urlopen(request, data=data.encode('utf-8'))
    rescode = response.getcode()
    if(rescode==200):
        response_body = response.read()
        fn = file.filename.split('.')[0]
        with open('./%s_voice.mp3'% fn, 'wb') as f:
            f.write(response_body)
    else:
        print("Error Code:" + rescode)
    file_path = os.getcwd() + '/%s_voice.mp3'% fn
  return FileResponse(path=file_path, media_type='application/octet-stream',
                      filename= '%s_voice.mp3'% fn)


# 사진 파일로 나이 인식 -> 메세지 송출
@app.post('/face/age')
async def speech_script(files: List[UploadFile] = File(...)):
  for file in files:
    contents = await file.read()
    with open(os.path.join('/content/',file.filename), 'wb') as fp:
      fp.write(contents)
      client_id = "id 발급"
      client_secret = "key 발급"
      url = "https://naveropenapi.apigw.ntruss.com/vision/v1/face"
      files = {'image': open(os.path.join('/content/',file.filename), 'rb')}
      headers = {'X-NCP-APIGW-API-KEY-ID': client_id, 'X-NCP-APIGW-API-KEY': client_secret }
      response = requests.post(url,  files=files, headers=headers)
      rescode = response.status_code
      if(rescode==200):
          print (response.text)
      else:
          print("Error Code:" + rescode)
      res = response.json()
      low = int(res['faces'][0]['age']['value'].split('~')[0])
      high = int(res['faces'][0]['age']['value'].split('~')[1])
      if (low + high) / 2 < 15:
        msg = "시청 불가능한 연령입니다.(15세 미만)"
      else:
        msg = "시청 가능한 연령입니다.(15세 이상)"

  return HTMLResponse(content=F"<h1>{msg}", status_code=200)


ngrok_tunnel = ngrok.connect(8000)
print('Public URL:' , ngrok_tunnel.public_url)
nest_asyncio.apply()
uvicorn.run(app, host='0.0.0.0', port=8000)
```





