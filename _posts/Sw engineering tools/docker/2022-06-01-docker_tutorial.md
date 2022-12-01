---
layout: single
title: Docker(1) - 도커 개요
tags: [docker]
categories: docker 
work: 1
---
# Introduction

- 도커는 컨테이너 기반의 가상화 오픈플랫폼이다. 리눅스용으로 만들어졌지만, 윈도우에서도 사용이 가능하다.     
- 컨테이너는 도커 플랫폼에서 구성할 수 있는 독립적인 환경으로, 구동하려는 어플리케이션에 필요한 것들을 모두 포함한다.

# 가상화
- 가상화란 컴퓨터 리소스(하드웨어, 소프트웨어)의 추상화를 모두 포함한다. 여기에서는 소프트웨어 환경을 추상화하는 어플리케이션 가상화만을 다룬다.
- 주로 특정 **소프트웨어 환경을 local에서 만들고, 이를 production 서버에서 그대로 활용**하기 위해 쓰인다.
- 어떤 환경에서도 동일한 환경으로 프로그램을 실행할 수 있기 때문에, **개발과 운영 서버의 환경 불일치를 해소**할 수 있다.
- 방법은 크게 두 가지가 있다. 도커는 컨테이너 기반 가상화이다.
  - Virtual Machine 가상화
    - 호스트 머신이란 물리적 컴퓨터 위에, OS를 포함해 하드웨어를 가상화함. 대표적으로 AWS EC2가 있음.
    - 그러나 OS 위에 OS를 하나 더 실행시키면서 굉장히 많은 리소스를 사용한다.
    
  - Container 가상화
    - 좀 더 경량화된 방법
    - 서비스 배포 시, 원격 저장소에 이미지를 업로드하고, 서버에서 받아서 실행함.
    
# 도커의 기본 개념
- 도커를 이해하기 위해 (일반적인 사용자 관점에서) 기본 개념으로 Docker Image와 Container가 있다.
  - Docker Image
    - 컨테이너를 실행할 때 사용할 수 있는 일종의 템플릿으로 읽기만 가능하다. 
    - Dockerfile을 이용해서, 특정 소프트웨어를 실행하기 위한 환경(library, bin 파일 등)을 포함시킨다.
  - Docker Container
    - Docker Image를 활용해 실행된 인스턴스이다. 다른 컨테이너 간에서는 서로 격리되어있다.
    - Write가 가능하다.

# Docker architecture
- 도커의 동작원리를 알기 위해 구조를 알아보자.
먼저, 도커는 client-server 구조를 사용한다. 아래 그림에서 보이는 각 요소들에 대해 먼저 알아보자.
![](./../../../assets/images/(TODO)2022-06-01-docker_tutorial_images/1655105073538.png)

## Docker client (docker)
- 클라이언트는 유저가 도커와 상호작용을 하기 위한 창구 역할을 한다.
- 예를 들어 사용자가 docker run이란 명령어를 입력하면 client는 docker daemon에게 
해당 명령어를 전달한다.
- CLI에서 사용되는 docker는 Docker API 역할을 하는 셈이다.
- client는 하나의 docker daemon 뿐 아니라 여러개의 daemon과도 소통이 가능하다.

## Docker daemon (dockerd)
- Docker API의 요청을 대기하고, 도커 오브젝트(image, network, container, volumes)들을 관리해준다.
- docker 서비스를 관리하기 위해 다른 daemon과도 상호 소통할 수 있다고 한다.
- 참고로 daemon은 사용자가 직접적으로 제어하지 않고, 백그라운드에서 돌면서 여러 작업을 하는 프로그램을 말한다.
부모 프로세스를 가지지 않아 (엄밀히는 init 프로세스만을 부모 프로세스로 가진다.) PPID가 1로 정의된다.
## Docker registry
- registry는 docker images들의 저장소이다. 공개 저장소로 Docker Hub가 주로 쓰인다. 
- pull 또는 run 명령어로 registry에 있는 docker image를 가져다가 바로 사용할 수 있다.


# Docker를 실행할 때 일어나는 일
docker를 직접 사용하기 위해서 우분투 이미지를 한번 실행해보자.
```commandline
docker run -i -t ubuntu /bin/bash
```
다음과 같은 일이 차례로 일어난다.
1. local에서 ubuntu 이미지가 없다면 설정한 registry에서 docker image를 가져온다.
이 과정은 pull 명령어로 수동 실행할 수 있다.
2. docker는 새로운 컨테이너를 만든다. 이 과정 또한 docker container create 명령어로 수동실행할 수 있다.
3. 컨테이너에 호스트의 파일시스템과 독립적인 read-write 파일시스템을 할당한다.
4. network interfance를 생성하고 컨테이너에 연결한다. 호스트 머신의 network connection와 연결되어 외부 네트워크와도 연결된다.
5. /bin/bash를 실행한다.


# Reference 
- [도커 공식 문서](https://docs.docker.com/get-started/overview/)  
- [안내서](https://subicura.com/2017/01/19/docker-guide-for-beginners-2.html
- 네이버 AI 부스트캠프 (강의 내용을 바탕으로 재구성)
- [도커 컨테이너는 가상머신인가요? 프로세스인가요?](https://www.44bits.io/ko/post/is-docker-container-a-virtual-machine-or-a-process)