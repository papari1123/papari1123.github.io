---
layout: single
title: 한국어 정보처리를 위한 파이썬 패키지 (Konlpy)
tags: [NLP, Konlpy]
categories: nlp_engineering
---
# Introduction
한국어 데이터를 처리하기 위한 파이썬 패키지로 Konlpy가 있다.   
※ Konlpy는 사용하면서, 포스팅 내용을 단계적으로 구체화하고 내용을 늘려나갈 예정이다.


# konlpy
Konlpy는 품사 분석을 위한 다음과 같은 모듈을 제공한다. 모듈마다 비슷한 기능을 제공하나,
품사 태그나 실행 시간, 그리고 정확성에 차이가 있다.

  - Kkma
  - Komoran
  - Hannanum
  - Okt
  - Mecab

아래 명령어로 설치할 수 있다.
```python
!pip install konlpy
```

## konlpy.tag
문장 데이터의 토큰을 얻기 위한 토큰화기이다. 아래와 같이 사용할 수 있다.
```python
from konlpy import tag 

sentence = "오늘은 아침을 굶었다."
tokenizer = tag.Okt()

tokens = tokenizer.morphs(sentence)
print(tokens)

>>> ['오늘', '은', '아침', '을', '굶었다', '.']
```

예시에서 사용한 Okt 클래스에 대한 설명이다.
> Open Korean Text is an open source Korean tokenizer written in Scala, developed by Will Hohyon Ryu.

Okt과 비슷한 모듈로 Hannanum이라는 모듈도 제공된다. 아래와 같은 기능을 가지고 있다.
```python
from konlpy.tag import Hannanum
hannanum = Hannanum()
text = '안녕하세요, 좋은 아침입니다!'
print(hannanum.morphs(text))  # 형태소 분석 
print(hannanum.nouns(text))   # 명사만 뽑기
print(hannanum.pos(text))     # 품사 태깅

>>> ['안녕', '하', '세', '요', ',', '좋', '은', '아침', '이', 'ㅂ니다', '!']
>>> ['안녕', '아침']
>>> [('안녕', 'N'), ('하', 'X'), ('세', 'E'), ('요', 'J'), (',', 'S'), ('좋', 'P'), ('은', 'E'), ('아침', 'N'), ('이', 'J'), ('ㅂ니다', 'E'), ('!', 'S')]
```

# Discussion
- 패키지 제작자는 KoNlpy를 사용하면서 아래 3가지 철학을 가지고 개발을 진행했다고 한다. 
이런 대규모 오픈소스를 설계한면 자신만의 확고한 철학이 있어야겠다. 
  - 사용법이 간단해야 한다.
  - 누구나 쉽게 이용할 수 있어야 한다.
  - “인터넷 민주주의는 효과적이다.”
- 아직 사용을 많이 해보진 않았기 때문에, 좀더 써보고 후기를 작성 예정이다.

# Reference
- 네이버 AI 부트캠프 (* 강의 자료 바탕으로 재구성)
- [공식문서](https://konlpy.org/ko/latest/index.html)