# 정규표현식(Regular Expressions)
- 특정한 규칙을 가진 문자열의 집합을 표현하는데 사용하는 형식 언어
- `re` 라는 모듈을 통해 구현

## re 모듈의 주요 메서드
```python
import re
```

### .search(pattern: str, string: str)
- 문자열 전체에서 패턴이 매치되는 첫 번째 위치를 찾아서 Match 객체를 반환
- 매치되는 패턴이 없으면 None 반환
```python
result = re.search(r'\d+', 'abc123def')  # '123' 매치
print(result.group())  # '123'
```

### .match(pattern: str, string: str)
- 문자열의 처음부터 패턴이 매치되는지 검사
- 매치되면 Match 객체 반환, 아니면 None 반환
```python
result = re.match(r'\d+', '123abc')  # '123' 매치
result2 = re.match(r'\d+', 'abc123')  # None 반환
```

### .findall(pattern: str, string: str)
- 문자열에서 패턴과 매치되는 모든 부분을 찾아서 리스트로 반환
```python
result = re.findall(r'\d+', 'abc123def456')  # ['123', '456'] 반환
```

### .finditer(pattern: str, string: str)
- findall과 비슷하지만 iterator 객체를 반환
- 각 매치에 대한 Match 객체를 순회할 수 있음
```python
for match in re.finditer(r'\d+', 'abc123def456'):
    print(match.group())
```

### Match 클래스
- 정규표현식 매치의 결과를 담고 있는 객체
- 주요 메서드:
    - group(): 매치된 문자열을 반환
    - start(): 매치의 시작 위치 반환
    - end(): 매치의 끝 위치 반환
    - span(): 매치의 (시작, 끝) 위치 튜플 반환
```python
match = re.search(r'\d+', 'abc123def')
print(match.group())   # '123'
print(match.start())   # 3
print(match.end())     # 6
print(match.span())    # (3, 6)
```

## 정규표현식 패턴

### 기본 패턴
- `.`: 모든 문자 한 개와 매치 (줄바꿈 문자 제외)
- `^`: 문자열의 시작
- `$`: 문자열의 끝
- `\`: 특수 문자를 일반 문자로 취급

### 문자 클래스
- `[abc]`: a, b, c 중 한 개의 문자와 매치
- `[a-z]`: a부터 z 사이의 모든 소문자와 매치
- `[A-Z]`: A부터 Z 사이의 모든 대문자와 매치
- `[0-9]`: 모든 숫자와 매치
- `[^abc]`: a, b, c를 제외한 모든 문자와 매치

### 미리 정의된 문자 클래스
- `\d`: 숫자와 매치 [0-9]
- `\D`: 숫자가 아닌 것과 매치 [^0-9]
- `\w`: 문자 또는 숫자와 매치 [a-zA-Z0-9_]
- `\W`: 문자 또는 숫자가 아닌 것과 매치 [^a-zA-Z0-9_]
- `\s`: 공백문자와 매치 (스페이스, 탭, 줄바꿈)
- `\S`: 공백이 아닌 문자와 매치

### 반복
- `*`: 0회 이상 반복
- `+`: 1회 이상 반복
- `?`: 0회 또는 1회 반복
- `{m}`: m회 반복
- `{m,n}`: m회부터 n회까지 반복
- `{m,}`: m회 이상 반복
- `{,n}`: n회 이하 반복

### 그룹
- `()`: 그룹화
- `(?:)`: 그룹화하지만 캡처하지 않음
- `|`: 또는 (OR 연산)

### 탐욕적/비탐욕적 패턴
- 기본적으로 탐욕적(greedy) 방식
- `*?`, `+?`, `??`: 비탐욕적(non-greedy) 방식

### 예시
```python
# 이메일 패턴
email = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'

# 전화번호 패턴 (한국)
phone = r'(\d{2,3})-?(\d{3,4})-?(\d{4})'

# URL 패턴
url = r'https?://[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}/?.*'

# 날짜 패턴 (YYYY-MM-DD)
date = r'(?:19|20)\d\d-(?:0[1-9]|1[012])-(?:0[1-9]|[12][0-9]|3[01])'

# IP 주소 패턴
ip = r'(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)'