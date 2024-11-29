# Redux란?
- state(변수)들을 한 파일을 만들어서 그 파일에서 Component들이 변수를 가져다 쓸 수 있게 해주는 라이브러리
## 그래서 왜 쓰는데
1. Component간 값(데이터)들을 Props 없이 꺼내 쓸 수 있음
2. 상태(state)를 관리하기 용이하다 : 수정 방법을 미리 지정해서 오류를 방지 할 수 있음

# 사용 방법
0. 설치
1. slice 정의
2. store 설정
3. index.tsx 설정
4. Component에서 사용
## 설치
```shell
yarn add redux react-redux redux-thunk
yarn add @reduxjs/toolkit
yarn add -D @types/react-redux
```
## slice 정의
- slice란 하나의 변수를 설정한 문서 라고 생각하면 편하다

**counterSlice.ts**
```typescript
export interface CounterState { //interface 이름 알아서 지정
  변수1: number; // 값도 원하는 만큼
}

const initialState: CounterState = { // 설정한 interface로 자료형 설정
  변수1: 0 // 초기 값 설정
};

// slice 이름도 알아서
const counterSlice = createSlice({//redux의 createSlice 함수로 slice 생성
  name: 'counter',
  initialState, //초기값, 자료형 지정
  reducers: {
    /*
    reducers는 값을 어떻게 변경할지 지정하는 함수이다.
    값을 함부로 변경 못하게 막아서 유지보수를 쉽게 해준다
    */
    increment: (state) => { 
        /*
        state는 그냥 변수 이름이다. 원하면 바꿔도 된다. 
        state에는 자동으로 최근 값이 들어간다
        */
      state.value += 1;
    },
    /*
    객체 처럼 key : value를 하는데, 단, value는 arrow 함수로 넣는게 좋을듯
    */
    decrement: (state) => { //몇 개든 만들 수 있다.
      state.value -= 1;
    },
    /*
    PayloadAction : Redux에서 지정한 interface
    ```
    interface PayloadAction<P = void> {
        type: string;
        payload: P; // payload의 타입을 제네릭으로 지정해서 원하는 값을 받을 수 있다
    }
    ```
    payload가 매개변수 같은 느낌
    */
    incrementByAmount: (state, action: PayloadAction<number>) => {
      state.value += action.payload;
    },
  },
});

//다른 곳에서도 쓸 수 있게 내보낸다 
export const { increment, decrement, incrementByAmount } = counterSlice.actions; 
export default counterSlice.reducer;
```

## store 설정
**index.ts**
```typescript
export const store = configureStore({
  reducer: {
    counter: counterReducer, 
    /*
    counterSlice를 counterReducer라는 이름으로 불러옴(관습)
    여러개의 reducer를 불러와도 된다.
    */
  },
});

/*
store.getState : reducer 안에 있는 slice들의 현재 상태(값)를 가져와서 반환
ReturnType : 주어진 함수의 반환 타입을 추출하고 반환한다
RootState : 상태(값)을 읽을 때 자료형을 지정하기 위해 사용한다
*/
export type RootState = ReturnType<typeof store.getState>; 

/*
store.dispatch : store의 action을 dispatch 하는 함수
AppDispatch : store.dispatch 함수의 자료형을 추출한 것. 자료형의 안정성을 보장하려고 사용
*dispatch : 상태(값)을 변경하기 위해 action(함수)을 store에 전달하는 함수.
=> Redux store에 무언가 하라고 요청하는 방법
*/
export type AppDispatch = typeof store.dispatch;
```

## index.tsx 설정
**index.tsx**
```tsx
const root = ReactDOM.createRoot(document.getElementById('root')!);

root.render(
    //Provider로 <App/>을 감싼다
  <Provider store={store}> 
    <App />
  </Provider>
);
```

## Component에서 사용
```tsx
const App: React.FC = () => {
    //useSelector : Redux의 store에서 상태(값)을 읽기 위해 사용되는 훅(hook)
    //state : RootState 자료형으로 자동으로 state를 넣는다
    //state.counter.value 처럼 값을 지정 해놓으면 useState처럼 값이 변경될 때마다 자동으로 리렌더링 된다
  const count = useSelector((state: RootState) => state.counter.value);
  //action(상태를 변경하는 함수)을 받으면 실행한다
  const dispatch = useDispatch<AppDispatch>();

  return (
    <div>
      <h1>Count: {count}</h1>
      <button onClick={() => dispatch(increment())}>
      증가
      </button>
      <button onClick={() => dispatch(decrement())}>
      감소
      </button>
      <button onClick={() => dispatch(incrementByAmount(5))}>
      +5
      </button>
    </div>
  );
};

export default App;
```