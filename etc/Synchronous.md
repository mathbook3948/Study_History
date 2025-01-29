# 비동기(Asynchronous)란?
- 코드가 순차적으로 실행되지 않고, 특정 작업이 완료될 때까지 기다리지 않고 다음 코드를 실행하는 방식
## 동기(Synchronous) VS 비동기(Asynchronous)
1. 동기
- 하나의 작업이 끝날 때까지 다음 코드가 실행되지 않음
- 실행 순서가 보장됨
- 단점 : 시간이 오래 걸리는 작업이 있을 경우 전체 프로그램이 멈춤(Blocking)
2. 비동기
- 특정 작업(예: 데이터 요청)이 끝날 때까지 기다리지 않고 다음 코드가 먼저 실행됨
- 시간이 오래 걸리는 작업(예: API 호출, 파일 읽기)을 할 때 유용
- 콜백, Promise, async/await 같은 기법을 사용
### 비동기 처리 방식
#### 1. 콜백 함수(Callback)
```js
function fetchData(callback) {
  setTimeout(() => {
    callback("데이터 받아옴");
  }, 2000);
}

console.log("1. 요청 시작");
fetchData((data) => {
  console.log("2. 응답 도착:", data);
});
console.log("3. 다음 작업 실행");
```
```
1. 요청 시작
3. 다음 작업 실행
(2초 후)
2. 응답 도착: 데이터 받아옴

```
#### 2. Promise
```js
function fetchData() {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      resolve("데이터 받아옴");
    }, 2000);
  });
}

console.log("1. 요청 시작");
fetchData().then((data) => {
  console.log("2. 응답 도착:", data);
});
console.log("3. 다음 작업 실행");
```
```
1. 요청 시작
(2초 후)
2. 응답 도착: 데이터 받아옴
3. 다음 작업 실행
```
#### 3. async/await
```js
function fetchData() {
  return new Promise((resolve) => {
    setTimeout(() => {
      resolve("데이터 받아옴");
    }, 2000);
  });
}

async function fetchAndDisplay() {
  console.log("1. 요청 시작");
  const data = await fetchData(); // 2초 기다림
  console.log("2. 응답 도착:", data);
  console.log("3. 다음 작업 실행");
}

fetchAndDisplay();
```
```
1. 요청 시작
(2초 후)
2. 응답 도착: 데이터 받아옴
3. 다음 작업 실행
```
## 3. 비동기 처리가 중요한 이유
- 서버에서 데이터를 가져오거나, 파일을 읽는 등의 작업은 시간이 오래 걸릴 수 있음
- 동기 처리를 하면 프로그램이 멈추지만, 비동기 처리를 하면 다른 작업을 먼저 수행할 수 있음
- 예: 웹사이트에서 데이터를 불러오는 동안 사용자가 UI를 조작할 수 있도록 하기 위해 사용
