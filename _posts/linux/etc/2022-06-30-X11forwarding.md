---
layout: single
title: GUI 원격작업을 하기 위한 X-window 사용
tags: [linux, pycharm, X-forwarding, Putty]
categories: linux
work : 2
---
# Introduction
리눅스 서버를 다룰 경우 보통 CLI 환경에서 작업을 많이 한다.
하지만 부득이하게 GUI 환경이 필요한 상황이 있다.
특히 QT를 사용하거나 해야할 떄, 테스트해야할 프로그램이 무조건 GUI 환경을 요구하는 경우,
CLI만 지원하는 개발 환경에서는 **아래와 같이 could not connect to display 오류가 뜬다.**
![could-not-display](../../../assets/images/X11forwarding_images/1656554017647.png)

이를 해결하기 위해 먼저 리눅스 서버에 접속하기 위해 제일 간편한 CLI환경인 **Putty에서
X-forwarding을 사용하는 방법**을 알아보고, 이후 **Putty SSH Session의 터미널 환경과 같은 다른 환경에서도** 사용할 수 있는 방법을
알아본다. 이 과정을 이해하기 위해 필요한 개념들도 같이 포스팅했다.

## X-window
 X-window는 유닉스 계열 운영체제에서 GUI 환경을 쓸 수 있도록 하는 프레임워크다.
디스플레이에 창을 표시하며, 마우스와 키보드 등의 입력 장치와 상호 작용이 가능하다.     
 여기까진 기존 디스플레이 시스템과 별반 차이가 없으나, 중요한 것은 **네트워크 프로토콜(X 프로토콜)에 기반한 클라이언트-서버 모델의 네트워크 지향 윈도 시스템**이란 것이다.    
따라서 회사 서버실에 있는 리눅스 서버의 프로그램의 입력을 내 집 PC의 키보드로 입력할 수 있고, 동시에 모니터로 확인할 수도 있다. **즉 원격 작업을 가능하게 해준다.**

## X server와 X client
 서버-클라이언트 시스템에서 클라이언트는 서버에게 서비스나 정보를 요청하고, 서버는 요청에 응답한다.    
 그러나 원격으로 윈도우 클라이언트 PC로 리눅스 서버에 접속해 업무를 보는 일반적인 상황을 가정한다면, 
 **X-서버는 디스플레이 서비스를 제공해야 하므로 모니터가 달린 윈도우 pc에 위치하며, X-클라이언트는 응용프로그램으로서 GUI 서비스를 요청하는 리눅스 서버에 위치하게 된다.**
용어의 혼동이 있을 수 있어 정리가 필요한 부분이다.

# 1. Putty에서 X-forwarding을 사용하기

## ssh 설정 변경 (Server)
vi나 nano 같은 텍스트 편집기로 /etc/ssh에 ssh_config을 연다.
```commandline
cd /etc/ssh
sudo vi ssh_config 
```
ForwardX11 no를 ForwardX11 yes 로 수정하고, 아래 명령어로 서비스를 재시작한다.
```commandline
service sshd restart 
```

## X-window 설치 (client)
1. X-window를 설치한다. 아래 링크에서 설치하긴 했는데 다른 공식 링크가 있을 것 같다.   
https://sourceforge.net/projects/xming/
2. XLaunch를 실행하고 one window - start no client - Clipboard를 체크하고 마침을 누른다. (이건 일반적인 설정이고, 입맛에 맞게 바꿔도 된다.)
3. Putty를 설치한다. 공식사이트에서 설치할 수 있다.   
https://www.putty.org/
4. Putty Connection-SSH-X11에서 X11 forwarding에 Enable X11을 체크하고, Session에서 서버의 IP와 포트번호를 설정하고 실행한다. 
5. 이제 QT와 같은 GUI 지원이 필요한 프로그램을 실행해본다. 아래 예시처럼 X-window 창에 원격서버 프로그램이 GUI 환경에서 오픈이 된다.
![](../../../assets/images/2022-06-30-X11forwarding_images/1656555431039.png)

# 2. Pycharm SSH session 환경에서 X-forward 사용하기
위 Putty가 실행되는 것을 확인한 상태에서 진행이 가능하다.
1. Putty로 X11 forwarding Enable 체크 후 SSH 실행한 상태에서, export 쳐서 나오는 DISPLAY 변수를 확인한다.
![](../../../assets/images/X11forwarding_images/1656553681978.png) 

2. Pycharm SSH session을 열고, 터미널에서 DISPLAY 변수를 동일하게 수정한다.    
![](../../../assets/images/2022-06-30-X11forwarding_images/1656555655124.png)

3. 터미널에서 GUI 지원이 필요한 프로그램을 실행한다. **XLaunch와 Putty가 모두 실행된 상태여야 한다.**

+. 만약 Run/Debug로 실행할 경우
![](../../../assets/images/2022-06-30-X11forwarding_images/1656564662337.png)

그런데 이 방법은 Putty를 사용해야 해서 상당히 번거롭다.
Putty를 사용하지 않고 바로 할 수 있는 방법이 있을텐데, 찾게 되면 업로드를 할 예정이다.


# 자주 발생하는 오류들
## Connection refused ~~
아래와 같이 뜰 경우, XLaunch를 실행했는지 확인한다.
![](../../../assets/images/X11forwarding_images/1656553201286.png)

# Reference 
[깃허브블로그](https://vincentycyao.github.io/Vincent-DeepLearning-Blog/server/2020/09/02/PyCharm-Xforwarding.html)
[참고링크-네이버블로그](https://m.blog.naver.com/sunchan683/221465317759)    
[참고링크](http://yochin47.blogspot.com/2018/02/ubuntu-client-pc-pycharm-community.html)