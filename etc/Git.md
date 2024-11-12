# Git이란?
- 코드들을 기록, 보관 하려고 사용한다(버전관리)
- 과거 코드를 보거나, 과거 코드로 돌아갈 수 있다
# 설정
## 설치 하자마자
```shell
git --version #버전 확인 부터
git config --global user.email "본인이메일" #전역 변수로 이메일 설정
git config --global user.name "이름" #전역 변수로 이름(닉네임) 설정
```
# Git 메인
```shell
git init
```
- 먼저 Git을 시작하려면 폴더를 만들고 `git init`을 입력하여 작업 폴더를 세팅한다
## 저장(기록) 관련
### 파일을 저장(기록) 해놓으려면
```shell
git add 파일명
git commit -m "메모"
```
#### Q : 굳이 두 단계로 나눈 이유는?
- A : 꼭 필요한 파일만 기록을 하려고. 예를 들어 사진같은 파일은 기록을 할 필요가 잘 없음.

#### 한 폴더에 저장(기록)할 파일이 너무 많다면
```shell
git add .
git commit -m "메모"
```
- 작업폴더 내 모든 파일을 저장(기록) 해준다.

## branch
- 현재의 commit 상태를 복사한 새로운 commit을 만드는 것
- 현재의 commit에 영향을 주지 않고 독립적이고, 병렬적으로 작업을 가능하게 해준다
![pepe_branch](https://github.com/user-attachments/assets/6b5c616c-671b-4b73-b7e6-585271808ed9)

### branch 생성
```shell
git branch branch_name
```
### branch로 이동
```shell 
git switch branch_name
```
### branch merge
- branch에서 정상적으로 동작해서 다른곳(main...)에 합치고 싶을 때 사용하는 명령어
```shell
git merge branchB #branchA(main branch등..)에 합칠 때 branchB => branchA
```
- 어느 branch에 합칠지(어느 branch가 살아남을지) 잘 생각해야 한다
#### CONFLICT
- 같은 부분을 두곳 모두에서 수정 했을 때 충돌 문제가 생긴다.
##### Visual Studio Code의 경우
- 자동 병합을 실패하면 다른 부분을 띄워주는데, 그 부분을 모두 고치고 다시 commit 하면 된다
<!-- ------------------------------------------------ -->

## 기록 확인 관련
### 현재 `git add` 확인
```shell
git status
```
- 현재 스테이징된 파일(`git add` 한 파일)을 보여준다
```shell
git log --all --oneline [--graph]
```
- commit과 함께 작성한 메모와 해당 commit의 id를 보여준다
- `--graph` 옵션을 줄 경우 모든 branch의 commit 그래프와 commit id를 보여준다

### 최근 commit과 차이점 보기
```shell
git diff
```
- 실행시 가장 최근 commit과 차이점을 분석해서 보여준다
- `j`,`k` 키로 스크롤 할 수 있고, `q` 키로 나갈 수 있다.

~~쓸모없다~~
#### 쓸모 있는 버전
```shell
git difftool [commit_id]
git difftool [commit_id1] [commit_id2]
```
- 차이점을 보여주는 vim 에디터를 띄워준다
- commit id를 명시해주면 해당 커밋과 현재 파일을 비교해준다
- commit_id를 2개 명시한다면 선택한 커밋들을 비교해준다

~~사실 이거도 쓸모없음~~

사실 VSC에서 Git extension 아무거나 깔아도 이거보단 낫다
