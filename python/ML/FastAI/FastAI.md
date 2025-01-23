# FastAI 란?
- 딥러닝을 쉽게 구현할 수 있도록 PyTorch 기반으로 만들어진 고수준 라이브러리
- 적은 코드로 최신 딥러닝 기술들을 구현할 수 있게 해줌

# FastAI 메인
## 데이터 불러오기 및 전처리
### TabularDataLoaders
- 표 데이터(csv...)등을 로드 및 자동 전처리 하는 클래스이다
```python
from fastai.tabular.all import *
```
#### .from_df()
- DataFrame에서 TabularDataLoaders 객체를 생성한다
```python
dls = TabularDataLoaders.from_df(
    df,                            # pandas DataFrame
    path='.',                      # 데이터 저장 경로
    procs=[Categorify, FillMissing],  # 전처리 과정
    cat_names=cat_names,           # 범주형 변수명(카테고리)
    cont_names=cont_names,         # 연속형 변수명(숫자)
    y_names='target',             # 타겟 변수명(예측 원하는거)
    bs=64                         # 배치 크기
)
```
#### .from_csv()
- csv에서 직접 불러와 TabularDataLoaders 객체를 생성한다
```python
dls = TabularDataLoaders.from_csv(
    'path/to/file.csv',           # CSV 파일 경로
    path='.',                     # 데이터 저장 경로
    procs=[Categorify, FillMissing],
    cat_names=cat_names,          # 범주형 변수명(카테고리)
    cont_names=cont_names,        # 연속형 변수명(숫자)
    y_names='target',
    bs=64,
    delimiter=',',               # CSV 구분자 (기본값: ',')
    encoding='utf-8',           # 파일 인코딩
    header='infer',             # 헤더 행 지정
    na_values=['NA', ''],       # 결측치로 처리할 값들
)
```
#### Splits(데이터 분할)
- 모든 TabularDataLoaders의 불러오는 메서드는 `splits` 매개변수를 가지고 있다.
##### RandomSplitter
```python
splits = RandomSplitter(valid_pct=0.2)(range_of(df))
```
## 학습
### Loss_Func
#### 기본 분류
- CrossEntropyLossFlat      # 기본 분류 문제용
- FocalLossFlat            # 클래스 불균형 데이터용
- BCEWithLogitsLossFlat    # 이진 분류용 (시그모이드 포함)
- BCELossFlat             # 이진 분류용 (시그모이드 미포함)
- LabelSmoothingCrossEntropy  # 레이블 스무딩 적용된 분류용
#### 회귀
- MSELossFlat   # 평균 제곱 오차
- L1LossFlat    # 절대값 오차
### TabularLearner
- 표 형식 데이터를 학습하기 위한 모델을 생성하는 클래스이다
```python
learn = tabular_learner(
    dls,                          # TabularDataLoaders 객체
    layers=[200,100],             # 은닉층 구성
    metrics=accuracy              # 평가 지표
)
```
- 주요 매개변수
  - layers: 은닉층의 뉴런 수를 지정하는 리스트 (기본값: [200,100])
  - emb_szs: 임베딩 크기 딕셔너리 (기본값: None)
  - metrics: 평가 지표 (기본값: None)
  - loss_func: 손실 함수
  - opt_func: 최적화 함수 (기본값: Adam)
  - ps: 드롭아웃 비율 (기본값: None)
  - config: 모델 설정 (기본값: None)
#### metrics
- accuracy : 모델의 성능을 측정하는 값
- mse : 평균 제곱 오차
- rmse : 평균 제곱근 오차
#### 학습 관련 메서드
#### fit
```python
learn.fit(
    n_epoch=10,
    lr=1e-3,
    wd=0.01 
)
```
- wd : L2 규제의 강도 설정