# Zustand 란?
- 상태(값)를 여러 컴포넌트에서 사용할 수 있게 해주는 상태 관리 라이브러리
- Redux와 비슷하지만, 훨씬 더 간단한 API를 제공 (Redux Github Star수 60k, Zustand Github Star수 48k)
- TypeScript로 작성되어 타입 안정성이 뛰어남

# 사용 방법
1. 설치
2. store 설정
3. Component에서 사용

## 설치
```bash
# npm 사용시
npm install zustand

# yarn 사용시
yarn add zustand
```

## store.ts 설정 (최신 버전)
```typescript
import { create } from 'zustand'

// 상태의 타입 정의
type State = {
  count: number
  increase: (by: number) => void
  decrease: (by: number) => void
}

// create 함수를 사용하여 store 생성
export const useStore = create<State>()((set) => ({
  // 초기 상태
  count: 0,
  
  // 액션
  increase: (by) => set((state) => ({ 
    count: state.count + by 
  })),
  
  decrease: (by) => set((state) => ({ 
    count: state.count - by 
  })),
}))

// 컴포넌트에서 사용 예시
import { useStore } from './store'

function Counter() {
  const { count, increase, decrease } = useStore()

  return (
    <div>
      <h1>{count}</h1>
      <button onClick={() => increase(1)}>Increase</button>
      <button onClick={() => decrease(1)}>Decrease</button>
    </div>
  )
}
```

주요 변경사항:
1. `interface` 대신 `type` 사용 (선호도에 따라 선택)
2. create 함수의 import 방식 변경
3. 상태와 액션을 더 명확하게 구분
4. TypeScript의 타입 추론 활용

### 추가 기능 예시

```typescript
// 여러 상태 결합하기
type State = {
  count: number
  text: string
  updateText: (text: string) => void
  reset: () => void
}

export const useStore = create<State>()((set) => ({
  count: 0,
  text: '',
  
  updateText: (text) => set({ text }),
  reset: () => set({ count: 0, text: '' }),
}))

// 상태 구독하기 (성능 최적화)
const count = useStore((state) => state.count)
```

### 미들웨어 사용 예시

```typescript
import { create } from 'zustand'
import { persist } from 'zustand/middleware'

export const useStore = create(
    persist<State>(
        (set) => ({
            count: 0,
            increase: (by) => set((state) => ({ count: state.count + by })),
        }),
        {
            name: 'counter-storage', // localStorage에 저장될 키 이름
        }
    )
)
```