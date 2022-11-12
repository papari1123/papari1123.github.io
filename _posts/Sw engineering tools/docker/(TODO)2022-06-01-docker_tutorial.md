---
layout: single
title: Docker(1) - 도커 개요
tags: [docker]
categories: docker 
work: 1
---
# Introduction
도커는 컨테이너 기반의 가상화 오픈플랫폼이다. 리눅스용으로 만들어졌지만, 윈도우에서도 사용이 가능하다.     
컨테이너는 도커 플랫폼에서 구성할 수 있는 독립적인 환경으로, 구동하려는 어플리케이션에 필요한 것들을 모두 포함한다.

# Docker architecture
도커는 client-server 구조를 사용한다. 
도커 클라이언트와 데몬은 동일한 시스템을 돌리거나 도커 클라이언트를 원격 docker daemon에 연결할 수 있다.
도커 클라이언트와 데몬은 REST API나 UNIX socket 또는 network interface 등을 이용해 통신할 수 있다.
또 다른 도커 클라이언트는 Docker compose로 컨테이너들을 포함한 어플리케이션들을 돌릴 수 있다.  



![](./../../../assets/images/(TODO)2022-06-01-docker_tutorial_images/1655105073538.png)


## Docker daemon
도커 데몬은 

The Docker client and daemon can run on the same system, or you can connect a Docker client to a remote Docker daemon. The Docker client and daemon communicate using a REST API, over UNIX sockets or a network interface. Another Docker client is Docker Compose, that lets you work with applications consisting of a set of containers.

The Docker daemon
The Docker daemon (dockerd) listens for Docker API requests and manages Docker objects such as images, containers, networks, and volumes. A daemon can also communicate with other daemons to manage Docker services.

The Docker client
The Docker client (docker) is the primary way that many Docker users interact with Docker. When you use commands such as docker run, the client sends these commands to dockerd, which carries them out. The docker command uses the Docker API. The Docker client can communicate with more than one daemon.

Docker Desktop
Docker Desktop is an easy-to-install application for your Mac or Windows environment that enables you to build and share containerized applications and microservices. Docker Desktop includes the Docker daemon (dockerd), the Docker client (docker), Docker Compose, Docker Content Trust, Kubernetes, and Credential Helper. For more information, see Docker Desktop.

Docker registries
A Docker registry stores Docker images. Docker Hub is a public registry that anyone can use, and Docker is configured to look for images on Docker Hub by default. You can even run your own private registry.

When you use the docker pull or docker run commands, the required images are pulled from your configured registry. When you use the docker push command, your image is pushed to your configured registry.

Docker objects
When you use Docker, you are creating and using images, containers, networks, volumes, plugins, and other objects. This section is a brief overview of some of those objects.

Images
An image is a read-only template with instructions for creating a Docker container. Often, an image is based on another image, with some additional customization. For example, you may build an image which is based on the ubuntu image, but installs the Apache web server and your application, as well as the configuration details needed to make your application run.

You might create your own images or you might only use those created by others and published in a registry. To build your own image, you create a Dockerfile with a simple syntax for defining the steps needed to create the image and run it. Each instruction in a Dockerfile creates a layer in the image. When you change the Dockerfile and rebuild the image, only those layers which have changed are rebuilt. This is part of what makes images so lightweight, small, and fast, when compared to other virtualization technologies.

Containers
A container is a runnable instance of an image. You can create, start, stop, move, or delete a container using the Docker API or CLI. You can connect a container to one or more networks, attach storage to it, or even create a new image based on its current state.

By default, a container is relatively well isolated from other containers and its host machine. You can control how isolated a container’s network, storage, or other underlying subsystems are from other containers or from the host machine.

A container is defined by its image as well as any configuration options you provide to it when you create or start it. When a container is removed, any changes to its state that are not stored in persistent storage disappear.
![img_2.png](img_2.png)

# Main content
포스팅에서 아래 내용들을 배우게 된다.
- Build and run an image as a container
- Share images using Docker Hub
- Deploy Docker applications using multiple containers with a database
- Running applications using Docker Compose
```commandline
docker run -d -p 80:80 docker/getting-started
```
- -d - detach mode (background mode)로 컨테이너를 동작
- p 80:80 - port 매핑, host의 80번 포트를 컨테이너의 80번 포트로 매핑.
  (-d 와 -p는 -dp로 줄여쓸 수 있다.)
- docker/getting-started - 사용할 도커 이미지


docker exec -it {container_id or name} /bin/bash

docker exec -it ubuntu20 /bin/bash

# 윈도우의 경우
docker exec -it {container_id or name} /bin/sh
또는
docker attach {cntainer}

# attach와 exec 차이 정리
attach 명령어
attach 명령어로 컨테이너에 진입할 시 도커로 주피터노트북을 백그라운드로 실행한 것이 포그라운드로 로그가 나오게 된다. 이럴 경우 터미널을 닫을 경우 주피터노트북 실행을 닫히게 되어 다시 도커로 주피터 노트북을 켜주어야 한다. (일반적으로 도커로 주피터을 실행할 시 포그라운드가 아닌 백그라운드로 시켜주는 이유도 이런 번거로움을 면하기 위해서이다.) 따라서, 백그라운드로 실행시킨 의미가 없어진다. 만약 도커의 로그가 보고 싶었던 것이라면 차라리 도커의 로그를 확인하는 명령어 logs를 활용하는 것이 현명하다.

exec 명령어

exec 명령어로 컨테이너에 접속할 시 (단, 명령어를 /bin/bash로 하였을 경우) 성공적으로 /bin/bash에 접속할 수 있다. 가끔씩 도커 가상환경의 버전에 맞는 환경세팅을 추가적으로 해주어야 하는 경우 주피터노트북에서 하는데에는 한계가 있으므로 이와 같이 /bin/bash로 접속하는 것이 효율적이다.
출처: https://biology-statistics-programming.tistory.com/120 [히비스서커스의 블로그:티스토리]


(아래 정리 https://wooono.tistory.com/348)
Docker run 옵션 종류
-i, --interactive
표준 입력(stdin)을 활성화하며, 컨테이너와 연결(attach)되어 있지 않더라도 표준 입력을 유지합니다.
보통 이 옵션을 사용하여 Bash 에 명령을 입력합니다.
-t, --tty
TTY 모드(pseudo-TTY)를 사용합니다.
Bash를 사용하려면 이 옵션을 설정해야 합니다.
이 옵션을 설정하지 않으면 명령을 입력할 수는 있지만, 셸이 표시되지 않습니다.
--name
컨테이너 이름을 설정합니다.
-d, --detach
Detached 모드입니다.
보통 데몬 모드라고 부르며, 컨테이너가 백그라운드로 실행됩니다.
이를 설정하지 않으면, 셀 위에서 컨테이너가 실행된다. 컨테이너 로그를 바로 볼 수 있으나,
컨테이너를 나가면 실행 종료.

-p, --publish
호스트와 컨테이너의 포트를 연결합니다. (포트포워딩)
<호스트 포트>:<컨테이너 포트>
포트 지정

-p 80:80
--privileged
컨테이너 안에서 호스트의 리눅스 커널 기능(Capability)을 모두 사용합니다.
호스트의 주요 자원에 접근할 수 있습니다.
--rm
프로세스 종료시 컨테이너 자동 제거
--restart
컨테이너 종료 시, 재시작 정책을 설정합니다.
--restart="always"
-v, --volume
데이터 볼륨을 설정입니다.
호스트와 컨테이너의 디렉토리를 연결하여, 파일을 컨테이너에 저장하지 않고 호스트에 바로 저장합니다. (마운트)
-u, --user
컨테이너가 실행될 리눅스 사용자 계정 이름 또는 UID를 설정합니다.
--user root
-e, --env
컨테이너 내에서 사용할 환경 변수를 설정합니다.
보통 설정 값이나 비밀번호를 전달할 때 사용합니다.
-e GRANT_SUDO=yes
--link
컨테이너끼리 연결합니다.
[컨테이너명 : 별칭]
--link="db:db"
-h, --hostname
컨테이너의 호스트 이름을 설정합니다.
-w, --workdir
컨테이너 안의 프로세스가 실행될 디렉터리를 설정합니다.
-a, --attach
컨테이너에 표준 입력(stdin), 표준 출력(stdout), 표준 에러(stderr) 를 연결합니다.
-c, --cpu-shares
CPU 자원 분배 설정입니다.
기본 값은 1024이며, 각 값은 상대적으로 적용됩니다.
-m, --memory
메모리 한계를 설정합니다.
<숫자><단위> 형식이며 단위는 b, k, m, g 를 사용할 수 있습니다
--memory=”100000b”
--gpus
컨테이너에서 호스트의 NVIDIA GPU 를 사용할 수 있도록 설정합니다.
호스트는 NVIDIA GPU 가 장착 된 Linux 서버여야하며,
NVIDIA driver 가 설치되어 있어야하고,
docker 19.03.5 버전 이상이어야합니다.
GPU 모두 사용하기
--gpus all
GPU 지정해서 사용하기
--gpus ‘”device=0,1”’
--security-opt
SELinux, AppArmor 옵션을 설정합니다.
--security-opt=”label:level:TopSecret”

# 도커 복사
![](./../../../assets/images/(TODO)2022-06-01-docker_tutorial_images/1657002173444.png)

![](./../../../assets/images/(TODO)2022-06-01-docker_tutorial_images/1657002775441.png)

# docker 실행 - my sql 실행하기
- docker pull "이미지 이름 :태그"
```commandline
# mysql 8 버전의 이미지를 다운
docker pull mysql:8 
docer images
```
- docker run "이미지 이름:태그"
- 다운받은 MYSQL 이미지 기반으로 Docker container 만들고 실행

- docker ps 명령어로 실행한 컨테이너 확인 가능
- 

(출처 : 네이버 부캠)
![](./../../../assets/images/(TODO)2022-06-01-docker_tutorial_images/1668145542337.png)


![](./../../../assets/images/(TODO)2022-06-01-docker_tutorial_images/1668145621543.png)

![](./../../../assets/images/(TODO)2022-06-01-docker_tutorial_images/1668145703048.png)

# Discussion




# Reference 
[도커 공식 문서](https://docs.docker.com/get-started/overview/)  
[안내서](https://subicura.com/2017/01/19/docker-guide-for-beginners-2.html