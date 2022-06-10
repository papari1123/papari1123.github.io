---
layout: single
title: C++ 문법(1) 참조자
tags: [c++, reference, 참조자]
categories: c++
work: 0
---
# Introduction
C++은 C에서 쓰인 문법들을 거의 계승하나, 몇 가지 새로운 기능이 추가되었다.
C++에서 추가된 참조자(reference)는 특정 변수의 실제 이름 대신 사용할 수 있는 것으로,   
1. 크기가 큰 구조체와 같은 데이터를 함수에 인수할 때
2. 클래스를 설계할 때   

자주 사용된다.

# 참조자의 선언
C++에서 참조자는 다음과 같은 문법으로 선언한다.
```cpp
int {변수이름}; // 변수의 선언
int& {참조자이름} = {변수이름}; // 참조자 선언
```
**&연산자는 주소 연산자가 아닌 타입을 식별하기 위해 사용하는 식별자로 사용**되었다.
int&는 int형 변수에 대한 참조로 쓰인다.

다음과 같은 사항에 유의해야 한다.
1. 참조자의 타입은 대상이 되는 변수의 타입과 일치해야 한다.
2. 참조자는 선언과 동시에 초기화되어야 한다.
3. 참조자는 한 번 초기화되면 참조하는 대상을 변경할 수 없다.

선언된 참조자는 **대상변수와 같은 메모리 위치를** 참조하게 된다.
따라서 참조자를 이용해 연산을 수행하면 참조 변수뿐 아니라 대상 변수도 같이 변경된다.
```cpp
int x = 1;
int& y = x;

cout << "x:" << x << ",y:" << y << endl;
y++;
cout << "x:" << x << ",y:" << y << endl;
cout << "x의 주소값: " << &x << ",y의 주소값 :" << &y;
```

# 인수 전달에서 활용
함수가 **참조자를 인수로 전달받으면, 참조자가 참조하고 있는 실제 변수의 값을 함수 내에서 조작**할 수 있다. (call by reference)
```cpp
void swap(int& x, int& y)
{
 int temp;
 temp = x;
 x = y;
 y = temp;
}
int main(void)
{
  int a = 1, b = 7;
  cout << a << " and " << b << endl;
  swap(a, b);
  cout << a << " and " << b << endl;
  return 0;
}
```
참조에 의한 전달은 기존의 포인터를 사용해도 똑같은 결과를 얻을 수 있다.   
주의할 것은 보통 인자로 값에 의한 전달을 사용하는 경우가 많기 때문에 크기가 큰 구조체나 클래스와 같은 경우를 제외하고는 사용하지 않는 것이 좋다.


```cpp
struct Person
{
    string name;
    int age;   
};

void Display(const Person& p)
{
    cout << "name is " << p.name << " and age is " << p.age << endl;
}
 
int main(void)
{
    Person ganada = {"가나다", 20};
    Display(ganada);
    return 0;
}
```
# Discussion
핵심만 정리하자면,
- &는 주소 연산자가 아닌 타입을 식별하기 위해 사용하는 식별자로 사용.
- 참조자를 인수로 전달받으면, 참조자가 참조하고 있는 실제 변수의 값을 함수 내에서 조작이 가능함.
- 참조자는 포인터처럼 call by reference 용으로 쓸 수 있으나, 구조체나 클래스를 다룰 때만 사용하는 것이 좋음.

# Reference
[TCP School 강의문서](http://www.tcpschool.com/cpp/cpp_intro_iostream)  
