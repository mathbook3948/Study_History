# Local Area Network
## HUB
- 포트들을 이용해서 컴퓨터를 물리적으로 연결하여 중앙으로 모으는 장치
### 문제점
- 연결된 모든 컴퓨터에 정보를 전달한다
- 동시에 서로 정보를 전달하면 중간에서 정보가 충돌할 수 있다(물리적으로 연결되어있기 때문에)
#### CSMA/CD(Carrier Sense Multiple Access / Collition Detection)
- 더미데이터를 실질적 데이터 이전에 먼저 보내어 충돌이 발생하는지 확인한 후, 데이터를 보낸다.
- //TODO https://www.geeksforgeeks.org/collision-detection-csmacd/
#### MAC(Medium Access Control)
```
# ex
fe:1b:63:84:45:e6
```
- 네트워크 인터페이스 카드에 각인된 물리적 주소
- 인터넷을 사용하는 모든 기기에는 MAC 주소를 가지고 있다
- 데이터를 보낼 때 본인과 수신자의 MAC 주소를 같이 보낸다(본인거만 받게 한다)
##### MAC 주소 구조
```
# ex
fe:1b:63:84:45:e6
```
- 콜론(:) 기준으로 1묶음에 1바이트씩 6바이트로 구성되어있다
- 각 자리는 16진법으로 되어있다(각 자리를 0~255라 할 수 있다)
- fe:1b:63 => 첫 3바이트는 IEEE 에서 기업, 단체에게 할당한다
- 84:45:e6 => 뒤 3바이트는 기업, 단체에서 할당한다

---
Frame
```
목적지 MAC 주소 + 소스 MAC 주소 + 데이터
```
ETHERNET Frame Format
```
PREAMBLE(7Bytes) + 
SFD(1Byte) + 
DESTINATION ADDRESS(6Bytes) +
SOURCE ADDRESS(6Bytes) +
LENGTH(2Bytes) +
DATA(46~1500Bytes) +
CRC(4Bytes)

```
- PREAMBLE : 10101010....을 56번 반복
- SFD(Start of frame delimiter) : 10101011 : 실질적 데이터가 시작되는 곳을 나타낸다
- LENGTH : 총 Frame의 크기를 나타낸다. 0~65534 값이 가능하며, 전체 크기는 1500Bytes를 넘을 수 없다
- CRC : 
- //TODO https://www.geeksforgeeks.org/ethernet-frame-format/
LAN 통신에서 가장 많이 쓰인다