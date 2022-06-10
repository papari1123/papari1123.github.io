---
layout: single
title: f-string을 이용한 문자열 표현
tags: [f-string, Literal String Interpolation]
categories: python
---

F-string은 문자열에 f또는 F 접두어를 붙이고 표현식을 {expression} 형태로 작성해
문자열에 파이썬 표현식의 값을 그대로 삽입할 수 있도록 한다.

아래 예시처럼, 선택 포맷 지정자가 표현식 뒤에 올 수 있다.
```python
from math import pi
print(f"Pi is approximately {pi:.3f}.")
# out: Pi is approximately 3.142.
table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
```
열을 맞출 때, f-string 표현식 뒤에 정수를 전달하면 필드의 최소 문자 폭을 맞출 수 있다. 
(0을 앞에 원하는 만큼 채워야 하는 경우에는 f-string과 별개로 str.zfill을 사용한다.)
```python
for name, phone in table.items():
    print(f'{name:10} ==> {phone:10d}')

""" 
out:
Sjoerd     ==>       4127
Jack       ==>       4098
Dcab       ==>       7678
"""
```
f-string을 사용하면 위치 지정자 중괄호 안에 완전한 파이썬 식을 넣을 수 있다.
값을 약간 변경하고 싶을 때도 간결한 구문으로 표기가 가능하고, 여러 줄이 필요한 형식화를 한 줄로 해결할 수 있다.
```python
places = 5
i, j = 1.245, 3.754
print(f'{i+j} = {i:.{places}f} + {j:.{places}f}, max between {i} and {j} is {max(i, j)}')
```




## @ 참고
[PEP 문서](https://peps.python.org/pep-0498/)  
[7.1.1 포맷 문자열 리터럴](https://docs.python.org/ko/3/tutorial/inputoutput.html)   
[포맷 문자열의 명세 방법](https://docs.python.org/ko/3/library/string.html#formatspec)