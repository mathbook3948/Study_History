# React 란?
- 컴포넌트를 이용하고 조합해서 사용자 인터페이스를 만들 수 있는 **JavaScript 라이브러리**. 
- **컴포넌트란** 화면의 한 부분을 담당하는 독립적이고 재사용 가능한 코드 조각이다.

## React의 특징
- 데이터가 바뀌어 리렌더링이 필요할 때, 이를 효율적이고 간단하게 수행할 수 있도록 도와준다.
- Virtual DOM을 사용하여 변경된 부분만 실제 DOM에 반영함으로써 **효율적인 렌더링**을 제공한다.
  - 데이터가 변경되면 Virtual DOM이 변경 사항을 비교하고, **변경된 부분만 실제 DOM에 적용** 한다.
- React는 기본적으로 Client-Side Rendering(CSR)을 지원하여 서버의 부담을 줄일 수 있다.
### DOM과 Virtual DOM?
- HTML을 컴퓨터가 이해할 수 있게 만들어둔 구조.
```
HTML -> DOM -> 렌더링
```
- 이 과정을 통해 사용자에게 보여지게 된다.
```
HTML -> Virtual DOM->기존 Virtual DOM과 비교 -> 달라진 부분만 렌더링
```
- 하지만 Virtual DOM을 사용한 React는 기존 Virtual DOM과 비교하여 바뀐 부분만 다시 렌더링하여 효율적으로 화면을 업데이트 할 수 있다


# 아직 정리 안된 부분
jsx 안에 html을 넣기
- dangerouslySetInnerHTML

Component를 감싸는 Container 만들기
```tsx
interface Props {
    children: ReactNode; // ReactNode 타입 : React 요소, number, string, 기타 모든 자료형을 나타내는 자료형. 자바에서 Object 하고 비슷한 느낌
  }

const ExampleComp: React.FC<Props> = ({ children }) => { // children에는 ExampleComp로 감싼 요소가 자동으로 들어간다.

  return true ? <>{children}</> : <div>접근 권한이 없습니다.</div>;
  // 조건을 줘서 특정 조건에만 화면 보이게 구성 가능
};

export default ExampleComp;
```