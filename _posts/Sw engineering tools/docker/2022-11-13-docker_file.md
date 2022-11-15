---
layout: single
title: Docker(4) - Dockerfile 작성
tags: [docker, dockerfile]
categories: docker 
work: 1
---
# Introduction
docker Image를 빌드하기 위한 정보를 설정해주는 Dockerfile 작성 방법을 알아본다.

# Dockerfile 작성방법
## FROM
- FROM {이미지이름 : 태그}
- 보통 도커 이미지를 처음부터 만들지 않고, Docker hub 등에 있는 base 이미지를 사용해 빌드한다. 
- FROM 명령어는 사용할 base 도커 이미지를 지정한다.

## COPY
- COPY {로컬디렉토리} {컨테이너 디렉토리}
- 로컬에 있는 파일과 디렉토리를 컨테이너에서 사용할 수 있도록 COPY 명령어를 사용해 파일을 컨테이너 환경에 복사한다.

## WORKDIR 
- WORKDIR {컨테이너 디렉토리}
- 리눅스 pwd 명령어 처럼 RUN, CMD 등의 명령어를 실행할 컨테이너 내 경로를 지정한다.
- 이 명령어 이후, 모든 명령어가 해당 컨테이너 디렉토리를 기준으로 적용된다.

## ENV
- ENV {환경변수이름=값}
- 컨네이터 내 환경 변수를 지정한다. 

## RUN
- RUN {실행할 리눅스 명령어}
- 컨테이너 환경에서 실행할 리눅스 명령어를 입력한다. 실행할 명령어가 여러 개인 경우, &&\을 틍해 이어줄 수 있다.

## CMD
- CMD [{실행명령어}, {인자}]
- docker run으로 컨테이너를 만들 때, 즉시 실행할 명령어.

### CMD와 RUN의 차이?
- RUN은 도커 이미지를 빌드할 때 사용되는 커맨드이며, CMD는 생성된 도커 이미지를 런칭할 때 사용되는 이미지이다.
> **RUN** is an **image build step,** the state of the container after a RUN command will be committed to the container image. A Dockerfile can have many RUN steps that layer on top of one another to build the image.

> **CMD** is the command the container executes by default **when you launch the built image**. A Dockerfile will **only use the final CMD defined**. The CMD can be overridden when starting a container with docker run $image $other_command.

# 예시

```commandline
FROM python:3.8.7-slim-buster 

COPY . /app  # 현재 폴더에 있는 파일들을 /app에 저장함.
WORKDIR /app
ENV PYTHONPATH=/app # 
ENV PYTHONBUFFERED=1

RUN pip install pip==21.2.4 &&\
    pip install -r requirements.txt
   
CMD ["python", "main.py"]    
```
# Dockerfile 사용
- Dockerfile을 생성했다면, build 명령어로 Docker image를 만들 수 있다.
- -t {이미지이름:태그} 옵션으로 이미지 이름과 태그 지정가능.
- 태그가 latest일 시 생략 가능.
```commandline
docker build {Dockerfile이 위치한 경로}
docker build , -t my-appp
```
- 이후 docker run {이미지 이름:태그}로 방금 만든 이미지를 실행가능.

# Reference
- 네이버 AI 부스트캠프
- [difference-between-run-and-cmd-in-a-dockerfile](https://stackoverflow.com/questions/37461868/difference-between-run-and-cmd-in-a-dockerfile)