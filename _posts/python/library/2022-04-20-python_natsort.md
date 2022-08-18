---
layout: single
title: 숫자를 포함한 파일이름을 naturally하게 정렬하는 라이브러리 (natsort)
tags: [python library, natsort]
categories: python_lib
---

# 모듈 임포트
일반적으로는 모듈 내 natsorted 함수를 주로 사용한다.    
다만 real sort 등 특별한 기준으로 정렬해야 할 경우 다른 함수들을 임포트 해줘야 한다. (포스트 하단 참조)


```python natsorted
```

# 모둘 사용해 정렬
숫자가 포함된 폴더 이름을 정렬 시, 빌트인 정렬 함수처럼 1, 10, 2.. 이런식으로 정렬되지 않고 1,2, .., 10 이렇게 "naturally"하게 정렬된다.

아래는 모듈 설명 :   
When you try to sort a list of strings that contain numbers, the normal python sort algorithm sorts lexicographically, so you might not get the results that you expect:   
```
>>> a = ['2 ft 7 in', '1 ft 5 in', '10 ft 2 in', '2 ft 11 in', '7 ft 6 in']
>>> sorted(a)
['1 ft 5 in', '10 ft 2 in', '2 ft 11 in', '2 ft 7 in', '7 ft 6 in']
```
Notice that it has the order ('1', '10', '2') - this is because the list is being sorted in lexicographical order, which sorts numbers like you would letters (i.e. 'b', 'ba', 'c').       
    
natsort provides a function natsorted that helps sort lists "naturally" ("naturally" is rather ill-defined, but in general it means sorting based on meaning and not computer code point). Using natsorted is simple:     
```
>>> from natsort import natsorted
>>> a = ['2 ft 7 in', '1 ft 5 in', '10 ft 2 in', '2 ft 11 in', '7 ft 6 in']
>>> natsorted(a)
['1 ft 5 in', '2 ft 7 in', '2 ft 11 in', '7 ft 6 in', '10 ft 2 in']
```
natsorted identifies numbers anywhere in a string and sorts them naturally. Below are some other things you can do with natsort (also see the examples for a quick start guide, or the api for complete details).

# 주의할 점
**natsorted를 쓴다고, 마법처럼 내가 원하는대로 정렬된다고 생각하면 안된다**.
예를 들어 다음과 같이 0.mp4부터 22.mp4까지 동영상 파일 경로를 pathlib 인스턴스로 담은 리스트를 만들었다고 하자.
이를 sort하거나, key 파라미터 없이 natsort해도 원하는대로 정렬이 되지 않고, 1-10-11 이런 순으로 정렬된다.
이는 string이 아닌 PosixPath 객체의 특정 어트리뷰트를 기준으로 정렬되어서 그렇다.    
**따라서 key 파라미터에 str을 매개변수로 넣어야 한다.**
```python
from natsort import natsorted
from pathlib import Path

dir_path = Path('./data')

vid_paths = [p for p in dir_path.glob('*.mp4')]

normal_sort = sorted(vid_paths)
natual_sort = natsorted(vid_paths)
natual_str_sort = natsorted(vid_paths, key=str)

print('normal_sort:', normal_sort)
print('natual_sort:', natual_sort)
print('natual_str_sort:', natual_str_sort)

>>>
normal_sort: [PosixPath('/0.mp4'), PosixPath('/1.mp4'), PosixPath('/10.mp4'), PosixPath('/11.mp4'), PosixPath('/12.mp4'), PosixPath('/13.mp4'), PosixPath('/14.mp4'), PosixPath('/15.mp4'), PosixPath('/16.mp4'), PosixPath('/17.mp4'), PosixPath('/18.mp4'), PosixPath('/19.mp4'), PosixPath('/2.mp4'), PosixPath('/20.mp4'), PosixPath('/21.mp4'), PosixPath('/22.mp4'), PosixPath('/3.mp4'), PosixPath('/4.mp4'), PosixPath('/5.mp4'), PosixPath('/6.mp4'), PosixPath('/7.mp4'), PosixPath('/8.mp4'), PosixPath('/9.mp4')]
natual_sort: [PosixPath('/0.mp4'), PosixPath('/1.mp4'), PosixPath('/10.mp4'), PosixPath('/11.mp4'), PosixPath('/12.mp4'), PosixPath('/13.mp4'), PosixPath('/14.mp4'), PosixPath('/15.mp4'), PosixPath('/16.mp4'), PosixPath('/17.mp4'), PosixPath('/18.mp4'), PosixPath('/19.mp4'), PosixPath('/2.mp4'), PosixPath('/20.mp4'), PosixPath('/21.mp4'), PosixPath('/22.mp4'), PosixPath('/3.mp4'), PosixPath('/4.mp4'), PosixPath('/5.mp4'), PosixPath('/6.mp4'), PosixPath('/7.mp4'), PosixPath('/8.mp4'), PosixPath('/9.mp4')]]]
natual_str_sort: [PosixPath('/0.mp4'), PosixPath('/1.mp4'), PosixPath('/2.mp4'), PosixPath('/3.mp4'), PosixPath('/4.mp4'), PosixPath('/5.mp4'), PosixPath('/6.mp4'), PosixPath('/7.mp4'), PosixPath('/8.mp4'), PosixPath('/9.mp4'), PosixPath('/10.mp4'), PosixPath('/11.mp4'), PosixPath('/12.mp4'), PosixPath('/13.mp4'), PosixPath('/14.mp4'), PosixPath('/15.mp4'), PosixPath('/16.mp4'), PosixPath('/17.mp4'), PosixPath('/18.mp4'), PosixPath('/19.mp4'), PosixPath('/20.mp4'), PosixPath('/21.mp4'), PosixPath('/22.mp4')]

```

# Sorting by Real Number (Signed Floats)
음수를 포함한 실수가 이름에 포함될 경우 정렬은 아래와 같이 alg 키워드에 ns.REAL 파라미터를 넣거나,
realsorted를 임포트한다.
```python
>>> from natsort import realsorted, ns
>>> # Note that when interpreting as signed floats, the below numbers are
>>> #            +5.10,                -3.00,            +5.30,              +2.00
>>> a = ['position5.10.data', 'position-3.data', 'position5.3.data', 'position2.data']
>>> natsorted(a)
['position2.data', 'position5.3.data', 'position5.10.data', 'position-3.data']
>>> natsorted(a, alg=ns.REAL)
['position-3.data', 'position2.data', 'position5.10.data', 'position5.3.data']
>>> realsorted(a)  # shortcut for natsorted with alg=ns.REAL
['position-3.data', 'position2.data', 'position5.10.data', 'position5.3.data']
```

# Locale-Aware Sorting (or "Human Sorting")
컴퓨터가 이해하는 아스키코드를 기준으로 정렬하지 않고,
사람이 단어를 정렬할 때 보편적으로 적용하는 기준대로 정렬한다.     
정확히는 영문자는 영문자(**아스키 코드가 아닌 알파벳 순서로 정렬**)대로, **숫자는 숫자대로** 생각해 정렬하고 싶을 경우 locale이나, alg 키워드에 ns.LOCALE 매개변수를 넣는다.
아래 예제를 보면
1. 오름차 순이면 기본 소트는 아스키코드 상 B가 a앞에 와야 하나, 알파벳 순서가 우선 적용되는 기준이므로 humansorted 하면 뒤에 오게 된다.
2. 오름차 순이면 기본 소트는 아스키코드 상 14,689가 15보다 앞에 와야 하나, 숫자가 더 큰 14,689가 포함된 apple14,689가 뒤에 온다.

**기준이 좀 복합적이라 정렬이 원하는대로 되었는지 결과를 반드시 확인하고 써야할 것 같다.**
```python
>>> a = ['Apple', 'apple15', 'Banana', 'apple14,689', 'banana']
>>> natsorted(a)
['Apple', 'Banana', 'apple14,689', 'apple15', 'banana']
>>> import locale
>>> locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')
'en_US.UTF-8'
>>> natsorted(a, alg=ns.LOCALE)
['apple15', 'apple14,689', 'Apple', 'banana', 'Banana']
>>> from natsort import humansorted
>>> humansorted(a)  # shortcut for natsorted with alg=ns.LOCALE
['apple15', 'apple14,689', 'Apple', 'banana', 'Banana']
```

# Reference.
https://github.com/SethMMorton/natsort
