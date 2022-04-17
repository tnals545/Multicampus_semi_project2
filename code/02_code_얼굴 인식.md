# 얼굴 및 눈 인식



### 얼굴인식 코드

```python
import cv2

#웹캠에서 영상을 읽어온다
cap = cv2.VideoCapture(0) # 혹은 비디오파일
cap.set(3, 640) #WIDTH
cap.set(4, 480) #HEIGHT

#얼굴 인식 캐스케이드 파일 읽는다
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + '../data/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "/content/haarcascade_eye.xml")
while(True):
    # frame 별로 capture 한다
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    #인식된 얼굴 갯수를 출력
    print(len(faces))

    # 인식된 얼굴에 사각형을 출력한다
    for (x,y,w,h) in faces:
         cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)

    #화면에 출력한다
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
```

> 참고 자료 : https://circlestate.tistory.com/5

​	위 코드는 얼굴만 인식하는 코드입니다.



---



### 얼굴, 눈 인식 코드

```python
import cv2

font = cv2.FONT_ITALIC

def faceDetect():
    eye_detect = False
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + '../data/haarcascade_frontalface_default.xml')  # 얼굴찾기 haar 파일
    eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + '../data/haarcascade_eye.xml') # 눈찾기 haar 파일
 
    try:
        cam = cv2.VideoCapture(0) # 혹은 비디오파일
    except:
        print("camera loading error")
        return
 
    while True:
        ret, frame = cam.read()
        if not ret:
            break
 
        if eye_detect:
            info = "Eye Detention ON"
        else:
            info = "Eye Detection OFF"
 
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray,1.3, 5)
 
        eyes = eye_cascade.detectMultiScale(gray, 1.3, 5)
 
        #카메라 영상 왼쪽위에 위에 셋팅된 info 의 내용 출력
        cv2.putText(frame, info, (5,15), font, 0.5, (255,0, 255),1)
 
        for(x,y, w,h) in faces:
            cv2.rectangle(frame, (x,y), (x+w, y+h), (255,0,0), 2)  #사각형 범위
            cv2.putText(frame, "Detected Face", (x-5, y-5), font, 0.5, (255,255,0),2)  #얼굴찾았다는 메시지
            if eye_detect:  #눈찾기
                roi_gray = gray[y:y+h, x:x+w]
                roi_color = frame[y:y+h, x:x+w]
                eyes = eye_cascade.detectMultiScale(roi_gray)
                for (ex,ey,ew,eh) in eyes:
                    cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0,255,0), 2)
 
        cv2.imshow("frame", frame)
        k=cv2.waitKey(30)
 
        #실행 중 키보드 i 를 누르면 눈찾기를 on, off한다.
        if k == ord('i'):
            eye_detect = not eye_detect
        if k == 27:
            break
    cam.release()
    cv2.destroyAllWindows()
 
faceDetect()
```

> 참고 자료 : https://dodo-it.tistory.com/30

​	위 코드는 얼굴과 눈을 모두 인식하는 코드입니다.

