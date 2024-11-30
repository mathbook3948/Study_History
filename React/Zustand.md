# Zustand 란?
- 상태(값)를 여러 컴포넌트에서 사용할 수 있게 해주는 라이브러리
- Redux와 비슷하지만, 훨씬 더 쉽다(Redux Github Star수 60k, Zustand Github Star수 48k)
# 사용 방법
0. 설치
1. store 설정
2. Component에서 사용
## 설치 
```shell
yarn add zustand
```
## store.ts 설정
```ts
interface Counter { // interface를 만든다. 이름은 자유롭게
    count : number; // 상태(값)는 몇 개든 알아서 추가하기
    // 상태를 변경하고 싶다면 자료형에 arrow 함수를 넣어주면 된다
    increase : (by : number) => void; // 예시 : 자료형이 number인 값 by를 받고, 반환형이 void인 함수가 들어가야 한다.
}

/*
Zustand 라이브러리의 create 함수를 이용하여 상태 관리자를 만들 수 있다.
제네릭으로 자료형을 지정해주어야 하고, 두번째 호출에서 매개변수로
*/
const useStore = create <Counter>()((set) => ({
    count : 0, // 상태(값)의 초기화를 여기서 진행한다
    increase : (by : number) => set((state) => ({count : state.count + by}))
}))
```