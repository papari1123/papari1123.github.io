---
layout: single
title: 한국어 텍스트 전처리 라이브러리 사용법
tags: [NLP, Konlpy, Re, Article, soynlp]
categories: nlp_engineering
---
# Introduction
한국어 데이터를 처리하기 위한 파이썬 패키지가 매우 다양하다.
이 포스팅에서는 유용하게 사용가능한 한국어 데이터 전처리 파이썬 패키지를 소개한다.
- re : 정규화식을 이용한 전처리, -> 기본 사용법은 파이썬 라이브러리 포스팅에서 다뤘음.
- Konlpy : 품사 분석을 위한 모듈 제공
- Article : 뉴스 기사에서 유의미한 텍스트 추출을 위한 모듈 (다국어 지원)
- soynlp : 반복되는 문자에 대해 압축을 지원

# Pre-question
- 한국어 데이터를 전처리하기 위해 자주 사용되는 라이브러리는 어떤 것이 있고, 어떤 기능을 가질까?
- 비슷한 다른 라이브러리와 차별성은?


# Re
- 가장 많이 쓰일 Re 라이브러리는 파이선 라이브러리 포스팅에 기본 문법을 정리하였다.
- 여기서는 응용 방법만 서술함.

## 태그 제거
- +는 앞의 문자가 1개 이상인 패턴을 매칭한다.
- []는 []안의 문자를 포함한 패턴을 매칭, 단 ^가 앞에 있다면 []내부를 예외로 둔다.
- ?는 바로 앞의 문자가 있거나 또는 없는 모든 경우에 대해 패턴 매칭한다.
```python
text = "<br>이것은 테스트 문장</br> 입니다."
text = re.sub(r"<[^>]+>\s+(?=<)|<[^>]+>", "", text).strip()
print(text)

>>> 이것은 테스트 문장 입니다.
```
## 이메일 제거
```python
text = "제 아이디는 test3@gmail.com입니다."
text = re.sub(r"[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+", "#email", text).strip()
print(text)

>>> 제 아이디는 #email입니다.
```
## hash tag, mention 제거
- \S는 white space를 제외한 모든 문자를 매칭한다.
- +는 앞문자가 1개 이상 반복될 때 매칭한다.
- \w는 white space를 제외한 모든 숫자와 문자를 매칭한다.
```python
text = "@고기1맛있다님, 와 이건 정말 #대박상품 이네요"
text = re.sub(r"#\S+", "", text).strip() # 
print(text)
text = re.sub(r"@\w+", "", text).strip() # 
print(text)

>>> @고기1맛있다님, 와 이건 정말  이네요
>>> , 와 이건 정말  이네요
```

## url 제거
- ()는 그룹 매칭을 위한 메타문자이다.
```python
text = "네이버 주소는 https://naver.com 이다."
text = re.sub(r"(http|https)?:\/\/\S+\b|www\.(\w+\.)+\S*", "", text).strip()
text = re.sub(r"pic\.(\w+\.)+\S*", "", text).strip()
print(text)

>>> 네이버 주소는 이다.
```

## bad char 제거
- 한국어 데이터를 크롤링하면 알 수 없는 문자가 들어오는데, 이런 것들을 제거하기 사용할 수 있음.
```python
def remove_bad_char(texts):
    bad_chars = {"\u200b": "", "…": " ... ", "\ufeff": ""}
    preprcessed_text = []
    for text in texts:
        for bad_char in bad_chars:
            text = text.replace(bad_char, bad_chars[bad_char])
        text = re.sub(r"[\+á?\xc3\xa1]", "", text)
        if text:
            preprcessed_text.append(text)
    return preprcessed_text

sents = remove_bad_char(sents)
for i, sent in enumerate(sents):
    print(i, sent)
```

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

다양한 토크나이저를 지원한다.
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

## KoNlpy TMI
- 패키지 제작자는 KoNlpy를 사용하면서 아래 3가지 철학을 가지고 개발을 진행했다고 한다. 
이런 대규모 오픈소스를 설계한면 자신만의 확고한 철학이 있어야겠다. 
  - 사용법이 간단해야 한다.
  - 누구나 쉽게 이용할 수 있어야 한다.
  - “인터넷 민주주의는 효과적이다.”
- 아직 사용을 많이 해보진 않았기 때문에, 좀더 써보고 후기를 작성 예정이다.


# Article
- 뉴스 기사를 크롤링하기 위한 라이브러리이다.
- 아래 명령어로 설치를 진행한다.
```python
!pip install newspaper3k

import newspaper
newspaper.languages()
```

## 사용법
Article 모듈을 임포트하고 기사링크로 article 인스턴스를 만들어 파싱하면 된다.
```python
from newspaper import Article # 모듈 임포트

news_url = "https://www.yna.co.kr/view/AKR20221115041453001?section=politics/all1"
article = Article(news_url, language='ko') 

article.download()
article.parse()

print('title:', article.title)
print('context:', article.text)

>>> title: 尹대통령·시진핑, 오늘 발리서 첫 대좌…3년만 한중정상회담(종합)
>>> context: 한중 정상, G20 참석차 발리 방문…北도발·인태전략·한한령 등 논의될 듯
>>> 윤석열 대통령(왼쪽) -시진핑 중국 국가주석 [신화=연합뉴스 자료사진]
```

# soynlp
- 'ㅋㅋㅋ', 'ㅋㅋㅋㅋ', 'ㅋㅋㅋㅋㅋㅋ'이 모두 다른 의미로 학습될 수 있다.
- soynlp를 사용해 이를 하나의 표현으로 전처리할 수 있다.

```python
pip install soynlp

from soynlp.normalizer import *
print(repeat_normalize('훗후후후후훗훗훗훗훗', num_repeats=2))

>>> 훗후후훗훗
```



# 기타 라이브러리
- 유용하지만 시간관계 상 자세히 다루지 않은 라이브러리를 서술한다.

## Khaiii
Khaiii는 카카오에서 만든 형태소 분석기이다. 그러나 통계 기반이 아니라
CNN 기반으로 만들어진 오픈소스이다. 전처리는 전체 프로세스에서 많은 시간을 차지하면 안되므로
당시 NLP에서 많이 쓰이는 LSTM, GRU를 쓰지 않고 CNN을 C로 구현해 모델링을 하였다.    
[공식링크](https://github.com/kakao/khaiii)    
[모델링크](https://github.com/kakao/khaiii/wiki/CNN-%EB%AA%A8%EB%8D%B8)    

## PyKoSpacing
- 띄어쓰기를 위한 전처리 모듈

## Py-Hanspell
- 맞춤법 교정

## kss 
문장 단위로 모델이 학습하기 위해 사용할 수 있는 모듈이다.

# Reference
- 네이버 AI 부트캠프 (* 강의 자료 바탕으로 재구성)
- [공식문서](https://konlpy.org/ko/latest/index.html)