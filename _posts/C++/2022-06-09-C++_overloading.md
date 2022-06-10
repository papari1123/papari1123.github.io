---
layout: single
title: C++ 문법(2) 오버로딩
tags: [c++, 오버로딩, overloading]
categories: c++
work: 0
---
# Introduction
오버로딩이란 **같은 기능을 수행하는 함수의 매개변수 형식만 달리해서 사용할 수 있도록 해주는 것**이며, 객체 지향 프로그래밍 특징인 다형성을 만족하도록 한다.
# 함수 시그니처
시그니처란 함수의 원형에 명시되는 매개변수 리스트를 가리킨다.

두 함수가 매개변수의 개수와 그 타입이 모두 같다면, 이 두 함수의 시그니처는 같다고 할 수 있다.
오버로딩은 서로 다른 시그니처를 갖는 여러 함수를 같은 이름으로 정의하는 것이다.

# 오버로딩 예시
```cpp
int add(int a, int b)
{
    return a + b;
}

string add(string a, string b)
{
    return a + b;
}

int main(void)
{
    cout << add(1, 2) << endl; 
    cout << add("1", "2") << endl;
    return 0;
}
```
# Discussion
C++에서 추가된 overloading은 다형성을 만족시키는 좋은 기능이다.

# Reference
[TCP School 강의문서](http://www.tcpschool.com/cpp/cpp_cppFunction_overloading)  
