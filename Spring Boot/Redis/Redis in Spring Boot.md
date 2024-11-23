## 사용방법
0. build.gradle에 `spring-data-redis` 추가
1. application.properties에 host와 port를 추가
2. RedisConfig 파일 만들기
3. - JPA의 엔티티의 경우 `@RedisHash` 설정
    - 그 외의 객체를 저장하려면 `@RedisTemplate` 설정
4. Redis에 저장
### 0. build.gradle에 `spring-data-redis` 추가
```gradle
implementation 'org.springframework.boot:spring-boot-starter-data-redis'
```
### 1. application.properties에 host와 port를 추가
- Redis가 서비스 중인 host와 port를 application.properties에 추가한다.
```properties
spring.redis.host=
spring.redis.port=
```
### 2. RedisConfig 파일 만들기
```java
@Configuration
public class RedisConfig {

    @Value("${spring.redis.host}")
    private String host;

    @Value("${spring.redis.port}")
    private int port;

    @Bean
    public RedisConnectionFactory redisConnectionFactory() {
        return new LettuceConnectionFactory(host, port);
    }
}
```
- Value 어노테이션을 통해 properties에서 값을 가져와 Redis와 연결하기 위한 설정을 한다

### 3-1. JPA의 엔티티의 경우 `@RedisHash` 설정
```java
@Entity
@Data
@RedisHash(value =, timeToLive=, ...)
public class Entity {

    @Id
    private Long id;
    //....
}
```
#### RedisHash 어노테이션
- Redis에 저장할 자료구조인 객체를 정의한다.