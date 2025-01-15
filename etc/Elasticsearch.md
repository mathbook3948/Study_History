# ElasticSearch 란?
- 분산 검색 및 분석 엔진으로, 빠르고 유연한 데이터 검색, 분석, 그리고 저장을 가능하게 해주는 도구이다. 주로 로그 데이터, 텍스트 데이터 등 대량의 데이터를 처리하고 검색하는 데 사용된다. Elasticsearch는 오픈 소스 기반으로, Lucene이라는 강력한 검색 라이브러리를 바탕으로 만들어졌다.
- 분산 검색이란, 데이터를 여러 서버(또는 노드)로 나누어 저장하고, 검색 요청이 들어오면 여러 노드에 병렬로 검색하고, 반환한다
## 기본 구조
```
Elasticsearch
└── index : 데이터베이스
    └── document : 데이터베이스의 행과 비슷
        └── field : 데이터베이스의 셀과 비슷
```
- 이런식으로 저장 후, 요청이 들어오면 분석(토큰화, 정규화 등)을 통해 연관도가 가장 높은 결과를 반환한다
## 사용 방법
- 기본적으로 9200 포트에서 작동(ex:localhost:9200)
```shell
# 시작
./bin/elasticsearch

# 종료
./bin/elasticsearch -s

# plugin(ex: nori) 확인
./bin/elasticsearch-plugin list
```
### settings
```
"settings": {
    
}
```
#### index
```
"index": {

}
```
- number_of_shards : 데이터를 몇개로 쪼갤지. 5개 -> 데이터를 5개로 나누어 검색 시 병렬 처리 가능
#### analysis
```
"analysis": {
    "analyzer": {
        "my_analyzer1": { // 이름은 알아서 지정하기
            "type":
            ["tokenizer": ]
            ["filter": ] // 배열로 여러 개 설정 가능
        },
        "my_analyzer2": {
            ...
        }
    }
}

// 실제 적용 예시

"mappings": {
    "properties": {
      "title": {
        "type": "text",
        "analyzer": "my_analyzer1"
      },
      "content": {
        "type": "text",
        "analyzer": "my_analyzer2"
      }
    }
}
```
- nori 설치 : `./bin/elasticsearch-plugin install analysis-nori`
##### "type"
- 분석기의 종류를 지정한다
```
"custom" : tokenizer와 filter을 직접 지정해서 사용한다 
"standard" : 기본 설정된 토크나이저와 필터 사용
"simple" : 알파벳만 남기고 소문자로 변환
"whitespace" : 공백만 기준으로 분리
"keyword" : 전체를 하나의 키워드로 처리
```
##### "tokenizer"
```
"standard" : 공백, 특수문자를 기준으로 분리
"whitespace" : 공백으로만 분리. 특수문자는 유지
"ngram" : //TODO
"edge_ngram" : 시작부터 연속으로 분리(ex:apple -> ["a", "ap", "app", "appl", "apple"])
"keyword" : 전체를 하나로 처리
"nori_tokenizer" : 형태소 단위로 분리
```
##### "filter"
```
"lowercase" : 소문자로 전환한다
"uppercase" : 대문자로 전환한다
"stop" : 불용어(the, a..등) 제거
"stemmer" : 어근 추출
"synonym" : 동의어
"nori_readingform" : 한자를 한글로 변환한다
"nori_part_of_speech" : 특정 품사를 제거해준다
```
#### 타입 설정
```
mappings": {
    "properties": {
      "text_field": { "type": "text" },          // 전문 검색용
      "keyword_field": { "type": "keyword" },    // 정확한 값 매칭
      "long_field": { "type": "long" },          // 정수
      "double_field": { "type": "double" },      // 실수
      "boolean_field": { "type": "boolean" },    // 참/거짓
      "date_field": { "type": "date" },          // 날짜
      "object_field": { "type": "object" }       // JSON 객체
    }
}
```
#### 분석기 설정(검색 관련)
### 고급 검색
#### 1. 오타 허용
```shell
curl -X GET "localhost:9200/books/_search" -H "Content-Type: application/json" -d'
{
  "query": {
    "fuzzy": {
      "title": {
        "value": "해리포타",
        "fuzziness": 1
      }
    }
  }
}'
```
- fuzzy : 
#### 2. 부분 검색(와일드 카드)
#### 3. 자동 완성
#### 4. 범위 검색
#### 5. 복합 검색
#### 6. 가중치 검색
# Kibana
- Elasticsearch의 데이터를 시각화를 통해 직관적으로 정보를 보여주기 위한 도구
- 브라우저 인터페이스를 활용하여 많은 데이터를 시각화 및 분석 할 수 있다
- Kibana와 Elasitcsearch의 버전은 반드시 동일해야한다
## 사용 방법
- 기본적으로 5601 포트에서 작동한다
### 서버의 상태 확인하기
```
http://YOUR_DOMAIN_OR_IP:5601/status
```
### Analytics
#### Discover
- 데이터를 확인하고 탐색하기 위한 용도
#### Visualize
- 데이터를 시각화하기 위한 도구를 제공한다
#### Dashboard
- 데이터를 여러 관점으로 볼 수 있는 화면을 제공한다