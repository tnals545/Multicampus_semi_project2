# FastAPI_By 기범

[본격적인 내용에 앞서 API가 무엇인지 부터 알아보자!](https://blog.wishket.com/api%EB%9E%80-%EC%89%BD%EA%B2%8C-%EC%84%A4%EB%AA%85-%EA%B7%B8%EB%A6%B0%ED%81%B4%EB%9D%BC%EC%9D%B4%EC%96%B8%ED%8A%B8/)

[API Youtube 설명](https://www.youtube.com/watch?v=iyFHfzCRHA8)



### 정의

​	현대적이고, 빠르며(고성능), 파이썬 표준 타입 힌트에 기초한 Python3.6+의 API를 빌드하기 위한 **웹 프레임워크**



---



### 주요 특징

- **빠름**: 매우 높은 성능을 갖춤. *<u>사용 가능한 가장 빠른 파이썬 프레임워크 중 하나</u>*.
- **빠른 코드 작성**: 약 200%에서 300%까지 기능 개발 속도 증가.
- **적은 버그**: 사람(개발자)에 의한 에러 약 40% 감소.
- **직관적**: 훌륭한 편집기를 지원. 모든 곳에서 자동완성. 적은 디버깅 시간.
- **쉬움**: 쉽게 사용하고 배우도록 설계. 적은 문서 읽기 시간.
- **짧음**: 코드 중복 최소화. 각 매개변수 선언의 여러 기능. 적은 버그.
- **견고함**: 준비된 프로덕션 용 코드를 얻으십시오.
- **표준 기반**: API에 대한(완전히 호환되는) 개방형 표준 기반.



---



### FastAPI 기초_단계별 요약

#### 1단계: 설치

```python
!pip install fastapi[all]
!pip install fastapi nest-asyncio pyngrok uvicorn
```

​	FastAPI 설치하는데, 모든 기능을 사용하기 위해 [all]로 설치했다. 부분적으로도 설치가 가능하다. uvicorn은 서버 역할을 하는데, 가상환경을 사용한다면 설치해주자.



#### 2단계: FastAPI import

```python
from fastapi import FastAPI
```

​	`FastAPI`는 API에 대한 모든 기능을 제공하는 파이썬 클래스이다.



#### 3단계: FastAPI 인스턴스

```python
app = FastAPI()
```

​	`app` 변수는 `FastAPI` 클래스의 인스턴스가 된다. 즉, 이것은 모든 API를 생성하기 위한 **상호작용의 주요 지점**이 된다.



#### 4단계: 경로 동작 생성

##### 경로

```python
@app.get("/")
async def root():
    return {"message": "Hello World"}
```

​	"경로"는 첫 번째 `/`에서 시작하는 URL의 마지막 부분을 나타낸다.

> ''경로"는 일반적으로 "앤드포인트" 또는 "라우트"라고도 불린다.

```python
https://example.com/items/foo
/items/foo # 경로
```



##### 동작

 "동작(Operation)"은 HTTP **"메소드"** 중 하나이다. 기본적인 동작 메소드는 아래와 같다.

- `POST`: 데이터를 생성하기 위해.
- `GET`: 데이터를 읽기 위해.
- `PUT`: 데이터를 업데이트하기 위해.
- `DELETE`: 데이터를 삭제하기 위해.

​	HTTP 프로토콜에서는 이러한 "메소드"를 하나(또는 이상) 사용하여 **각 경로와 통신**할 수 있습니다. 그리고 이러한 특정 행동을 수행하기 때문에 각 HTTP 메소드들을 '동작'이라고 부른다.



##### 코드해석

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}
```

​	위 코드는 루트`/` 로 접속하면 JSON 형태의 데이터를 리턴한다는 의미다. 실행시켜 API에 접속해 보면 JSON 데이터가 출력되는 것을 확인할 수 있다.



---



### 경로 매개변수

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/items/{item_id}")
async def read_item(item_id):
    return {"item_id": item_id}
```

​	경로 매개변수 `item_id`의 값은 함수의 `item_id` 인자로 전달된다. 쉽게 말해 예제를 실행하고 경로를 '/items/foo'로 이동하면, {"item_id":"foo"} 라는 결과가 나올 것이다.



```python
@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}
```

​	이렇게 함수에 있는 경로 매개변수의 타입을 선언할 수도 있다. 이때는 경로 매개변수는 반드시 int로 입력해야 하고,  그렇지 않으면 오류가 나올 것이다. '/items/3'을 입력해 확인해 보자.



```python
from fastapi import FastAPI

app = FastAPI()


@app.get("/users/me")
async def read_user_me():
    return {"user_id": "the current user"}

@app.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}
```

​	/users/me는 고정 경로이다. 이는 현재 사용자의 데이터를 가져온다. 이 외에 사용자 ID를 이용해 특정 사용자의 정보를 가져오는 경로로는 `/users/{user_id}`도 있다. 여기서 주의할 점은 순서인데, 만약 두 코드의 순서가 바뀌면 매개변수 `user_id`의 값을 `"me"`라고 생각하여 다른 결과를 가져올 수 있다.



```python
from enum import Enum

from fastapi import FastAPI

class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"

app = FastAPI()

@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name == ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}
```

​	**유효하고 미리 정의할 수 있는** 경로 매개변수 값을 원한다면 파이썬 표준 `Enum`을 사용하면 된다. 다음 코드를 사용하면 열겨형 클래스를 사용하는 경로 매개변수를 만들 수 있다.



---



### 쿼리 매개변수

```python
from fastapi import FastAPI

app = FastAPI()

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip : skip + limit]
```

​	쿼리는 URL에서 `?` 후에 나오고 `&`으로 구분되는 키-값 쌍의 집합이다. 위 코드에서는 skip이 0의 값을 갖고, limit이 10의 값을 기본값으로 갖는다. 그리고 '/items/'와 '/?skip=0&limit=10'로 이동한 경우 동일한 페이지를 가져온다.



```python
from typing import Optional

from fastapi import FastAPI

app = FastAPI()


@app.get("/items/{item_id}")
async def read_item(item_id: str, q: Optional[str] = None):
    if q:
        return {"item_id": item_id, "q": q}
    return {"item_id": item_id}
```

​	같은 방법으로 기본값을 `None`으로 설정하여 선택적 매개변수를 선언할 수 있다. 이 경우 함수 매개변수 `q`는 선택적이며 기본값으로 `None` 값이 된다. `item_id`가 경로 매개변수이고 `q`는 경로 매개변수가 아닌 쿼리 매개변수이다.

​	`q`가 `= None`이므로 선택적이라는 것을 인지하고, `Optional[str]`은 편집기에게 코드에서 오류를 찾아낼 수 있게 도와준다.

​	

```python
# Query Parameter
/users?id=123  # 아이디가 123인 사용자를 가져온다.

# Path Variable
/users/123  # 아이디가 123인 사용자를 가져온다.

/users  # 사용자 목록을 가져온다.
/users?occupation=programer  # 프로그래머인 사용자 목록을 가져온다.
/users/123  # 아이디가 123인 사용자를 가져온다.
```

​	Query string과 Path variable의 사용을 구분할 때, 일반적으로 우리가 어떤 자원(데이터)의 위치를 특정해서 보여줘야 할 경우 Path variable을 쓰고, 정렬하거나 필터해서 보여줘야 할 경우에 Query parameter를 쓴다. [더 자세히 학습하기](https://velog.io/@jcinsh/Query-string-path-variable)



---



### 문서화

경로 가장 마지막에 `/docs`를 입력하여 자동 대화식 API 문서를 확인한다.

> /docs는 `swagger`로 RestAPI를 JSON으로 표현해줌.
>
> /redoc은 open-source tool인데, 문서를 생성해준다.
>
> /openapi.json은 api를 만들어준다.



asyncio는 비동기 프로그래밍을 위한 모듈로, CPU 작업과 I/O를 병렬로 처리하게 해준다.

동기 처리는 특정 작업이 끝나면 다음 작업을 처리하는 순차처리 방식이고, 비동기 처리는 여러 작업을 처리하도록 예약한 뒤 작업이 끝나면 결과를 받는 방식이다.
