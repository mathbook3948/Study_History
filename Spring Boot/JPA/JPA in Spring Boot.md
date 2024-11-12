# 개념
## ORM
- Java의 객체와 관계형 데이터베이스의 데이터를 자동으로 매핑(연결)해주는것을 말한다
### JPA 
- ORM의 한 종류로서 Java의 ORM 표준 문법이다(~~어렵고 복잡하다~~)
#### Hibernate
- JPA를 쓰기 편하게 구현한 라이브러리이다.
### 장점
- Java 코드로 DB와 데이터 입출력이 가능하고, 뽑은 데이터의 타입 체크가 편하다
- 데이터를 Java 스타일로 관리 가능하다
### 단점
- 데이터 입출력 속도가 느리다.
# Hibernate 라이브러리
- 여기서는 JPA와 Hibernate를 같은 뜻으로 사용할 예정이다
## 사용법
0. gradle 파일에 JPA를 추가한다
1. .properties에 datasource, JPA 설정
2. `@Entity` 클래스 만들기
3. JpaRepository를 상속받은 인터페이스 만들기
4. DB 입출력 원하는 곳에서 사용하기
### gradle 파일에 JPA를 추가한다
```gradle
implementation 'org.springframework.boot:spring-boot-starter-data-jpa'
```
### .properties에 datasource, JPA 설정
```properties
spring.sql.init.platform=데이터베이스 플랫폼
spring.datasource.driver-class-name=해당 데이터베이스 플랫폼의 JDBC 드라이버 클래스
spring.datasource.url=데이터베이스의 위치(URL)
spring.datasource.username=사용자 이름
spring.datasource.password=비밀번호
```
- 데이터베이스의 연결 정보를 설정한다
```properties
spring.jpa.properties.hibernate.show_sql=true
spring.jpa.hibernate.ddl-auto=update
```
- 기타 Hibernate 옵션을 설정한다
#### JPA 설정
##### spring.jpa.properties.hibernate.show_sql
- JPA가 실행하는 SQL 쿼리(코드)를 콘솔에 출력할지 여부를 설정하는 옵션이다
	- `true`
	- `false`
##### spring.jpa.hibernate.ddl-auto
- JPA가 데이터베이스의 구조를 관리하는 방법을 설정하는 옵션이다
	- `none` : JPA가 테이블을 관리하지 않는다
	- `update` : 기존 테이블을 업데이트 한다. 새로운 엔티티, 컬럼이 추가되면 해당 변경사항을 반영하려 자동으로 시도한다.
	- `create` : 어플리케이션이 시작할 때 테이블을 삭제한 후 테이블을 새로 생성한다
	- `create-drop` : 어플리케이션이 시작할 때 테이블을 새로 생성하고, 종료 시 테이블을 삭제한다
### `@Entity` 클래스 만들기
- `@Entity` 클래스를 만들고 실행을 하면 자동으로 데이터베이스에 해당 클래스 이름으로 테이블을 만들어준다
- `@Entity` 클래스 안에는 `@Id` 어노테이션이 붙은 변수 하나가 필수적으로 필요하고, 이 변수는 일반적으로 Sequence 또는 Auto Increment를 사용한다. SQL에서 Primary Key이다.
- `@Entity` 클래스는 VO와 비슷하게 보통 getter과 setter을 만들어 놓는다
```java
@Entity
public class EntityName {
	@Id
	@GeneratedValue(strategy = GenerationType.IDENTITY) //Auto Increment 예시
	private Long id;
}
```
### JpaRepository를 상속받은 인터페이스 만들기
- JPA 만든 사람이 이렇게 하라고 만들어 놓은 규칙. 그냥 라이브러리 사용법이다.
```java
public interface EntityNameRepository extends JpaRepository<EntityName, IdType> {

} 
```
- 이런 식의 인터페이스를 만들어주고, JpaRepository를 상속받는데, 제너릭으로 `@Entity` 클래스의 이름, `@Id` 변수의 자료형을 넣어주어야 한다
### DB 입출력 원하는 곳에서 사용하기
- 알아서 Repository를 DI 잘 받아서 메서드를 통해 사용하면 된다
```java
var result = EntityNameRepository.findAll(); 
```
- 모든 행을 가져와서 List 형태로 result 변수에 저장한다
## JpaRepository 메서드
### 입력
- `.save(EntityName entity)` : 엔티티를 저장하거나 업데이트 한다.
### 출력
- `.findById(Long/int... id)` : 매개변수에 입력된 id를 바탕으로 엔티티 1개를 찾아 반환한다
- `.findAll()` : 모든 엔티티를 조회하고 List 형태로 반환한다
- `.deleteById(Long/int... id)` : 매개변수에 입력된 id를 바탕으로 엔티티를 찾아 삭제한다.
- `.findBy<Column>(<Type> <value>)` :JPA가 자동으로 `findByColumn` 형식의 메서드를 생성하고, 매개변수로 해당컬럼의 타입과 같은 타입의 값을 받는다. 조건에 맞는 엔티티가 여러 개일경우 List 형태로 반환하고, 하나만 존재할 경우 Entity 형태로 반환한다.
- `.findOneBy<Column>(<Type> <value>)` : `findby<Column>()` 과 거의 동일하게 JPA가 자동 생성시켜주며, Optional<T> 형태로 반환한다. 만약 조회된 엔티티가 여러 개일경우 NonUniqueResultException이 발생한다.
- `.findFirstBy<Column>(<Type> <value>)` : `.findOneBy<Column>()`와 거의 동일하지만, 조회된 엔티티가 여러 개일경우 가장 첫번째 엔티티를 Optional<T> 형태로 반환한다.
## 어노테이션 //TODO 정리하기
- `@Table(name=)`
- `@SequenceGenerator(name=, sequenceName=, initialValue=, allocationSize=)`
- `@Temporal()`
- `@Column([columnDefinition=], [length=], [nullable=])` 