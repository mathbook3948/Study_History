## Express 서버 시작하기

### 1. 프로젝트 설정

먼저 Express를 사용할 프로젝트 폴더를 생성하고, 그 안에서 `npm init` 명령어를 실행하여 `package.json` 파일을 생성합니다.

```bash
mkdir my-express-server
cd my-express-server
npm init -y
```

### 2. Express 설치

`npm`을 사용하여 Express를 설치합니다.

```bash
npm install express
```

### 3. 기본 서버 코드 작성

프로젝트 루트 디렉토리에 `index.js` 파일을 생성하고, 아래와 같이 Express 서버를 설정합니다.

```javascript
// index.js
const express = require('express');
const app = express();

// 기본 라우트 설정
app.get('/', (req, res) => {
  res.send('Hello, Express!');
});

// 서버 포트 설정
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
```

### 4. 서버 실행

서버를 실행하려면 `node` 명령어로 `index.js` 파일을 실행합니다.

```bash
node index.js
```

서버가 실행되면, 브라우저에서 `http://localhost:3000`을 열어 "Hello, Express!" 메시지를 확인할 수 있습니다.

### 5. 추가 설정

#### 5.1. 미들웨어 설정

미들웨어는 요청을 처리하기 전에 실행되는 함수입니다. 예를 들어, JSON 데이터를 요청 본문에서 처리할 수 있도록 하기 위해 `express.json()` 미들웨어를 사용할 수 있습니다.

```javascript
// JSON 데이터 처리 미들웨어 추가
app.use(express.json());
```

#### 5.2. 라우트 추가

Express에서는 다양한 HTTP 요청에 대해 라우트를 설정할 수 있습니다. 예를 들어, POST 요청을 처리하는 방법은 다음과 같습니다.

```javascript
// POST 요청 처리
app.post('/data', (req, res) => {
  const receivedData = req.body;
  res.json({ message: 'Data received successfully', data: receivedData });
});
```

### 6. 서버 종료

서버를 종료하려면 터미널에서 `Ctrl + C`를 눌러서 서버를 중지할 수 있습니다.
