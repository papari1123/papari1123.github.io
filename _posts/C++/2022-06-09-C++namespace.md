---
layout: single
title: C++ 문법(3) 변수 scope와 네임스페이스
tags: [c++, namespace, scope]
categories: C++
work: 0
---
# Introduction
네임스페이스를 알기 전에 미리 아래 개념들을 알아야 한다.
## scope
변수의 유효범위(scope)란 해당 변수가 사용될 수 있는 범위를 의미한다.    
## linkage
연결은 해당 변수를 사용할 수 있는 파일의 접근 가능 여부를 나타낸다.
- 외부 연결을 가지는 변수는 여러 파일에서 사용이 가능하다.
- 내부 연결을 가지는 변수는 하나의 파일에서만 사용이 가능하다.
- 함수 내에서 선언된 변수는 함수 밖에서 사용될 수 없으므로 연결을 가지지 못한다.

## 변수의 종류
C++은 변수의 scope에 따라 아래 3가지로 변수를 나눌 수 있다.  
1. 자동 변수
2. 레지스터 변수
3. 정적 변수

### 자동 변수
  C언어에서는 local variable이라고 한다. 블록 내에서 선언된 변수로, 함수의 매개변수가 여기 속한다.
 변수가 선언된 블록 내에서만 유효하다. 메모리 상의 스택 영역에 저장되며, 블록이 종료되면 메모리에서 사라진다.
    
### 레지스터 변수
선언 시 register 키워드를 붙여 선언한 변수로, 기존 C++에서는 CPU의 register 메모리에 저장되는 변수로 쓰였으나,
C++11 부터는 자동 변수와 차이없이 쓰인다.

### 정적 변수
메모리 상의 데이터 영역에 저장되며, 프로그래밍이 실행되는 내내 유지되는 변수를 의미한다. 초기화하지 않으면 0으로 자동 초기화된다.
정적 변수는 연결을 어떻게 가지느냐에 따라 scope가 좀 다르다.
1. **연결을 가지지 않는 정적 변수**는 블록 내부에 static 키워드를 사용해 정의하며 블록 내에서만 접근 가능하나, 프로그램 종료까지 메모리가 유지된다.
2. **내부 연결을 가지는 정적 변수**는 함수 밖에서 static 키워드로 정의하며, 해당 변수를 포함하는 변환 단위(C++은 파일을 변환 단위라고 정의함) 내에서만 사용이 가능하다.
3. **외부 연결을 가지는 정적 변수**는 extern 키워드로 정의하여, 선언된 파일 외부에서도 사용가능한 변수이다.

file1.cpp
```cpp
#include <iostream>

using namespace std;

static int static_variable = 1; // 내부 정적 변수
int extern_variable = 2; // 외부 정적 변수로 쓰일 변수

void sum5(int input)
{
 static int five = 5;
 return input + five;
}

int main(void)
{
  print(sum5(static_variable))
}
```

file2.cpp
```cpp
#include <iostream>
#include "file1.cpp"
using namespace std;

extern int extern_variable;

...
```

# 네임스페이스
C++에서 정의된 다양한 내부 식별자들은 여러 라이브러리가 포함되어 프로그램이 커지면 서로 충돌할 가능성도 커진다.
이를 네임스페이스를 적용해 해결할 수 있다.

네임스페이스는 내부 식별자로 사용될 수 있는 유효 범위를 제공하는 선언적 영역을 의미한다.

## 네임스페이스를 정의하기
네임스페이스는 일반적으로 헤더 파일에 정의하며 다른 네임스페이스에서도 정의할 수 있다. 
그러나 블록 내에서는 정의할 수 없다.
C++에서는 전역 네임스페이스라는 파일 수준의 선언 영역이 존재하며, 식별자의 네임스페이스가 명시되지 않을 경우 이곳에 자동으로 저장된다.   

namespace.h
```cpp
namespace kim
{
  int test;
}

namespace lee
{
 char test;
}
```

namespace.c
```cpp
#include "namespace.h"
kim::test = 1;
lee::test = '1';
```

::는 범위 지정 연산자라고 하는데, 이걸 쓰진 않고 보통 using 지시자로 네임스페이스에 속한 식별자들을 가져온다.     

namespace_using.c
```cpp
#include "namespace.h"
using namespace kim ;
test = 1
```

# Reference
[TCP School 강의문서](http://www.tcpschool.com/cpp/cpp_scope_namespace)  
