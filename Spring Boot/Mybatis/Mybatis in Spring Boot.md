## Mybatis란?
- 자바 기반의 데이터베이스 접근 프레임워크. 이때, 프레임워크란 소프트웨어 개발을 위한 기본 구조나 틀을 제공하는 플랫폼. 반복적인 작업을 크게 줄여준다.
- JDBC를 통하여 SQL 쿼리(코드)를 실행하고, 결과를 자바 객체로 변환하는 기능을 제공한다.

## 사용 방법
0. application.properties에 데이터베이스 연결 정보를 설정한다. 초기에 한번만 설정하면 된다.
1. Mapper을 작성한다. Mapper은 SQL 쿼리(코드)와 자바 객체 간의 매핑(연결)을 정의하는 인터페이스, 또는 XML파일을 의미한다. 
2. Service 클래스를 통해 Mapper 인터페이스에서 추상 메서드들을 준비하고, Controller에서 사용할 수 있게 준비한다.
3. Controller에서 요청이 왔을 때 해당 메서드를 Service 클래스에서 불러와서 SQL 쿼리(코드)를 실행과 처리 후 결과를 반환한다.
### 0. application.properties 설정
- 먼저, Spring에서 config.xml에서 설정했던 typeAlias 설정을 해주어야 한다. typeAlias 설정은 VO(DTO)의 이름을 짧게 바꾸어 주어서 Mappe XML을 작성 할 때 간편하게 작성 할 수 있다.
- 패키지(폴더)를 값으로 받기 때문에 값으로 VO(DTO)폴더를 설정해준다면 해당 폴더 안에 있는 `@Alias` 어노테이션을 인식해서 Alias를 자동으로 해준다.
```properties
mybatis.type-aliases-package=해당 VO(DTO)폴더의 위치
```
---
- Mapper XML 파일의 위치를 설정한다. Mybatis에서 XML 파일의 경로를 설정 할 때에는 `classpath:` 접두사를 무조건 사용해야 한다. 
- `/*.xml`을 통해서 해당 폴더 내의 모든 XML 파일을 Mapper로 설정 할 수 있다.
``` properties
mybatis.mapper-locations=classpath:Mapper XML의 폴더 또는 파일 경로
```
---
- 데이터베이스의 연결 정보를 설정한다. 
```properties
spring.sql.init.platform=데이터베이스 플랫폼
spring.datasource.driver-class-name=해당 데이터베이스 플랫폼의 JDBC 드라이버 클래스
spring.datasource.url=현재 데이터베이스의 위치(URL)
spring.datasource.username=사용자 이름
spring.datasource.password=비밀번호
```
#### spring.sql.init.platform
- 사용할 데이터베이스 플랫폼을 설정한다.
---
- oracle
#### spring.datasource.driver-class-name
- spring.sql.init.platform에서 설정한 플랫폼에 맞는 드라이버 클래스를 가져온다.
---
- oracle : `oracle.jdbc.driver.OracleDriver`
#### spring.datasource.url
- 데이터베이스의 위치(URL)과 연결 방법을 정의한다.
##### 예시
- oracle : `jdbc:oracle:thin:@localhost:1521:xe`
	xe : Oracle 데이터베이스의 Express Edition을 나타내며, 무료 버전(개발 및 학습 목적)으로 사용 되는 데이터베이스임을 나타낸다.
### 1-1. Mapper XML 작성법
- 먼저 상단에 Mapper XML임을 나타내는 코드를 적어주어야 한다. 
```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE mapper
  PUBLIC "-//mybatis.org//DTD Mapper 3.0//EN"
  "https://mybatis.org/dtd/mybatis-3-mapper.dtd">
```
---
- 최상단에 `<mapper>` 태그가 있어야 한다. `<mapper>` 태그는 `namespace` 속성을 가져야 하며, 연결될 Mapper 인터페이스의 경로로 설정해야 한다.
```xml
<mapper namespace="Dao의 경로">
	//SQL 쿼리(코드)
</mapper>
```
---
- `<mapper>` 태그 안에 SQL 쿼리(코드)들을 설정 해놓을 수 있다. 
#### SQL 쿼리 태그 종류
##### `<select>`
- `id` : 이 SQL 쿼리(코드)를 호출할 때 사용할 고유 식별자이다. Mapper 인터페이스의 추상 메서드의 이름과 동일해야 한다.
- `parameterType` : SQL 쿼리에 전달될 파라미터(입력값)를 지정한다. VO(DTO), String, int, Map 등에서 같은 이름(키)를 찾아서 값을 SQL 쿼리에 전달해준다. 클래스 이름 또는 Alias된 이름을 사용할 수 있다.
- `resultType` : 결과로 반환될 자료형(타입)을 지정한다. VO(DTO), Map, int 등으로 반환 받을 수 있다. Map의 경우 `Map<String, Object>`으로 반환된다. 클래스 이름 또는 Alias된 이름을 사용할 수 있다.
##### `<insert>` 
- `id` : 이 SQL 쿼리(코드)를 호출할 때 사용할 고유 식별자이다. Mapper 인터페이스의 추상 메서드의 이름과 동일해야 한다.
- `parameterType` : SQL 쿼리에 전달될 파라미터(입력값)를 지정한다. VO(DTO), String, int, Map 등에서 같은 이름(키)를 찾아서 값을 SQL 쿼리에 전달해준다. 클래스 이름 또는 Alias된 이름을 사용할 수 있다.
##### `<update>`
- `id` : 이 SQL 쿼리(코드)를 호출할 때 사용할 고유 식별자이다. Mapper 인터페이스의 추상 메서드의 이름과 동일해야 한다.
- `parameterType` : SQL 쿼리에 전달될 파라미터(입력값)를 지정한다. VO(DTO), String, int, Map 등에서 같은 이름(키)를 찾아서 값을 SQL 쿼리에 전달해준다. 클래스 이름 또는 Alias된 이름을 사용할 수 있다.
##### `<delete>`
 - `id` : 이 SQL 쿼리(코드)를 호출할 때 사용할 고유 식별자이다. Mapper 인터페이스의 추상 메서드의 이름과 동일해야 한다.
- `parameterType` : SQL 쿼리에 전달될 파라미터(입력값)를 지정한다. VO(DTO), String, int, Map 등에서 같은 이름(키)를 찾아서 값을 SQL 쿼리에 전달해준다. 클래스 이름 또는 Alias된 이름을 사용할 수 있다.
##### `<selectKey>`
- `<insert>`문에서 주로 쓰이며, 데이터에서 자동 생성된 Key(Sequence등..)를 가져와서 사용 할 수 있게 도와준다.
###### 예제
```xml
<insert id="addUser" parameterType="UserVO">
    <selectKey keyProperty="id" resultType="int" order="BEFORE">
        SELECT users_seq.NEXTVAL FROM dual
    </selectKey>
    INSERT INTO users (id, name, email) VALUES (#{id}, #{name}, #{email})
</insert>
```
---
- `keyProperty` : 값을 저장할 객체의 속성 이름을 지정한다. 여러개의 속성을 받으면 쉼표로 구분한다.
- `resultType` : 반환되는 값의 자료형(타입)을 지정한다.
- `order` : SQL 쿼리가 시작되기 전에 실행될지 후에 실행될지 설정한다. `BEFORE`, `AFTER`로 지정할 수 있다.
##### `<foreach`>`
- Collection 이나 배열 데이터들을 처리하기 위해 사용한다. 
###### 예제
```xml

<insert id="addImg" parameterType="java.util.List">
	<selectKey keyProperty="id" resultType="int" order="BEFORE">
			SELECT GALLERY_SEQ.CURRVAL FROM DUAL
		</selectKey>
	<foreach collection="list" item="image" separator=" " open="INSERT ALL" close="SELECT * FROM dual">
			INTO galleryImages(galleryId, imageName) VALUES(#{id},#{image.imagename})
	</foreach>
</insert>
```
---
- `collection` : 반복할 Collection이나 배열의 종류를 지정한다. `list`, `set`, `array` 등이 들어갈 수 있다.
- `item` : 반복시 사용할 변수의 이름을 지정한다. Collection 또는 배열의 요소들이 이 이름으로 참조된다.
- `open` : 반복 구문의 시작 부분에 삽입할 문자열을 지정한다. 
- `close` : 반복 구문의 끝 부분에 삽입할 문자열을 지정한다.
- `seperator` : 각 반복 구문 사이에 삽입할 문자열을 지정한다.
### 1-2. Mapper 인터페이스 작성법
- Mapper XML에서 지정한 위치에 위치해야하고, 파일명이 지정한것과 같아야 한다.
- Mapper XML에서 지정한 SQL 쿼리의 수, 각각  `id` 속성, 반환형, 매개변수가 같은 추상 메서드가 있어야 한다.
- `@Mapper` 어노테이션을 클래스 위에 명시해야 한다
##### 예제
###### Mapper XML
```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE mapper
  PUBLIC "-//mybatis.org//DTD Mapper 3.0//EN"
  "https://mybatis.org/dtd/mybatis-3-mapper.dtd">
<mapper namespace="kr.co.ictedu.myictstudy.dao.UserDao">
	<insert id="addUser" parameterType="UserVO">
		INSERT INTO users VALUES(users_seq.NEXTVAL, #{name}, #{age})
	</insert>
	<select id="userDetail" parameterType="int" resultType="UserVO">
		SELECT * FROM users WHERE num=#{num}
	</select>
</mapper>
```
###### Mapper 인터페이스
```java
package kr.co.ictedu.myictstudy.dao;

@Mapper //@Mapper 어노테이션이 필수이다
public class UserDao {
	void addUser();//id와 같은 이름을 가져야한다
	UserVO userDetail(int num);//모든 SQL 쿼리문과 같은 갯수의 추상 메서드가 필요하다
}
```
- `@Select()`, `@Insert()` 등 Dao에서 괄호 안에 직접 SQL쿼리를 써서 지정할 수도 있다
### 2. Service 클래스 만들기
- `@Service` 어노테이션을 클래스 위에 명시해야한다.
- Mapper 인터페이스(Dao)를 `@Autowired` 받아서 사용한다.
#### 예제
```java
public class UserService {
	@Autowired 
	private UserDao userDao;

	public void addUser(UserVO vo) {
		//비즈니스 로직
		userDao.addUser(vo);
	}
	public UserVO userDetail(int num) {
		//비즈니스 로직
		return userDao.userDetail(num);
	}
}
```
### 3. Controller에서 사용
- `@Autowired`된 Service 클래스의 메서드를 실행해서 데이터를 처리하고 반환한다. 이하생략