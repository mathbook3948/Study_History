![Trie](https://github.com/user-attachments/assets/678673c9-2a3d-4f5e-8439-21df0af7ca38)# Tree 구조란?
- 계층적 데이터를 효율적으로 탐색하기 위해 사용되는 자료 구조
## 특징
- 계층적 구조 : 사진에서 보이는것 처럼 부모->자식 요소로 구성되어 있다(단, 루트 요소는 제외)
- 비순환성 : 트리 구조에서는 한 노드에서 시작해서 다른 노드를 따라가더라도 자기 자신으로는 절대 돌아올 수 없다. 반대로 말하면 일치하는 노드를 따라가다 보면 결국에는 목표에 도달한다

## 장점
- 목표하는 데이터 탐색이 매우 빠르다.
## 단점
- 노드로 단어를 나눠서 저장하기 때문에 크기를 많이 차지한다.
- 한 노드로 데이터가 치우칠 경우 검색이 느려질 수 있다

# 종류
## Trie 구조
- 문자열을 효율적으로 검색하기 위한 자료 구조이다 
- 사전에서 단어를 찾는것을 생각하면 된다
![Trie](https://github.com/user-attachments/assets/fc56d210-c1e1-44d2-b723-be79a998eea8)

### 구현
#### Java
##### TrieNode.java
```java
public class TrieNode implements Serializable{

    Map<Character, TrieNode> children; // 현재 노드에서 갈 수 있는 다음 노드를 저장
    boolean isEndOfWord; //마지막 단어. 즉, 여기서 단어가 끝이 나는지
    String word;
    //Long id;      // 필요한 데이터 자유롭게 추가. 단, 단어의 끝일 때만 값이 들어가고 아닐경우 null

    public TrieNode() {
        children = new HashMap<>();
        isEndOfWord = false; 
        word = null; //단어의 끝이면 해당 단어를 저장, 아닐 경우 null
        id = null; 
    }
}
```
- 각 노드에는 다음에 어떤 글자가 들어갈 수 있는지 Character 형태의 Key, 또 그 다음 글자를 저장하기 위해 다른 TrieNode를 가지고 있다
##### Trie.java
###### 멤버 변수, 생성자
```java
@Data
public class Trie implements Serializable {

    private TrieNode root; // root, 즉 빈 노드

    public Trie() {
        root = new TrieNode(); // 뿌리노드를 생성한다.
    }
}
```
###### insert 메서드
```java
public void insert(String word, Long id) {
    TrieNode current = root; // 현재 root 노드를 선택(빈 노드)
    for (char ch : word.toCharArray()) { // 한 글자씩 선택하여 자식 노드를 만들어서 저장
        current.children.putIfAbsent(ch, new TrieNode()); // 자식 노드가 있는지 검사 후 없다면 새로운 TrieNode 생성. Key에 현재 글자, Value에 새로운 TrieNode를 put 한다
        current = current.children.get(ch); // 현재 글자의 노드를 가져와 current에 덮어씌움(다음 글자를 넣기위한 준비)
    }
    current.isEndOfWord = true; // 만약 단어의 끝이라면 isEndOfWord를 true로 바꾼다
    current.word = word; // 이후 데이터 삽입
    //current.id = id;
}
```
###### getWords 메서드
```java
public List<Pair<String, Long>> getWords(String prefix) {
    List<Pair<String, Long>> result = new ArrayList<>(); //결과를 담을 List

    if (prefix == null || prefix.isEmpty()) {
        return result;
    }

    TrieNode current = root; // 현재 root 노드를 선택

    // 주어진 단어의 노드를 따라가며 Trie 탐색
    for (char ch : prefix.toCharArray()) { // prefix 글자에 해당하는 노드를 찾고, 찾으면 current에 저장
        if (!current.children.containsKey(ch)) {
            return result; // 해당하는 노드가 없으면 빈 리스트 반환
        }
        current = current.children.get(ch); // 해당 노드로 이동
    }

    // 실제로 문자열을 찾는 메서드
    findWordsFromNode(current, result);
    
    return result;
}
```
##### Pair.java
```java
public class Pair<T, U>  implements Serializable{ // T, U 두개의 자료형을 제네릭으로 받음

    public T first;
    public U second;

    public Pair(T first, U second) { // 생성자로 값을 넣어줌.
        this.first = first;
        this.second = second;
    }
}
```
- Map과 비슷하게 값을 저장하지만, 하나만 저장 가능하다
##### TrieNodeSerializer.java
- TrieNode의 구조가 복잡해서 Redis에 일반적으로 들어가지 않는 문제를 해결하기 위해 Custom Serializer를 지정해야 한다
```java
public class TrieNodeSerializer extends JsonSerializer<TrieNode> { // JsonSerializer을 상속하는 클래스 생성. 제네릭에 직렬화 대상을 넣어줌

}
```
###### serialize 메서드 오버라이드
```java
@Override
public void serialize(TrieNode value, JsonGenerator gen, SerializerProvider serializers) throws IOException {
    gen.writeStartObject();
    
    // 필드 직렬화
    gen.writeBooleanField("isEndOfWord", value.isEndOfWord); //Root 노드의 단어가 끝인지 여부를 직렬화
    
    if (value.word != null) {
        gen.writeStringField("word", value.word); // isEndOfWord가 true이고, word에 값이 있다면 word를 직렬화
    }
        
    if (value.id != null) {
        gen.writeNumberField("id", value.id); // isEndOfWord가 true이고, id에 값이 있는면 id를 직렬화
    }

    /*
        여기 까지의 구조. Root 노드이기에 모두 false, null 이다
        {
            "isEndOfWord": false,
            "word" : null,
            "id" : null
        }
        */

    if (!value.children.isEmpty()) { // children 노드 있을 경우 직렬화
        gen.writeFieldName("children"); // children 이라는 키를 추가
        gen.writeStartObject(); // 자식 노드 객체의 시작
        for (Map.Entry<Character, TrieNode> entry : value.children.entrySet()) { // 해당 자식노드를 Map.Entry 형식으로 하나씩 불러옴
            gen.writeFieldName(String.valueOf(entry.getKey()));// 자식노드의 단어를 Key로 만듦
            serialize(entry.getValue(), gen, serializers); // serialize를 다시 호출하여 반복
        }
        gen.writeEndObject(); // 자식 노드 객체의 끝
    }

    /*
        구조
        {
            "isEndOfWord": false,
            "word" : null,
            "id" : null,
            "children" : {
                "a" : {
                    "isEndOfWord": false,
                    "word" : null,
                    "id" : null,
                    "children" : {
                        "a" : {
                            "isEndOfWord": false,
                            "word" : null,
                            "id" : null
                        },
                        "b" : {
                            "isEndOfWord": false,
                            "word" : null,
                            "id" : null
                        }
                    }
                },
                "b" : {
                    "isEndOfWord": false,
                    "word" : null,
                    "id" : null,
                    children : {
                        .....
                    }
                },
                ....
            }
        }
        */

    gen.writeEndObject(); // 직렬화 완료(닫기)
}
```
##### TrieNodeDeserializer.java
```java
public class TrieNodeDeserializer extends JsonDeserializer<TrieNode> { // JsonDeserializer 상속 받고 제네릭에 역직렬화 원하는 대상

}
```
###### deserialize 메서드 오버라이드
```java
@Override
public TrieNode deserialize(JsonParser parser, DeserializationContext context) throws IOException {
    JsonNode node = parser.getCodec().readTree(parser);
    return deserializeNode(node);
}
```
