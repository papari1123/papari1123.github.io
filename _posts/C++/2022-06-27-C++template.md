---
layout: single
title: C++ 문법(6) 템플릿
tags: [c++, template]
categories: C++
work: 0
---
# Introduction
템플릿은 매개변수의 타입에 따라 함수나 클래스를 다르게 생성하는 것이다.
자료형을 추상화한다고 생각해도 될 것 같다.

템플릿이 없으면 매개변수 자료형에 따른 함수나 클래스를 직접 정의해야 한다.
가령 아래와 같이 오버로딩으로 데이터 형식에 맞는 sum 함수를 따로 만들었다고 하자.
```cpp
int sum(int a, int b)
{
 return a + b;
}
double sum(double a, double b)
{
 return a + b;
}
```
데이터 형식만 다르지만 오버로딩으로 모든 함수를 다 만들어줘야 한다.

# 함수 템플릿
함수 템플릿을 사용하면 위와 같이 매개변수의 자료형이 달라도 하나의 함수로 만들 수 있다.
```cpp
template <typename 타입이름>
함수의 원형
{
 // 내용
}
```
예시는 아래와 같다.
````cpp
templete <typename T>
T sum(T a, T b)
{
 return a + b;
}

int a = 1, b = 2;
string s1 = "a";
string s2 = "b";

cout << "int sum :" << sum<int>(a, b) << endl;
cout << "string concat :" << sum<string>(s1, s2) << endl;
````

# 클래스 템플릿
함수 템플릿과 마찬가지로 클래스에 대해 타입에 따라 다르게 동작하는 클래스 집합을 만든다.
```cpp
template <typename T>
class 클래스템플릿이름
{
    // 클래스 멤버의 선언
}
```

예시는 아래와 같다.
```cpp
template <typename T>
class Data
{
private:
    T data_;

public:
    Data(T dt);
    data(T dt);
    T get_data();
};

Data<int> data(10);
```

# Reference
[TCP School 강의문서](http://www.tcpschool.com/cpp/cpp_template_function)  


