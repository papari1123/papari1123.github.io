---
layout: single
title: python의 예외처리 (try-except, assert)
tags: [try-except, assert, 예외처리, python]
categories: python
---

try-except는 파이썬 예외 처리 시 사용할 수 있다.    
## try-except의 예외 처리를 위한 분기
```python
try: 
    # 실행내용
    raise Exception("에러테스트") # 에러 발생시키기
except:
    # 에러 발생 시 분기
else : 
    # 예외가 발생하지 않았을 때 분기
finally:
    # 예외와 상관없이 실행
```
  
  
## 예외 만들기
Exception을 상속해 만들 수 있다.
```python
class CustomException(Exception):
    def __init__(self):
        super().__init__('error message')
```
  
## 예외 발생시키기 
python에서 에러를 발생시키는 방법은 대표적으로 raise와 assert가 있다.
### raise
프로그래머가 지정한 예외를 발생하도록 강제한다. raise 다음 임의로 발생시킬 에외를 정할 수 있다. 예외가 발생했지만 처리하고 싶지 않으면 raise 다음을 비워두는 것도 가능하다.

```python
>>> raise NameError('Hi There')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: HiThere
```
### assert
assert는 가정 설정문이라고 하여, assert 뒤의 조건이 True가 아니면 AssertError를 발생한다.
개발자가 프로그램을 디버깅할 때 특정 조건이 나올 때까지 계속 테스트할 수 있도록 만들어 줄 때도 쓰인다.
```python
# assert 조건, '메세지' 로 쓸 수 있고 메세지는 생략가능하다.
>>> assert type(num) is int, f'{num} is not int type.'
#결과
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AssertionError
```

## 예외 상황을 이용한 디버깅 메세지 출력
예외처리 시, 에러가 발생한 파일명과 라인 번호, 에러 내용을 출력하고 싶으면 아래를 참고한다.
```python
try:
    raise TypeError("Hello, World!")  # line 2
except Exception as e:
    print(
        type(e).__name__,          # TypeError
        __file__,                  # /tmp/example.py
        e.__traceback__.tb_lineno,
        e
    )
```

## @ 참고
[에러와 처리 방법에 대한 공식 문서](https://docs.python.org/ko/3/tutorial/errors.html)