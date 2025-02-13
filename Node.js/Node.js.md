# **Node.js란?**
- Chrome V8 JavaScript 엔진 위에서 동작하는 **JavaScript 런타임 환경**.
- JavaScript를 브라우저뿐만 아니라 서버에서도 실행할 수 있도록 해준다.
- **이벤트 기반, 논블로킹 I/O 모델**을 사용하여 높은 성능과 확장성을 제공한다.

---

## **Node.js의 특징**
### 1. **비동기 및 논블로킹 I/O**
- Node.js는 **싱글 스레드** 기반이지만 **비동기 처리**를 통해 동시에 많은 요청을 처리할 수 있다.
- `fs.readFile()` 같은 파일 입출력도 비동기적으로 동작하여 성능을 높인다.

```js
const fs = require("fs");

fs.readFile("example.txt", "utf8", (err, data) => {
  if (err) throw err;
  console.log(data);
});

console.log("파일 읽기 요청 완료"); 
// 파일 읽기가 끝나기 전에 이 코드가 실행됨 (비동기)
```

### 2. **이벤트 기반 아키텍처**
- Node.js는 **이벤트 루프(Event Loop)**를 사용하여 **비동기 이벤트를 처리**한다.
- 이벤트 리스너를 통해 특정 이벤트가 발생할 때 자동으로 실행되도록 설정할 수 있다.

```js
const EventEmitter = require("events");
const myEmitter = new EventEmitter();

myEmitter.on("event", () => {
  console.log("이벤트 발생!");
});

myEmitter.emit("event"); // "이벤트 발생!" 출력
```

### 3. **모듈 시스템 (CommonJS)**
- Node.js는 모듈 시스템을 사용하여 코드의 재사용성을 높인다.
- `require()`와 `module.exports`를 이용해 모듈을 불러오고 내보낼 수 있다.

**모듈 정의 (`math.js`)**
```js
function add(a, b) {
  return a + b;
}

module.exports = { add };
```

**모듈 사용 (`index.js`)**
```js
const math = require("./math");
console.log(math.add(2, 3)); // 5
```

### 4. **내장 모듈 (Built-in Modules)**
- Node.js에는 파일 시스템(`fs`), HTTP(`http`), 경로(`path`) 등 다양한 내장 모듈이 제공된다.

```js
const os = require("os");

console.log("운영체제:", os.platform()); // Windows, Linux 등 출력
console.log("CPU 코어 개수:", os.cpus().length);
```

### 5. **패키지 관리자 (npm)**
- `npm`을 사용하여 다양한 라이브러리를 설치하고 관리할 수 있다.
- 예를 들어, Express 프레임워크 설치:
  ```sh
  npm install express
  ```

---

## **Node.js의 주요 활용 사례**
✅ **웹 서버 개발** → Express.js, Koa.js 사용  
✅ **REST API 서버** → JSON 데이터 제공  
✅ **실시간 애플리케이션** → WebSocket 기반 채팅, 게임  
✅ **파일 시스템 관리** → 로그 처리, 파일 업로드  
✅ **CLI 도구 개발** → npm 스크립트, 자동화 툴

---