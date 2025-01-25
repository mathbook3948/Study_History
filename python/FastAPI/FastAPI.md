# FastAPI 왜씀?
1. Django보다 2배 빠름 ㄷㄷ
2. 문법 자체가 쉬움
3. 비동기 처리가 가능
4. 기능들을 단위별로 나눠서 구현하기 쉬움
# FastAPI
## 설치
```shell
pip install fastapi
pip install "uvicorn[standard]"
```
## 서버 실행
```shell
uvicorn main:app --reload
# main : 파이썬 파일 이름(main.py)
# app : 해당 파일 내에서 생성한 객체를 담고있는 변수 이름
# --reload : 코드가 변경될 때 서버를 자동으로 재시작
```
- 기본으로 포트 8000에서 실행된다

### API 문서
- `/docs`또는 `/redoc`으로 이동할 경우 자동 생성된 API 문서를 볼 수 있다
## FastAPI 빠른 시작
### 1. FastAPI import, 객체 생성
```python
from fastapi import FastAPI

app = FastAPI()
```
- FastAPI를 import하고 객체를 생성한다
### 2. 경로 생성
```python
@app.get("/")
async def root():
    return {"message" : "Hello World"}
```
- `@app.get(path), @app.post(path)`등을 이용하여 해당 경로로 요청이 오면 처리할 함수를 만든다 
#### 경로 매핑 어노테이션(`@app`)
- `.get(path)`
- `.post(path)`
- `.put(path)`
- `.delete(path)`
- `.options(path)`
- `.head(path)`
- `.patch(path)`
- `.trace(path)`
#### 매핑되는 함수
```python
async def root():
    return {"message" : "Hello World"}

def root():
    return {"message" : "Hello World"}
```
- 비동기, 동기를 원하는대로 선택할 수 있다
- 비동기를 자유롭게 이용하기때문에 FastAPI의 속도가 빠르다(성능 최적화가 가능하다)
### 3. 컨텐츠 반환
- `dict`, `list` 등을 자유롭게 반환할 수 있다 

## 매개변수
### 경로 매개변수
```python
@app.get("/items/{item_id}")
async def read_item(item_id):
    return {"item_id": item_id}
```
- 경로에 f-string 문법을 이용하여 경로 매개변수를 선언할 수 있다
```python
@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}
```
- 파이썬의 타입 어노테이션을 이용하여 매개변수의 타입을 지정 가능하다. 타입을 지정하면 FastAPI에서는 자동으로 해당 타입으로 변환을 시도 한다
```python
from enum import Enum

class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"

@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}
```
- Enum, 타입(선택)을 상속한 클래스를 만들고, 타입 어노테이션으로 사용함으로 매개변수로 들어오는 값을 제한할 수 있다
#### 경로를 포함하는 경로 매개변수
- 경로에는 `/`가 포함되어있을 수 있기 때문에 Starlette의 옵션을 이용해야 한다
```python
@app.get("/files/{file_path:path}") # :path 를 이용하면 "/"이 포함된 경로도 문자열로 받아온다
async def read_file(file_path: str):
    return {"file_path": file_path}
```
##### 공식 문서의 팁
- 매개변수가 가져야 하는 값이 /home/johndoe/myfile.txt와 같이 슬래시로 시작(/)해야 할 수 있습니다.
- 이 경우 URL은: /files//home/johndoe/myfile.txt이며 files과 home 사이에 이중 슬래시(//)가 생깁니다.
#### 순서 문제
```python
@app.get("/users/me")
async def read_user_me():
    return {"user_id": "the current user"}


@app.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}
```
- `/users/me`로 요청이 들어왔을 때 요청 처리는 위에서부터 순차적으로 진행되기 때문에 `/users/me` 다음에 `/users/{user_id}`을 선언해야 한다
- 그렇지 않으면 `/users/me`도 `/users/{user_id}`의 `user_id`가 `"me"`인 것으로 인식할수도 있다.
- **근데 이따위로 코딩하면 뒷목잡을듯**
### 쿼리 매개변수
- 경로 매개변수의 일부가 아닌 함수 매개변수를 선언하면 "쿼리" 매개변수(?,& 써가지고 값 보내는거)로 자동 해석된다
```python
@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip : skip + limit]
```
- 기본적으로 타입은 문자열이지만, 경로 매개변수와 비슷하게 타입 어노테이션을 사용하면 자동으로 해당 타입으로 변환한다 
- 선택적으로(기본값을 설정해서) 매개변수를 받을 수 있다
```python
@app.get("/items/{item_id}")
async def read_item(item_id: str, q: str | None = None):
    if q:
        return {"item_id": item_id, "q": q}
    return {"item_id": item_id}
```
- 이 경우 함수 매개변수 q는 선택적이며 기본값으로 None 값이 된다
```python
@app.get("/items/{item_id}")
async def read_user_item(
    item_id: str, needy: str, skip: int = 0, limit: int | None = None):
    item = {"item_id": item_id, "needy": needy, "skip": skip, "limit": limit}
    return item
```
- 필수 쿼리 매개변수와 비필수 쿼리 매개변수를 동시에 선언 할 수 있다
#### 공식 문서의 팁
- 경로 매개변수와 마찬가지로 Enum을 사용할 수 있다
#### 필수 쿼리 매개변수
```python
@app.get("/items/{item_id}")
async def read_user_item(item_id: str, needy: str):
    item = {"item_id": item_id, "needy": needy}
    return item
# 여기서 needy는 기본값을 지정해주지 않아서 필수 쿼리 매개변수이다
```
### 여러 경로/쿼리 매개변수
- 여러 경로 매개변수와 쿼리 매개변수를 동시에 선언할 수 있으며 각 매개변수는 이름으로 감지된다(순서 상관x)
```python
@app.get("/users/{user_id}/items/{item_id}")
async def read_user_item(
    user_id: int, item_id: str, q: str | None = None, short: bool = False
):
    item = {"item_id": item_id, "owner_id": user_id}
    if q:s
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item
```
## 요청 본문(body)
- Pydantic 라이브러리를 활용하여 요청 본문을 dict로 변환한다

## 라우팅
- 여러 파일에서 각각 라우트를 정의하고 불러올 수 있다.
### 

## 기타
- FastAPI는 Starlette를 직접 상속하는 클래스이다
- FastAPI 매개변수 타입 자동 매핑은 Pydantic에 의해 수행된다