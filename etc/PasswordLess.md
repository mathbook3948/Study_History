# PasswordLess 란?

## 사용하는 이유
- 기존 인증 방식은 서비스가 사용자를 일방적으로 인증하는 방식.
- 하지만 사용자가 서비스가 진짜인지 검증하지 못하는 문제가 있다.
- 이를 해결하기 위해 서비스와 사용자 간의 상호인증을 통하여 서로 진짜인지 검증을 하는 방법을 사용할 수 있다.

# PasswordLess X1280
## 설치 방법
1. PasswordLess X1280 members 가입
2. 테스트 모드로 서비스 생성
3. docker 설치, 네트워크 설정
4. image 다운로드 및 실행
### 1. PasswordLess X1280 members 가입
https://members.passwordlessalliance.org/aod/web/login/p/login
- 위 링크에 들어가서 회원가입
### 2. 테스트 모드로 서비스 생성
```
## 필요한 정보
서비스 도메인
서비스의 사설 IP : 152.67.200.235,182.220.224.39 // 예시
유저 커넥션 서버의 도메인
```
- 생성 후 라이선스 키 파일(.ap) 다운로드 및 저장
### 3. docker 설치, 네트워크 설정
```shell
#ubuntu 예시
sudo apt install docker.io

#rocky 예시
dnf config-manager --add-repo=https://download.docker.com/linux/centos/docker-ce.repo
dnf -y install docker-ce docker-ce-cli containerd.io 
```
- docker 설치는 알아서 OS에 맞게
```shell
systemctl start docker # 도커 실행
systemctl enable docker	# 서버 부팅시 자동 실행
systemctl status docker	# 현재 도커 상태 확인
```
- 필요 시 실행
```shell
docker network create some-network # 도커에서 사용할 네트워크 설정
docker network ls # 설정한 네트워크 확인
```
- 예시에서는 some-network 라는 네트워크 그룹 생성
### 4. image 다운로드 및 실행
```shell
docker run -d --name server \
    --network some-network \
    --restart always \
    --cpus=1 \
    --cpuset-cpus="0" \
    --cpu-shares=1024 \
    --memory=1g \
    --memory-swap=2g \
    -e DOMAIN=<<서버의도메인주소>> \
    -e USE_SSL=false \
    -v auth-settings:/opt/x1280/tomcat/conf/passwordless \
    -v auth-logs:/opt/x1280/tomcat/logs \
    -v user-connection-logs:/opt/x1280/connector/logs \
    -v push-request-logs:/opt/x1280/pushConnector/logs \
    -v config:/etc/opt/x1280 \
    -v database:/var/lib/mysql \
    -p 8006:8005 \
    -p 8080:8080 \
    -p 8180:8180 \
    -p 8143:8143 \
    -p 8443:8443 \
    -p 11040:11040 \
    -p 12010:12010 \
    -p 15010:15010 \
    dualauth/passwordless-x1280-single:latest
```
- `서버의도메인주소`에는 현재 서버의 도메인(IP)을 넣어준다.
### 5. 서버 방화벽 설정
```shell
# ubuntu 예시
sudo apt install -y firewalld

# rocky 예시
dnf install -y firewalld
```
- 방화벽 설치
```shell


systemctl start firewalld # 방화벽 실행
systemctl enable firewalld # 서버 부팅시 자동 실행
systemctl status firewalld # 현재 방화벽 상태 확인

firewall-cmd --list-all # 방화벽 목록 조회

# 필요한 포트 오픈
firewall-cmd --zone=public --permanent --add-port=8005/tcp
firewall-cmd --zone=public --permanent --add-port=8080/tcp
firewall-cmd --zone=public --permanent --add-port=8180/tcp
firewall-cmd --zone=public --permanent --add-port=8143/tcp
firewall-cmd --zone=public --permanent --add-port=8443/tcp
firewall-cmd --zone=public --permanent --add-port=11040/tcp
firewall-cmd --zone=public --permanent --add-port=12010/tcp
firewall-cmd --zone=public --permanent --add-port=15010/tcp

firewall-cmd --reload # 추가된 방화벽 포트 반영

systemctl restart docker.service # 필요 시 docker 재시작
```
### 6. 인증 서버 확인
```shell
docker exec -it server /bin/bash
```
- docker container 내부 shell로 들어감
```shell
# ubuntu 예시
sudo apt -y install procps

# rocky 예시
dnf -y install procps
```
- ps 명령어 설치

```shell
#Docker Auth Server 확인
#폴더 : /opt/x1280/tomcat

ps -ef | grep tomcat

#Docker User Connection Server 확인
#폴더 : /opt/x1280/connector

ps -ef | grep connect
ps -ef | grep nginx

#Docker Push Request Server 확인
#폴더 : /opt/x1280/pushconnector

ps -ef | grep push
```
- 제대로 실행 되는지 확인
### 7. .ap 파일 업로드 및 admin 접속
- 서버주소의 8143포트로 접속 후, .ap 설정 파일 업로드
- 이후 나온 창에 (admin, admin) 입력해서 접속.
- 서버 키 발급 눌러서 새로운 키를 발급받고, 서버 아이디와 함께 저장 해놓기

  