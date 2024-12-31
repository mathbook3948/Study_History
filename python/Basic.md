# Python 기초
## 기본 문법
### for 관련
#### enumerate
- 인덱스와 값을 iterable 객체의 튜플 형태로 반환한다
```python
exam_list = ["요소A", "요소B", "요소C", "요소D", "요소E"]

for index, value in enumerate(exam_list):
    print(f"인덱스 {index}: {value}")

# 출력:
# 인덱스 0: 요소A
# 인덱스 1: 요소B
# 인덱스 2: 요소C
# 인덱스 3: 요소D
# 인덱스 4: 요소E
```
- 인덱스의 시작 값을 변경할 수 있다
```python
exam_list = ["요소A", "요소B", "요소C", "요소D", "요소E"]

for index, value in enumerate(exam_list, start=1):
    print(f"인덱스 {index}: {value}")

# 출력:
# 인덱스 1: 요소A
# 인덱스 2: 요소B
# 인덱스 3: 요소C
# 인덱스 4: 요소D
# 인덱스 5: 요소E
```
#### range()
- 연속된 숫자를 생성하고 object 형태로 반환하는 함수
- 주로 for 반복문과 함께 사용된다
- 리스트나 튜플로 변환 가능하다
```python
# 기본 형태: range(stop) - 0부터 stop-1까지
for i in range(5):
    print(i)
# 출력: 0, 1, 2, 3, 4

# 시작과 끝 지정: range(start, stop)
for i in range(2, 5):
    print(i)
# 출력: 2, 3, 4

# 증가폭 지정: range(start, stop, step)
for i in range(0, 10, 2):
    print(i)
# 출력: 0, 2, 4, 6, 8

# 리스트로 변환
numbers = list(range(5))
print(numbers)  # [0, 1, 2, 3, 4]
```
### list 관련
#### reversed()
- 리스트를 뒤에서부터 재정렬하고 object 형태로 반환한다
```python
exam_list = ["요소A", "요소B", "요소C", "요소D", "요소E"]

reversed_list = list(reversed(exam_list))

print(reversed_list)

# 출력: ['요소E', '요소D', '요소C', '요소B', '요소A']
```
#### zip
- 같은 길이의 리스트를 같은 인덱스끼리 잘라서 튜플로 묶어 하나의 zip object 형태로 반환하는 함수이다
- 리스트로 변환이 가능하다
```python
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
result = list(zip(list1, list2))
print(result)  
# 출력: [(1, 'a'), (2, 'b'), (3, 'c')]

x = [1, 2, 3]
y = ['a', 'b', 'c']
z = ['!', '@', '#']
result = list(zip(x, y, z))
print(result)
# 출력: [(1, 'a', '!'), (2, 'b', '@'), (3, 'c', '#')]
```
### Comprehension
- 리스트, 딕셔너리, 세트 등의 자료구조를 생성할 때 사용하는 간단한 표현식
- 반복문과 조건문을 한 줄로 작성할 수 있다
#### List Comprehension
- [표현식 for 항목 in iterable if 조건식]
```python
# 기본 형태
numbers = [i for i in range(5)] 
# [0, 1, 2, 3, 4]

# 조건문 포함
evens = [i for i in range(10) if i % 2 == 0] 
# [0, 2, 4, 6, 8]

# 중첩 반복문
matrix = [(i, j) for i in range(2) for j in range(2)] 
# [(0,0), (0,1), (1,0), (1,1)]
```
## 모듈
### time
#### .sleep(seconds)
- 지정된 시간만큼 프로그램을 일시 정지한다
- 단위는 초(seconds)이며, 소수점도 사용 가능하다
```python
import time

print("시작")
time.sleep(1)  # 1초 대기
print("1초 지남")
time.sleep(0.5)  # 0.5초 대기
print("0.5초 더 지남")
```
### datetime
- 날짜 관련 기능을 제공해주는 모듈
#### datetime 클래스
- 날짜와 시간을 함께 처리하는 클래스
- date 객체(년,월,일)와 time 객체(시,분,초,마이크로초)를 포함
## .now()
- 현재 날짜와 시간을 datetime 객체 형태로 반환한다
```python
```python
from datetime import datetime

current = datetime.now()
print(current)  # 2024-12-31 11:07:00.123456

# 멤버 변수 접근 예시
print(current.year)      # 2024
print(current.month)     # 12
print(current.day)       # 31
print(current.hour)      # 15
print(current.minute)    # 30
print(current.second)    # 0
```
#### timedleta 클래스
- 시간의 간격(기간)을 나타내는 클래스
- 날짜/시간의 계산을 위해서 datetime 객체와 같이 쓰이는 경우가 많다
- 생성자의 주요 파라미터 주요 파라미터: days, weeks, hours, minutes, seconds, milliseconds, microseconds
```python
from datetime import datetime, timedelta

# timedelta 객체 생성
delta1 = timedelta(days=1)              # 1일
delta2 = timedelta(hours=24)            # 24시간
delta3 = timedelta(weeks=1)             # 1주
delta4 = timedelta(days=1, hours=12)    # 1일 12시간

# datetime과 함께 사용
now = datetime.now()
tomorrow = now + delta1
next_week = now + delta3

print(delta1)       # 1 day, 0:00:00
print(delta2)       # 1 day, 0:00:00
print(next_week)    # 2025-01-07 15:30:00.123456
```
## 어노테이션
### @property
- 클래스의 함수를 마치 멤버 변수처럼 사용할 수 있게 해주는 어노테이션
- getter/setter 기능을 제공한다
```python
class Person:
   def __init__(self, name, age):
       self._name = name  # private 변수임을 나타내기 위해 _를 붙임
       self._age = age

   @property
   def name(self):  # getter
       return self._name
   
   @name.setter # @property를 사용한 후에 .setter을 사용할 수 있다
   def name(self, value):  # setter
       if len(value) > 0:  # 유효성 검사 가능
           self._name = value
       else:
           raise ValueError("이름은 비어있을 수 없습니다")
       
    @property # 꼭 멤버 변수가 아니어도 가능하다
    def one(self):  # getter
        return 1

# 사용 예시
person = Person("홍길동", 20)
print(person.name)  # 홍길동 (마치 멤버변수처럼 접근)
person.name = "김철수"  # setter 호출
print(person.name)  # 김철수
person.name = ""  # ValueError: 이름은 비어있을 수 없습니다
```