# WADO-RS(Web Access to DICOM Objects by RESTFul Services)

## 1. 기본 개념

### DICOM이란?
- Digital Imaging and Communications in Medicine의 약자
- 의료 영상 데이터의 표준 형식
- CT, MRI, X-ray 등 의료 영상을 저장/전송하는 표준 방식

### WADO-RS란?
- 웹을 통해 DICOM 이미지를 주고받기 위한 현대적인 방식
- REST API를 사용해서 의료 영상을 조회/다운로드
- 기존의 복잡한 DICOM 통신을 웹 기반으로 단순화

### 일반 http 요청과 다른 점
#### 일반 HTTP
```http request
GET /api/images/123
```
- 서버마다 응답 구조가 다름
- 자유로운 URL 구조
```
# 자유로운 반환값 가짐
Accept: application/json
Content-Type: application/json
```

#### WADO-RS 
```http request
GET /studies/{studyUID}/series/{seriesUID}/instances/{instanceUID}
```
- DICOM 표준에 따른 고정된 URL 구조
- 의료 영상의 계층 구조 반영 (Study > Series > Instance)
```
# 반환값이 제한적임
Accept: application/dicom   // DICOM 원본
Accept: application/dicom+xml  // DICOM 메타데이터
Accept: image/dicom+jpeg  // DICOM 이미지를 JPEG로
```
```json
{
  "PatientID": "12345",
  "StudyDate": "20240125",
  "Modality": "CT",
  "PixelSpacing": [0.5, 0.5],
  ...수백개의 표준화된 태그
}
```
- DICOM 표준의 복잡한 메타데이터 포함


## 2. 주요 기능

### 의료 영상 조회
```
예시: 환자의 MRI 스캔 영상을 조회하는 경우

1. Study 단위 조회 
   - 환자의 특정 검사(예: 2024년 1월 MRI 검사) 전체 조회
   URL: /studies/1.2.3.4.5

2. Series 단위 조회
   - 검사 중 특정 시리즈(예: 횡단면 영상들) 조회
   URL: /studies/1.2.3.4.5/series/1.2.3.4.6

3. Instance 단위 조회  
   - 시리즈 중 특정 영상 한 장 조회
   URL: .../instances/1.2.3.4.7
```

### 영상 데이터 종류
1. 원본 DICOM 데이터
    - 의료용 viewer에서 사용
    - 모든 메타데이터 포함

2. Bulk Data(픽셀 데이터)
    - 실제 영상 부분만 추출
    - 웹에서 보여주기 용도

3. 메타데이터
    - 환자 정보, 촬영 정보 등
    - 영상 없이 정보만 필요할 때

## 3. 실제 사용 예시

### EMR/EHR 시스템 연동
```
1. 의사가 EMR에서 환자 차트 확인
2. 영상 조회 버튼 클릭
3. WADO-RS로 영상 서버에 요청
4. 웹 브라우저에서 영상 표시
```

### 의료 영상 공유
```
1. 병원 A의 PACS에서 영상 저장
2. WADO-RS URL 생성
3. 병원 B에서 URL로 영상 조회
4. 표준 방식으로 호환성 보장
```

## 4. 보안과 안전성

### 데이터 보호
- HTTPS 암호화 통신 필수
- 의료 정보 보호 규정 준수
- 접근 권한 관리

### 인증 방식
```
1. 기본 인증
   - ID/Password 방식
   - 간단하지만 보안성 낮음

2. 토큰 인증
   - JWT 등 토큰 사용
   - 보안성 높고 관리 용이

3. 인증서 기반
   - SSL 인증서 사용
   - 가장 높은 보안성
```

## 5. 성능 최적화

### 데이터 효율성
- 필요한 부분만 선택적 전송
- 압축 기술 활용
- 캐싱 전략 적용

### 로딩 최적화
```
1. Progressive Loading
   - 저해상도 먼저 표시
   - 점진적으로 고화질로 개선

2. Prefetching
   - 예상되는 다음 영상 미리 로드
   - 빠른 응답성 제공
```