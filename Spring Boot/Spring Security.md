# Spring Security란?

- 로그인 등 보안과 관련된 기능을 쉽게 구현할 수 있게 해주는 라이브러리

## 용어

- Authentication(인증) : 해당 사용자의 신원을 확인하는 것
- Authorization(인가) : 해당 사용자의 권한을 확인하는 것
- Principal : 보호 대상인 리소스에 접근하는 대상
- Credential : Principal(대상)의 비밀번호
- Hashing(해싱) : 주어진 입력값을 일정한 규칙에 따라 변환하여 고정된 길이의 출력을 만드는 것. 불가역성, 고유성, 고정된 길이 같은 속성을 가지고 있다
- BASE64 : Unicode를 ASCII 영역 문자로 바꾸는 인코딩 방식
- CSRF(Cross site Request Forgery) : 공격자가 인증된 사용자의 권한을 악용하여 요청을 보내는 공격 기법. Session 방식에서 로그인이 유지될 때(서버에 정보가 남아 있을 때) 사용자가 악성 링크를 접속하면 로그인이 유지된 상태로 공격자가 원하는 요청을 처리하는 것을 말한다. 반대로 말하면 Rest API 만을 사용하는 서버라면 로그인 정보를 저장하지 않기 때문에 이 공격은 무시할 수 있다

# 아키텍쳐

```
UsernamePasswordAuthenticationFilter ->
ProviderManager ->
DaoAuthenticationProvider(+UserDetails) ->
ProviderManager ->
UsernamePasswordAuthenticationFilter ->
SecurityContextHolder
```

- 기본 필터 중 하나인 **UsernamePasswordAuthenticationFilter**에서 UsernamePasswordAuthenticationToken 객체를 반환한다.
- 여러개의 AuthenticationProvider을 관리하고, AuthenticationManager를 구현한 **ProviderManager** 클래스에서 AuthenticationProvider를 구현한 적절한 클래스에게 Authentication(UsernamePasswordAuthenticationToken)을 반환한다
- AuthenticationProvider를 구현한 **DaoAuthenticationProvider**(ID/PW 기반 로그인을 처리하는 객체)에서 UserDetailsService를 구현한 Bean을 찾아 loadUserByUserName을 통해 유저의 정보가 담긴 UserDetails 객체를 가져오고, PasswordEncoder를 구현한 객체를 찾아서 입력된 비밀번호를 Hashing 하고 인증을 시도한다.
- **DaoAuthenticationProvider**에서 인증을 성공할 시 인증 완료된 Authentication 객체를 생성하고, ProviderManager에게 반환한다.
- **ProviderManager**에서 UsernamePasswordAuthenticationFilter에게 Authentication 객체를 반환한다.
- **UsernamePasswordAuthenticationFilter**에서 Authentication 객체를 SecurityContext 객체에 넣고, SecurityContextHolder에 저장한다.

세션 방식 로그인을 사용할 때 일정 시간 후 로그인 해제

- application.properties에

```properties
server.servlet.session.timeout = 1m 2s .... //세션이 유지되는 시간(로그인이 유지되는 시간)
server.servlet.session.cookie.max-age=1m 3s ...//쿠키가 유지되는 시간(로그인 티켓(쿠키)가 유지되는 시간)
```

# ID/PW 로그인 방식

## 공통 구현 사항

### loadUserByUsername 메서드 구현

```java
//UserDetailsService
UserDetails loadUserByUsername(String username) throws UsernameNotFoundException;
```

- 로그인을 구현하려면 필수적으로 UserDetailsService를 구현한 클래스를 만들고, UserDetails을 구현한 클래스를 반환하는 loadUserByUsername 메서드를 만들어야 한다
- 이 메서드에서 DB에서 Username을 이용해 유저 데이터를 가져오고, 그 데이터를 UserDetails를 구현한 객체에 넣어 반환해야 한다.
- 모든 UserDetails를 구현한 클래스에 있는 `Collection<? extends GrantedAuthority> authorities` 변수가 있으며, DB에서 가져온 권한 정보를 그대로 넣을 수 없고, GrantedAuthority 객체로 변환한것들을 Collection에 넣어서 반환해야 한다. 이때, 가장 간단한 GrantedAuthority를 구현한 클래스는 **SimpleGrantedAuthority** 이며, 생성자에 role 매개변수를 받는데, 이때 role은 `ROLE_`로 시작해야한다.
- UserDetails를 구현한 가장 기본적인 클래스는 User(org.springframework.security.core.userdetails)이다

```java
//가장 기본이 되는 생성자
public User(String username, String password, Collection<? extends GrantedAuthority> authorities) {
		this(username, password, true, true, true, true, authorities);
	}
    //enabled, accountNonExpired, credentialsNonExpired, accountNonLocked 변수 모두 true로 설정한다
```

- 이 외에 복잡한 User 클래스를 만들고 싶다면 UserDetails를 구현 한 클래스를 만들면 된다.

## Session

- 서버에 로그인 정보를 저장하는 방식이다.
- 서버가 모든 로그인 정보를 가지고 있기 때문에 보안이 더 안전하다
- 서버가 모든 로그인 정보를 가지고 있어야 하기 때문에 서버의 부하가 심하다

### 방식

1. 유저가 로그인 시 서버의 메모리에 세션(로그인 정보)이 저장된다. 이때 세션에는 각각 ID가 존재한다
2. 유저의 브라우저에 쿠키로 Session ID가 저장된다
3. 유저가 요청을 보낼 때 마다 쿠키에 있는 Session ID도 같이 보낸다
4. 서버가 유저가 보낸 ID와 서버 메모리에 있는 ID 를 비교해서 일치하면 요청을 허가 해준다.

### 직접 구현 해보기

## JWT

- 여러가지 많은 정보들이 들어있는 티켓을 끊어서 준다.
- 티켓만 검사하면 되기 때문에, DB 조회 없이 신원을 조회할 수 있다(서버(DB) 부담이 줄어든다).
- 하지만 티켓이 털리면 막아줄 방법이 없다(사실 사용자 잘못). 그래서 보통 유효 시간을 짧게 설정한다(5~30분)

### 구성

- 문자열이다.
- header, payload, signature 부분이 `.`을 기준으로 나누어져 있다
- **Header** : 토큰의 유형과 signature의 알고리즘이 포함된다
- **Payload** : 사용자 정보, 만료 시간 등을 담고 있다.
- **Signature** : JWT의 진위 여부를 검증하기 위한 정보를 담고 있다

#### Header

- alg와 typ 두가지 정보로 구성된다.
- **alg** : Signature을 해싱하기 위한 알고리즘을 지정한다
- **typ** : 토큰의 타입을 알려준다(JWT 토큰이니까 JWT)

#### Payload

- 토큰에서 사용할 정보들을 담고 있다. 이 정보들을 담고 있는 것을 Claim 이라고 한다.
  //TODO Claim 종류 3가지 공부

#### Signature

- Signature은 Header와 Payload의 값을 BASE64로 인코딩하고, 그 값을 비밀 키를 이용하여 Header에서 정의 한 알고리즘(alg)로 해싱을 하고 이 값을 다시 BASE64로 인코딩하여 생성한다.

```
1. Header, Payload 인코딩
2. 1번에서의 값 + 비밀키 해싱
3. 2번을 다시 인코딩
```
### Refresh Token 
- JWT 토큰은 탈취당했을 시 공격자가 인증받은 척 하고 요청을 보낼 수 있기 때문에 일반적으로 유효 기간을 5~30분 정도로 짧게 해둔다.
- 유효기간이 짧다?? => 사용자는 5~30분 마다 로그인을 다시 해야한다(매우 귀찮음)
- 이를 해결하기 위해 Refresh Token을 도입할 수 있다.
#### 작동 방식
1. 사용자가 로그인 성공 시 Refresh Token, Access Token을 두개 받는다
2. Access Token이 만료되기 전까지 API 통신을 한다.
3. 시간이 지나 Access Token이 만료(요청을 보내도 401 반환)
4. 401이 반환되면 가지고 있는 Refresh Token을 같이 서버로 보냄
5. Refresh Token의 유효성을 서버에서 확인하고 응답과 함께 새로운 Access Token을 header에 같이 보낸다
6. 만약 Refresh Token도 만료되었다면 401 응답을 다시 보낸다
- Access Token을 다시 보낼때 기존 Refresh Token을 무력화 시키고 새로운 Refresh Token 보내서 보


### 직접 구현해보기
//TODO

#### build.gradle 추가

```gradle
implementation 'io.jsonwebtoken:jjwt-api'
implementation 'io.jsonwebtoken:jjwt-gson'
implementation 'io.jsonwebtoken:jjwt-impl'
```

#### SecurityConfig.java 설정

- Spring Security의 설정이 이루어지는 파일이다.

```java
/*
SecurityConfig 클래스 위에 어노테이션 설정
*/
@Configuration
@EnableWebSecurity
public class SecurityConfig {
    public SecurityFilterChain filterChain(HttpSecurity http) throws Exception {
        // 이 사이에 Spring Security 설정을 넣으면 된다
        return http.build();
    }
}
```

##### HttpSecurity 메서드

###### Filter 관련

- `.addFilterAfter(jakarta.servlet.Filter filter, Class<? extends jakarta.servlet.Filter> afterFilter)` : `afterFilter` 뒤에 filter을 추가한다
- `.addFilterBefore(jakarta.servlet.Filter filter, Class<? extends jakarta.servlet.Filter> beforeFilter)` : `beforeFilter` 앞에 filter을 추가한다

###### request 관련

- `.authorizeHttpRequests(Customizer<AuthorizeHttpRequestsConfigurer<HttpSecurity>.AuthorizationManagerRequestMatcherRegistry> authorizeHttpRequestsCustomizer)` : HTTP 요청(request)에 대한 보안 설정(로그인, 권한, 인증 등)을 정의하기 위한 시작점이다
- `.requestMatchers(String... antPatterns)` : HTTP 요청이 오는 URL을 선택하는 메서드이다. 후에 `.permitAll(), .authenticated()` 같은 메서드로 해당 URL에 조건을 걸 수 있다
- `.*anyRequest*()` : `requestMatchers(String... antPatterns)` : 로 연결되지 않은 모든 URL을 선택한다.
- `.permitAll()` : 선택된 URL로 오는 모든 요청을 허용한다.
- `.authenticated()` : 인증된(로그인) 사용자만 요청이 허용된다.
- `.hasRole(String role)` : 특정 역할(ROLE*ADMIN, ROLE_USER, ....)을 가진 사용자만 접근할 수 있도록 설정한다. 입력값으로는 역할 그대로의 이름(ADMIN, USER, ....)을 받고, 자동으로 `ROLE*`을 붙여 검사를 진행한다.
- `.hasAuthority(String authority)` : `hasRole(String role)`와 거의 유사하지만, `ROLE_`을 자동으로 붙여서 검사를 해주지 않는다. `ROLE_ADMIN` 처럼 끝까지 넣어주어야 한다.
- `.denyAll()` : 해당 경로에 대한 모든 요청을 거부한다.

###### 보안 설정

- `.csrf(Customizer<CsrfConfigurer<HttpSecurity>> csrfCustomizer)` : CSRF(Cross site Request Forgery) 보호를 활성화하거나 비활성화하는 설정

---

- `.cors(Customizer<CorsConfigurer<HttpSecurity>> corsCustomizer)` : CORS(Cross Origin Resource Sharing) 처리를 활성화 또는 비활성화하는 설정

---

- `.formLogin()` : 폼 로그인 창 설정의 시작점이다.
- `.loginPage(String path)` : 사용자 정의 로그인 폼 경로를 지정한다.
- `.loginProcessingUrl(String path)` : 로그인 폼에서 인증이 진행되는 경로를 지정한다. 기본값은 `/login` 이다
- `.defaultSuccessUrl(String path, boolean alwaysUse)` : 로그인 성공 후 이동할 URL을 설정한다. alwaysUse가 true이면 항상 지정된 URL로 이동하고, 이전 요청이 있으면 그쪽으로 이동한다.
- `.failureUrl(String path)` : 로그인 실패 시 이동할 URL을 설정한다

---

- `.sessionManagement(Customizer<SessionManagementConfigurer<HttpSecurity>> sessionManagementCustomizer)` : Session을 어떻게 관리할지 정하는 설정의 시작점이다.
- `.sessionCreationPolicy(SessionCreationPolicy policy)` : 세션을 어떻게 생성하고 유지할지 정한다. Rest API(JWT) 방식에서는 `SessionCreationPolicy.STATELESS` 로 설정하면 된다. 세션을 생성하거나 유지하지 않도록 설정한다.

---

- `.disable()` : `.csrf(), .cors(), .formLogin()` 등을 활성화하거나 비활성화하는 설정이다

#### JWT 토큰 구현

```java
public class JwtService {
    /*
    Keys 클래스 : SecretKey를 쉽게 생성할 수 있게 해준다.
    SecretKey 클래스 : byte 배열을 담는 형식을 지정한 interface이다
    */
    static final SecretKey key
            = Keys.hmacShaKeyFor // 바이트 배열을 사용하여 HMAC 방식으로 비밀 키를 생성한다.
            (
                Decoders.BASE64.decode // 바이트 배열로 변환하여 반환한다
                (
                    "jwtpassword123jwtpassword123jwtpassword123jwtpassword123jwtpassword"
                )
            );


    public static String createToken(Authentication auth) {
        Object principal = auth.getPrincipal();

        // principal이 UserDetails를 구현했는지 검사한다
        if (!(principal instanceof UserDetails)) {
            throw new IllegalArgumentException("Unexpected principal type: " + principal.getClass());
        }

        // loadUserByUsername 메서드에서 반환한 형식에 맞게 캐스팅 한다
        UserDetails user = (UserDetails) principal;
        String username = userDetails.getUsername();
        String authority = userDetails.getAuthorities().stream()
                .findFirst()
                .map(GrantedAuthority::getAuthority)
                .orElse("ROLE_USER");

        return Jwts.builder()
                .claim("username", user.getUsername())
                .claim("authorities", user.getAuthorities())// 원하는 값들을 넣는다
                .issuedAt(new Date(System.currentTimeMillis())) // 발행 시간
                .expiration(new Date(System.currentTimeMillis() + 3600 * 1000)) //1시간
                .signWith(key) // 해싱할 때 사용할 비밀키
                .compact(); // 최종 JWT 생성
    }

    /*
    Claims 클래스 : Map<String, Object>를 상속하고 있어 키-값 형태로 정보를 저장한다. 토큰에 담긴 정보에 접근하기 쉽게 해주는 기능들을 제공한다
    Jws 클래스 : JWT의 Payload 부분, Header 부분, getSignature 부분을 Claims 형태로 가지고 있다
    */
    public static Claims extractToken(String token) { //jwt 토큰 입력 받음
        Claims claims = Jwts
        .parser()  // JwtParserBuilder 객체를 불러온다
        .verifyWith(key) //JWT를 만들 때 쓴 Key 넣어주기
        .build() // 해당 Key를 이용하여 JwtParser 객체를 불러온다
        .parseSignedClaims(token) // 서명을 검증하고 데이터를 Jws<Claims> 형태로 반환한다
        .getPayload(); //사용자가 정의한 정보, 만료 시간 등 데이터를 Claims 형태로 반환한다
        return claims;
    }
}
```

#### **로그인**

```java
@PostMapping("/login") //무조건 POST 방식을 요구한다
    public ResponseEntity<?> login(@RequestBody Map<String, String> data, HttpServletResponse response) {
        if (!map.containsKey("username") || !map.containsKey("password")) {
            return ResponseEntity.badRequest().body("Username and password are required.");
        }

        // 사용자 정보를 UserDetailsService로부터 불러오기
        try {
            // Authentication 객체를 구현한 UsernamePasswordAuthenticationToken을 생성
            UsernamePasswordAuthenticationToken auth = new UsernamePasswordAuthenticationToken(data.get("username"), data.get("password"));

            // UsernamePasswordAuthenticationToken을 바탕으로 인증 시도
            Authentication authentication = authenticationManager.authenticate(auth);

            // 현재 로그인 정보를 가진 Authentication 객체를 SecurityContext 객체에 담아서 SecurityContextHolder 객체에 저장한다.
            SecurityContextHolder.getContext().setAuthentication(authentication);

            //현재 로그인 정보(Authentication 객체)을 이용하여 jwt 토큰을 만든다.
            String jwt = JwtService.createToken(authentication);

            //response에 Cookie 객체를 만들어 넣으면 클라이언트 측에 쿠키가 저장이 된다. 하지만 보안에는 좋지 않다

            return ResponseEntity.ok(jwt);
        } catch (UsernameNotFoundException e) {
            return ResponseEntity.status(HttpStatus.UNAUTHORIZED).body("User not found.");
        } catch (BadCredentialsException e) {
            return ResponseEntity.status(HttpStatus.UNAUTHORIZED).body("Invalid username or password.");
        } catch (Exception e) {
            // 예외 발생 시 내부 서버 오류 처리
            return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).body("Authentication failed: " + e.getMessage());
        }
    }
```

#### 접근 시 검사

```java
@Component
public class JwtFilter extends OncePerRequestFilter { //OnceOerRequestFilter 를 상속받아 한 요청에 한번만 실행되도록 한다

    @Override
    protected void doFilterInternal(HttpServletRequest request, HttpServletResponse response, FilterChain filterChain)
            throws ServletException, IOException { // 요청이 올때 작동시킬 필터를 설정한다

        /*
            Header의 Authorization에 담아서 오는 경우(Bearer)
            String token = request.getHeader("Authorization"); 
            if(token == null || !token.startsWith("Bearer ")) {
                filterChain.doFilter(request, response);
                return;
            }
            token = token.substring(7);
        */


        Cookie[] cookies = request.getCookies(); //여기서는 쿠키에서 가져오는 예시

        if(cookies == null) {
            return;
        }
        Cookie jwt = null;
        for (Cookie cookie : cookies) {
            if("jwt".equals(cookie.getName())) {
                jwt = cookie;
                break;
            }
        }
        if(jwt == null) { // 만약 토큰이 제공 안됐을시 패스한다
            filterChain.doFilter(request, response);
            return;
        }


        Claims claims = null;
        try {
            claims = JwtService.extractToken(jwt.getValue()); // 만든 extractToken을 이용하여 내용(Payload)을 가져온다
        } catch (Exception e) {
            response.setStatus(HttpServletResponse.SC_UNAUTHORIZED);
            return;
        }

        //권한을 하나만 String 형식으로 토큰에 넣어 넘긴 예시
        List<GrantedAuthority> authorities = new ArrayList<>();
        authorities.add(new SimpleGrantedAuthority(claims.get("authority", String.class)));

        var authToken = new UsernamePasswordAuthenticationToken( // Authentication을 구현한 UsernamePasswordAuthenticationToken을 생성한다
            claims.get("username"),"", authorities //username은 가져오지만, 비밀번호는 JWT 토큰을 만들 때 넣지 않아 몰라서 빈 문자열 넣음
        );

        //SecurityContextHolder에 현재 로그인 정보(Authentication 객체)를 SecurityContext에 담아서 저장
        SecurityContextHolder.getContext().setAuthentication(authToken);

        //다음 필터로 넘어가게 한다
        filterChain.doFilter(request, response);
    }

}
```
