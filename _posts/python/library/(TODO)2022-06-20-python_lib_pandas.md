---
layout: single
title: 데이터 조작 및 분석을 위한 파이썬 라이브러리 (pandas)
tags: [python library, pandas]
categories: python_lib
work: 0 
---

##  Introduction
csv와 2차원 데이터를 다룰 때 주로 사용되는 pandas에 대해 알아보자.
numpy와 보통 같이 쓰기 때문에 numpy도 같이 import 한다.
```python
import numpy as np
import pandas as pd
```
## 객체 생성
### Series
Series를 이용해 아래와 같이 간단한 pandas 객체를 생성할 수 있다.
```python
s = pd.Series([1, 3, 5, np.nan, 6, 8])
s

>>>
0    1.0
1    3.0
2    5.0
3    NaN
4    6.0
5    8.0
dtype: float64
```
### from_dict
dictionary를 이용해 pandas 객체를 생성할 수 있다.
```python
data = {'col_1': [3, 2, 1, 0], 'col_2': ['a', 'b', 'c', 'd']}
pd.DataFrame.from_dict(data)
   col_1 col_2
0      3     a
1      2     b
2      1     c
3      0     d

```


## @참고
[pandas 공식 가이드](https://pandas.pydata.org/docs/user_guide/10min.html)