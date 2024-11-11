## 기본적인 개념, 구성요소
### Bean
- Spring IoC 컨테이너가 관리하는 객체를 의미한다.
- 싱글톤 패턴으로 객체를 자동으로 생성해준다
##### 생성 방법
- `@Service`, `@RestController`등의 어노테이션을 사용하여 Bean을 생성한다.
### 의존성 주입(Dependency Injection)
- 한 클래스에서 다른 클래스를 참조하려 할 때 자동으로 의존성을 주입해주는 것이다.
#### 개념
##### 의존성
- 한 클래스가 다른 클래스의 기능을 사용하기 위해 해당 클래스의 인스턴스나 참조를 필요로 하는 상태를 말한다. 예를 들어, A 클래스가 B 클래스의 메서드를 호출하려면 B 클래스의 인스턴스가 필요하다. 이때 A 클래스는 B 클래스에 의존하게 된다.
##### 결합도
- 두 개 이상의 클래스의 의존 관계를 나타내는 개념이다. 결합도가 높다는 뜻은 의존이 너무 많은 것이다. 결합도가 높으면 유지 보수가 어려워지고, 재사용성이 떨어지고, 특정 클래스만 독립적으로 테스트 하기가 힘들어진다. 반면, 결합도가 낮으면 각 클래스가 독립적으로 동작할 수 있어 유지 보수와 테스트가 용이해진다.
#### 의존성 주입의 장점
- 유지 보수성 향상: 의존성 주입을 통해 클래스 간의 결합도를 낮출 수 있어, 코드 변경 시 다른 클래스에 미치는 영향을 최소화할 수 있다.
- 테스트 용이성: 한 클래스의 독립적인 테스트가 쉬워진다.
- 재사용성 증가: 의존성이 명확하게 정의되므로, 특정 클래스의 재사용이 쉬워진다.
#### 의존성 주입의 방법
##### ByName
- Bean의 이름으로 기반으로 DI 하는 방법이다.
- Bean의 이름은 기본적으로 클래스명의 첫글자를 소문자로 만든 것이다.
---
```java
@Resource
private ExampleClass exampleClass;
```
- `ExampleClass`의 기본 Bean 이름은 `exampleClass`이기 때문에 이름을 찾아서 자동으로 의존성을 주입해준다.
##### ByType
- Bean의 자료형(타입)을 기반으로 DI 하는 방법이다.
- 같은 자료형(타입)을 가지는 Bean이 여러개 있을 경우 오류가 발생한다.
---
```java
@Autowired
private ExampleClass testClass;
```
- 이 경우 `testClass`로 이름을 설정 했고, `ExampleClass`의 Bean 명을 따로 지정해주지 않아서 기본 이름을 찾으려 했으나, 같은 이름이 없어서 ByType으로 찾아서 DI 한다.
#### 의존성 주입의 원리
### Spring MVC
- Spring MVC는 Spring Model-View-Controller의 약자로, 기능별로 코드를 분리시켜서 유지보수를 용이하게 할 수있게 하는 목적으로 사용된다.
#### 개념
1. 외부에서 요청이 들어옴
2. DispatcherServlet이 HandlerMapping을 통해 일치하는 Controller를 찾아 반환
3. 해당 Controller에게 처리를 요청
4. Controller에서 비즈니스 로직을 처리한 후 ModelAndView 반환
5. DispatcherServlet에서 ModelAndView를 분석하고 해당 View 정보를 ViewResolver에게 넘김
6. ViewResolver는 View 정보를 받아 View를 DispatcherServlet에게 전달
7. DispatcherServlet이 View를 렌더링 후 Response로 클라이언트에게 보냄

//TODO
## Annotation(어노테이션)
### DI  관련
- `@Autowired` : Spring이 관리하는 Bean을 자동으로 주입한다. ByType을 기본으로 DI를 진행한다.
- `@Resource` : Bean의 이름을 기준으로 DI 한다. `@Qualifier`을 통해 Bean의 이름을 명시하지 않을경우 기본 이름을 찾는다. 
- `@Qualifier(String BeanName)` : Bean을 만들때, 또는 Bean을 찾을 때 이 어노테이션이 있다면, 특정 이름의 Bean을 생성, 주입할 수 있다.
### Controller 관련
- `@RestController` : 요청을 받아서 JSON, XML 형식으로 데이터를 반환하는 서비스를 만들 때 사용하고, `@Controller`과 `@ResponseBody`를 결합한 것으로 볼 수 있다. `@ResponseBody`를 명시하지 않아도 자동으로 JSON 또는 XML로 변환하여 데이터를 반환한다.
- `@Controller` : 요청을 받아서 View를 반환하는 서비스를 만들 때 사용한다. 
- `@ResponseBody` : 메서드의 반환 값을 JSON 또는 XML로 변환하여 HTTP Response Body에 내용을 작성하게 한다. 일반적으로 `@Controller`가 적용된 클래스에서 사용된다
- `@RequestMapping`
- `@GetMapping`
- `@PostMapping`
- `@PutMapping`
- `@DeleteMapping`
### Service 관련
//TODO