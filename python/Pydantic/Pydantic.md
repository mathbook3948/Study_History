# Pydantic이란?

Pydantic은 Python에서 사용하는 데이터 검증용 라이브러리입니다. 다음과 같은 용도로 널리 사용됩니다:

## 기본 사용법
```python
from pydantic import BaseModel

class User(BaseModel):
    name: str
    age: int
    email: str | None = None  # 선택적 필드
```
## 주요 기능
1. 데이터 타입 검증
   ```python
   user = User(name="John", age="25")  # age는 문자열이지만 자동으로 int로 변환
   ```
2. 기본값 설정
   ```python
   class Settings(BaseModel):
       database_url: str
       api_key: str = "default-key"     # 기본값 설정
       debug: bool = False
   ```
3. 필드 검증
   ```python
   from pydantic import BaseModel, EmailStr, Field

   class User(BaseModel):
       name: str = Field(..., min_length=2)  # 최소 2글자
       age: int = Field(..., ge=0, le=150)   # 0-150 사이
       email: EmailStr                       # 이메일 형식 검증
   ```
4. 복잡한 데이터 모델
   ```python
   from typing import List

   class Item(BaseModel):
       name: str
       price: float

   class Order(BaseModel):
       user_id: int
       items: List[Item]  # 중첩 모델 지원
   ```
## 활용 사례
1. FastAPI와 함께 사용
   ```python
   from fastapi import FastAPI
   from pydantic import BaseModel

   app = FastAPI()

   class Item(BaseModel):
       name: str
       price: float

   @app.post("/items/")
   def create_item(item: Item):
       return item
   ```
2. 환경 설정 관리
   ```python
   class DatabaseSettings(BaseModel):
       host: str
       port: int
       username: str
       password: str
       database: str = "default"
   ```
## 장점
- 자동 타입 변환
- 상세한 에러 메시지
- IDE 자동완성 지원
- JSON 스키마 자동 생성
- 고성능 데이터 파싱
- Python 타입 힌트와의 통합