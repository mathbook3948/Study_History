# Docker 란?
- 컨테이너(Container) 기반의 오픈소스 가상화 플랫폼
## 이미지(Image)
- 컨테이너를 실행하는데 필요한 파일과 설정값들을 포함하고 있는 파일이다
- 일종의 프로그램 설치 파일이라고 생각하면 된다.
## 컨테이너(Container)
- 격리된 공간에서 프로세스가 동작하는 기술이다.
- 이미지를 설치 하고 실행한 상태이며, 추가되거나 변하는 값들은 컨테이너 안에만 존재한다.
- 같은 이미지에서 여러개의 컨테이너를 생성할 수 있고 컨테이너의 상태가 바뀌거나 컨테이너가 삭제되더라도 이미지는 변하지 않고 그대로 남아 있는다. 
# Docker in Linux
## 설치
```bash
sudo apt install docker.io
```
## Docker 실행
```bash
sudo systemctl start docker #시작
sudo systemctl restart docker #재시작
```
## Image
### Image 추가
```bash
docker pull ImageName
```
- ImageName에 다운 받고싶은 Image의 이름을 넣으면 된다.
### Image 제거
```bash 
docker rmi ImageName
```
- ImageName에 제거하고 싶은 Image의 이름을 넣으면 된다.
### Image 목록 확인
```bash
docker images
```
## Container
### Container 추가
```bash
docker container create [--name="ContainerName"] ImageName
```
- ImageName에 원하는 Image를 명시하면 된다.
- Container의 이름은 기본적으로 Image의 이름으로 설정되지만, `--name=` 속성을 주어 원하는 이름을 줄 수도 있다.
### Container 삭제
```bash
docker container rm ContainerName
```
### Container 확인
```bash
docker ps -a #모든 Container 확인
docker ps #실행된 Container만 확인
```
### Container 실행, 정지
```bash
docker start ContainerName # 시작
docker stop ContainerName #정지
```
### Container 추가 및 실행
```bash
docker run [--name=ContainerName] [옵션] ImageName
```
#### Container 실행 옵션
- `-p LocalPort:ContainerPort` : 로컬 시스템(Docker가 실행되는 컴퓨터)의 특정 포트를 컨테이너의 포트로 연결한다.
- `-d` : 컨테이너를 백그라운드에서 실행한다

---
# 정리 안된 내용
## Docker Container 접속
```bash
docker exec -it ContainerName /bin/bash #bash 환경으로 가상화 접속
```