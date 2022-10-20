---
layout: single
title: 한국어 텍스트 전처리 개요
tags: [NLP, Corpus cleaning]
categories: nlp_engineering
---
# Introduction
NLP는 말뭉치를 모델이 효과적으로 학습하기 위해 다양한 전처리 과정이 필요하다.
이번 포스팅에서는
- 한국어 말뭉치 전처리 과정에 필요한 다양한 모듈을 사용해보고,
- 자연어처리 및 다양한 분야에서 많이 쓰이는 정규 표현식도 같이 공부해본다.

# Pre-question
- 한국어 데이터를 전처리하기 위해 자주 사용되는 라이브러리는 어떤 것이 있고, 어떤 기능을 가질까?
- 비슷한 다른 라이브러리와 차별성은?

# koNLPy
koNLPy는 품사를 분석할 때 주로 쓰이는 라이브러리이다. 통계를 기반으로 한 형태소 분석기이다.
```python
from konlpy.tag import Hannanum
hannanum = Hannanum()
text = '안녕하세요, 좋은 아침입니다!'
print(hannanum.morphs(text))  # 형태소 단위
print(hannanum.nouns(text))   # 명사만 추출
print(hannanum.pos(text))     # 품사 태깅

>>> ['안녕', '하', '세', '요', ',', '좋', '은', '아침', '이', 'ㅂ니다', '!']
>>> ['안녕', '아침']
>>> [('안녕', 'N'), ('하', 'X'), ('세', 'E'), ('요', 'J'), (',', 'S'), ('좋', 'P'), ('은', 'E'), ('아침', 'N'), ('이', 'J'), ('ㅂ니다', 'E'), ('!', 'S')]
```

# Khaiii
Khaiii는 카카오에서 만든 형태소 분석기이다. 그러나 통계 기반이 아니라
CNN 기반으로 만들어진 오픈소스이다. 전처리는 전체 프로세스에서 많은 시간을 차지하면 안되므로
당시 NLP에서 많이 쓰이는 LSTM, GRU를 쓰지 않고 CNN을 C로 구현해 모델링을 하였다.    
[공식링크](https://github.com/kakao/khaiii)    
[모델링크](https://github.com/kakao/khaiii/wiki/CNN-%EB%AA%A8%EB%8D%B8)    

# PyKoSpacing
- 띄어쓰기를 위한 전처리 모듈

# Py-Hanspell
- 맞춤법 교정


# Discussion

# Reference
- 네이버 AI 부트캠프 (* 강의 자료 바탕으로 재구성)
- [공식문서](https://konlpy.org/ko/latest/index.html)