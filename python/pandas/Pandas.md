# Pandas란?
## Pandas 메인
```python
import pandas as pd
```
### Series 클래스
- 한 열을 표현하는 클래스
```
# 생성자 매개변수
data => 실제 데이터. 리스트, 딕셔너리, numpy 배열 등이 올 수 있다
index => 데이터의 커스텀 인덱스(라벨)를 지정 
dtype : Dtype => 데이터의 타입(자료형)을 지정한다. int64, float64, object 등을 지정 가능하다
name => 해당 객체의 이름을 지정한다. DataFrame 객체에서 열 이름으로 사용된다
copy => //TODO
fastpath => Deprecated. pandas 2.0.0 버전부터 제거될 예정
```
#### 주요 메서드
##### .head() .tail()
- 데이터 앞 또는 뒷부분과 dtype을 보여준다
```python
s = Series(np.random.randn(500))
s.head()
s.tail()
"""
0   -0.487862
1   -0.142409
2    0.444524
3    1.276300
4   -0.509550
dtype: float64
495    0.833564
496   -1.098467
497   -0.041700
498    0.458014
499    1.726630
dtype: float64
"""
```
##### .describe()
- 각종 통계를 보여준다
```python
s = Series(np.random.randn(500))
print(s.describe())
"""
count    500.000000 => 데이터의 갯수
mean       0.027296 => 평균
std        1.011907 => 표준편차
min       -2.992704 => 최솟값
25%       -0.686816
50%        0.028757 => 중간값
75%        0.698366
max        2.820692 => 최댓값
dtype: float64
"""
```
- `.count()`, `.mean()`, `.std()`... 처럼 개별로도 가능하다
##### .info()
- 현재 객체의 정보를 출력(print) 해준다
```python
s = Series(np.random.randn(500))
print(s.info())

"""
<class 'pandas.core.series.Series'> => 객체 타입
RangeIndex: 500 entries, 0 to 499 => 인덱스의 항목 수
Series name: None => Series의 이름(이 경우는 지정 안함)
Non-Null Count  Dtype  => Null(None)이 아닌 값 갯수, 그 값의 타입
--------------  -----  
500 non-null    float64
dtypes: float64(1) => float64 1개의 타입으로만 구성됨
memory usage: 4.0 KB => 차지하는 메모리 크기
None
"""
```
##### .unique()
- 데이터의 중복을 제거하고 고유한 값들만 numpy 배열로 반환한다
##### .to_() 시리즈
- `.to_numpy()`
- `.to_list()`
- `.to_dict()`
- `.to_frame()`
- `.to_string()`
- `.to_excel(filepath)` : filepath 경로, 이름으로 xlsx 확장자로 반환한다
```python
s = pd.Series([1, 2, 3])
s.to_excel('output.xlsx')
```
##### .grouby()
### DataFrameGroupBy 클래스
- DataFrame을 특정 기준으로 그룹화하여 집계/분석하는 클래스
- `DataFrame.groupby()` 메서드 호출 시 반환되는 클래스
#### 주요 메서드
