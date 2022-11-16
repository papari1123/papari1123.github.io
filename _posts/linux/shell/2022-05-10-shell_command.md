---
layout: single
title: Shell 기초 및 명령어
tags: [shell, cat, export]
categories: linux
---
셸은 커널에 명령을 전달하기 위한 사용자 인터페이스 역할을 한다. 셸 명령어는 실제로 커널에 실행할 내용을 의미한다.
여기서는 리눅스 표준 쉘인 bash shell을 기준으로 주로 설명한다.

# 셸

## 리눅스에서 셸의 위치
HW - Kernel - **Shell** - 사용자 or 응용프로그램   

## 명령어 실행 순서*
- 각 파일의 맨 아랫 부분에 실행 코드를 추가할 때 기준이다.
1. /etc/profile.d/ 에 있는 모든 sh 파일 (가령, /etc/profile.d/test.sh)
2. /etc/profile : 전역적인 파일로 **모든 사용자가 로그인 시 실행**
3. /etc/bashrc : 전역적인 파일로 logic 과정 없이 **bash shell이 실행하는 경우에만 실행.**
4. ~/.bashrc : 지역적인 파일로 특정 사용자가 bash shell을 실행할 때 실행됨.
5. ~/.bash_profile : 전역적인 파일로 특정 사용자가 shell을 실행할 때 실행됨.
6. (.bash_profile 이 없으면 .profile을 실행. .bash_profile 이 1순위이고, 우선순위에 따라 1개만 실행된다.)

### Login shell 과 Non-Login shell
/etc/profile와 ~/.bash_profile는 로그인이 필요하지 않은 경우에 실행된다.  
반면에 /etc/bashrc, ~/.bashrc는 로그인이 필요한 상황에서 쓰인다.  

### Jupyter의 shell :Ipython
**주피터는 ipython을 shell로 사용하기 때문에** **bashrc가 붙은 파일에 있는 명령어가 실행되지 않음**에 주의한다.  
profile에 있는 명령어는 사용이 가능하다.



# 유용한 셸 명령어 & 명령어 활용 방법
bash shell을 기준으로 한다.    
리눅스를 효율적으로 다루기 위해 필요한 명령어들,
또는 기본 명령어를 응용하는 방법들을 적어두었다.

### 쉘 커맨드 매뉴얼 문서를 보기 - man
종료는 :q를 치면 된다. 아래는 예시.
```commandline
man python
```
### 폴더 생성
```commandline
mkdir {folder_name}
```
### 파일 확인 : ls
```commandline
ls # 아무것도 작성안하면 현재 폴더 기준으로 실행된다.

# 옵션
-a : .으로 시작하는 파일, 폴더를 포함해 전체 파일을 출력한다.
-l : 퍼미션, 소유자, 만든 날짜, 용량까지 출력
-h : 용량을 사람이 읽기 쉽도록 GB, MB등 표현한다.

```
### 현재 폴더 경로를 절대 경로로 표현
```commandline
pwd
```

## 터미널을 깔끔하게 청소
```commandline
clear
```

### 쉘 커멘드 history 확인
```commandline
history
!30 # history 결과에서 30번째 커맨드를 다시 실행한다.
```

### 내용 확인
```commandline
cat test.txt     # 파일 내용 확인
cat /etc/shells  # 사용가능한 Shell 보기 
cat test.sh test2.sh > new_test.sh # 두 파일을 합쳐서 overwrite
```
  
### 터미널에 텍스트나 쉘커멘드 결과, 또는 현재 사용중인 Shell 보기 등
```commandline
echo "hello" # 터미널에 텍스트 출력
echo 'pwd' # ''로 쉘 커멘드 입력 시, 그 결과를 출력함
echo $SHELL # 사용중인 쉘을 확인
```

bash Shell은 실행 후 /etc/profile과 /etc/bashrc를 참조함.

### 명령어 위치 확인
which를 이용해 nvcc 명령어를 확인할 수 있다.
```commandline
which nvcc  
```

### 명령어 경로 추가
- export로 추가가 가능하나, 터미널이 꺼지면 사라짐.
- 영구적으로 유지하려면, bashrc 등에 export 명령어에 저장해야 함.
```commandline
export PATH=$PATH:/bin:/usr/local 
```

### 환경 변수 확인
export 명령어로 바로 확인 가능.
```commandline
export
```
### 쉘 스크립트 실행
bash는 쉘 스크립트를 실행하기 위한 명령어다
```commandline
bash vi-test.sh
```

### 파일 검색
```commandline
find . -name "test" # 현재 폴더에서 test란 이름을 가진 파일이나 디렉토리 검색
```

### 별칭 지정
```commandline
alias # 현재 별칭들을 확인함
alias ll2='ls -l' # ll2치면 ls -l 이 동작함.
```

### 앞/뒤의 n개 행을 출력 
head, tail로 가능하다.
```commandline
head -n 3 'test.sh'
tail -n 3 'test.sh'
```

### 파일 내용 sort
- 행단위로 파일 내용을 정렬한다.
- -r로 내림차순 정렬, -n으로 numeric sort를 지원한다.
```commandline
cat fruits.txt | sort
cat fruits.txt | sort -r 
```

### 중복 내용 제거
- 중복된 내용을 행 단위로 제거한다.
```commandline
cat fruits.txt | sort | uniq
```

### 조건부 검색 ★★★
- grep은 파일에 주어진 패턴 목록과 매칭되는 라인을 검색한다.
- 옵션은 여러가지가 있다.
  - -i 대소문자 구분없이 찾는다.
  - -w 정확히 그 단어만 찾는다.
  - -v 해당 패턴을 제외하고 찾는다.
  - -E 정규 표현식을 사용한다. (^단어 : 해당 단어로 시작 , 단어$ : 해당 단어로 끝, . : 하나의 문자 매칭)

### 서버에 request 테스트 명령어
```commandline
curl -X localhost:5000/ {data}
```

### ssh를 통한 파일 전송
- scp 명령어(Secure CoPy)를 사용하며, 옵션이 다음과 같다.
  - -r : 재귀적 복사
  - -P : ssh 포트 지정
  - -i : SSH 설정을 활용해 실행
```commandline
scp local_path user@ip:remote_directory
```

### 터미널 종료 후에도 작업 유지
nohup은 터미널 종료 후에도 계속 작업이 유지하도록 실행한다.
```commandline
nohup python3 test.py &  # 실행. 단, permisson이 755여야 함.
```
- 종료는, ps ef | grep app.py 후 pid 찾은 후 kill 명령어를 활용한다.
- 로그는 nohup.out에 저장된다.

### permission
- chmod로 r,w,x 권한을 줄 수 있다.
  - r: 읽기, 4
  - w: 쓰기, 2
  - x: 실행, 1
  - -: 권한없음
777 = r,w,x 모든 권한을 합한 것
```commandline

```

### 디스크 용량 확인
```commandline
df -h : 사람이 읽기 쉬운 형태로 용량 확인
```

### kill
강제종료
```commandline
kill -9 {PID} 
```

### 방화벽 해제
```commandline
ufw disable
```

# 표준 스트림
- Unix에서 동작하는 프로그램은 커맨드 실행 시 3개의 stream이 생성된다.
  - stdin : 0으로 표현되며, 커맨드와 비밀번호와 같은 입력에 해당한다.
  - stdout : 1로 표현되며, 출력값을 의미한다.
  - stderr : 2로 표현되며, 디버깅 정보나 에러값을 출력한다.

## redirection & pipe ★★★
- redirection은 프로그램의 출력을 다른 파일이나 스트림으로 전달한다.
  - \> 덮어쓰기 파일이 없으면 생성하고 저장한다.
  - \>> 맨 아래에 추가하는 append 기능.
```commandline
echo "hi" > vi-test.sh
echo "hello" >> vi-test.sh
```
- pipe는 프로그램의 출력을 다른 프로그램의 입력으로 사용한다.
  - a의 output을 b의 input으로 사용.
```commandline
ls | grep "vi" # 현재 폴더에 있는 파일명 중 vi를 찾는다.
ls | grep "vi > output.txt # 찾은 파일명 리스트를 output.txt로 저장한다.
history | grep "echo" "# 최근 입력 커맨드 중 echo가 들어간 명령어를 찾는다.
```


# vi
- vi는 리눅스 쉘에서 기본적으로 실행할 수 있는 vim 편집기로 파일을 생성하거나, 수정한다.    
- Command Mode, Insert Mode, Last Line Mode가 있다.
  - Command Mode : 기본 모드로 방향키를 통해 커서를 이동할 수 있다.
    - dd : 현재줄 삭제
    - yy : 현재줄 복사
    - x : 커서가 위치한 문자 1개 삭제
    - p : 현재 커서가 있는 줄 바로 아래에 붙여넣기
    - kjlh : 커서 위, 아래, 오른쪽, 왼쪽으로 이동
    - i : INSERT 모드로 변경
  - Insert Mode : 파일을 수정할 수 있다.
  - Last Line MOde :
    - ESC 누른 후 콜론을 누르면 나오는 모드이다.
      - w : 현재 파일명을 저장
      - q : vi 종료
      - wq : 저장 후 종료
- 수정은 INSERT 모드에서만 가능하며, vim 편집창이 뜨면 i키를 눌러 INSERT 모드로 변경한다.
- ESC를 눌러 :wq로 저장하고 나갈 수 있다.
- 


## @ 참고
- [환경변수](https://blog.naver.com/PostView.nhn?isHttpsRedirect=true&blogId=koromoon&logNo=220793570727)
- [zetawiki](https://zetawiki.com/wiki/Bash_%EC%89%98%EC%8A%A4%ED%81%AC%EB%A6%BD%ED%8A%B8_%EC%83%81%EB%8C%80%EA%B2%BD%EB%A1%9C_%EC%96%BB%EA%B8%B0)   
- [Shell script tutorial](https://www.shellscript.sh/quickref.html)   
- [colon을 이용한 참조](https://tldp.org/LDP/abs/html/parameter-substitution.html#EXPREPL1)   
- [명령어 실행 순서](https://zetawiki.com/wiki/Profile_bashrc_bash_profile_%EC%8B%A4%ED%96%89_%EC%88%9C%EC%84%9C)    
- 네이버 AI 부스트캠프
