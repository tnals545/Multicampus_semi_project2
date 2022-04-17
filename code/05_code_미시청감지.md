# 미시청 감지 코드



### 라이브러리

```python
import cv2, dlib
import numpy as np
from imutils import face_utils
from keras.models import load_model
import time
```

- dlib
  - OpenCV와 유사하게 이미지 프로세싱 커뮤니티에서 폭넓게 도입하고 있는 강력한 라이브러리
  - 주로 얼굴 탐지(detection)와 정렬(alignment) 모듈을 사용

- imutils
  -  OpenCV가 제공하는 기능 중에 좀 복잡하고 사용성이 떨어지는 부분을 보완해 주는 라이브러리
  
  

> 참고 자료
>
> - https://a292run.tistory.com/entry/Face-Recognition-with-Dlib-in-Python-1
> - https://enjoyimageprocessing.tistory.com/entry/imutils-package-%EA%B8%B0%EB%8A%A5



---



### Code

```python
count = 0

IMG_SIZE = (34, 26)

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')

# CNN 딥러닝 완료한 학습모델 불러오기
model = load_model('models/2022_03_23_10_18_14.h5')
model.summary()

# 눈 위치(좌표)를 이용한 이미지 크기 설정 함수 만들기
def crop_eye(img, eye_points):
    x1, y1 = np.amin(eye_points, axis=0)
    x2, y2 = np.amax(eye_points, axis=0)
    cx, cy = (x1 + x2) / 2, (y1 + y2) / 2
    
    w = (x2 - x1) * 1.2
    h = w * IMG_SIZE[1] / IMG_SIZE[0]
    
    margin_x, margin_y = w / 2, h / 2
    
    min_x, min_y = int(cx - margin_x), int(cy - margin_y)
    max_x, max_y = int(cx + margin_x), int(cy + margin_y)

    eye_rect = np.rint([min_x, min_y, max_x, max_y]).astype(np.int)
    
    eye_img = gray[eye_rect[1]:eye_rect[3], eye_rect[0]:eye_rect[2]]
    
    return eye_img, eye_rect


# 메인코드

# OpenCV
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, img_ori = cap.read()

    if not ret:
        break

    img_ori = cv2.resize(img_ori, dsize=(0, 0), fx=0.5, fy=0.5)

    img = img_ori.copy()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = detector(gray)

    for face in faces:
        shapes = predictor(gray, face)
        shapes = face_utils.shape_to_np(shapes)

        eye_img_l, eye_rect_l = crop_eye(gray, eye_points=shapes[36:42])
        eye_img_r, eye_rect_r = crop_eye(gray, eye_points=shapes[42:48])

        eye_img_l = cv2.resize(eye_img_l, dsize=IMG_SIZE)
        eye_img_r = cv2.resize(eye_img_r, dsize=IMG_SIZE)
        

        eye_input_l = eye_img_l.copy().reshape((1, IMG_SIZE[1], IMG_SIZE[0], 1)).astype(np.float32) / 255.
        eye_input_r = eye_img_r.copy().reshape((1, IMG_SIZE[1], IMG_SIZE[0], 1)).astype(np.float32) / 255.

        pred_l = model.predict(eye_input_l)
        pred_r = model.predict(eye_input_r)

        # visualize
        state_l = '%.1f' if pred_l > 0.1 else '%.1f'
        state_r = '%.1f' if pred_r > 0.1 else '%.1f'

        state_l = state_l % pred_l
        state_r = state_r % pred_r

        cv2.rectangle(img, pt1=tuple(eye_rect_l[0:2]), pt2=tuple(eye_rect_l[2:4]), color=(255,0,0), thickness=2)
        cv2.rectangle(img, pt1=tuple(eye_rect_r[0:2]), pt2=tuple(eye_rect_r[2:4]), color=(255,0,0), thickness=2)

        cv2.putText(img, state_l, tuple(eye_rect_l[0:2]), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255,255,255), 2)
        cv2.putText(img, state_r, tuple(eye_rect_r[0:2]), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255,255,255), 2)
        
        # 눈을 양쪽 다 감았을 때 일정 시간 후에 화면에 warning 경고 문구 표시
        # warning 문구 표시 후 5초 안에 눈을 뜨지 않으면 OpenCV 종료
        if pred_l <= 0.1 and pred_r <= 0.1:
            count += 1
            print(count)
            cv2.putText(img, str(count),(465,130), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,0,255), 2)
            time.sleep(1)
            if count > 5:
                org=(400,400) 
                text="warning" 
                font=cv2.FONT_HERSHEY_SIMPLEX 
                cv2.putText(img, text, org, font, 1.5, (0,0,255), 2)
                if count > 10:
                  print('영상 재생을 중지합니다.')
                  break
        else:
            count = 0
    
    
    cv2.imshow('result', img)
    if count > 10:
        break

    if (cv2.waitKey(1) == '27'):
        break
        
        
cap.release()
cv2.destroyAllWindows()
```

>  참고 자료
>
> - https://github.com/kairess/eye_blink_detector/blob/master/test.py
> - https://kali-live.tistory.com/13