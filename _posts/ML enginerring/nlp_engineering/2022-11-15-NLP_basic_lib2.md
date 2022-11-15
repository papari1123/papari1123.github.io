---
layout: single
title: 한국어 텍스트 전처리 활용 (filtering)
tags: [NLP, filtering]
categories: nlp_engineering
---
# Introduction
- 이전 포스팅에서 텍스트 전처리 라이브러리 사용법을 익혔다. 
- 이번 포스팅에서는 라이브러리 기능보다는, **nlp 모델 성능을 높이기 위해 필요한 텍스트 전처리(필터링) 방법들**에 대해 서술한다.
- 이전 포스팅과 일부 겹치는 내용이 있을 수 있고, 부실하게 정리된 내용이 있을 수 있으나 계속 다듬을 예정.

# Pre-question
- 모델 성능을 높이기 위해 nlp 데이터 전처리 관점에서 어떤 것을 해야할까?

# 1. 맞춤법 정리
- hanspell을 사용해 맞춤법이 틀린 문장들을 교정한다.

```python
!pip install git+https://github.com/ssut/py-hanspell.git

from hanspell import spell_checker
 
sent = "무엇이 않뒈는지 체크를해줘"
spelled_sent = spell_checker.check(sent)
print(spelled_sent)
checked_sent = spelled_sent.checked 
print(checked_sent)

>>> Checked(result=True, original='무엇이 않뒈는지 체크를해줘', checked='무엇이 않데는 지 체크를 해줘', errors=2, words=OrderedDict([('무엇이', 0), ('않데는', 4), ('지', 4), ('체크를', 2), ('해줘', 2)]), time=0.7035374641418457)
>>> 무엇이 않데는 지 체크를 해줘
```


# 2. 문제를 일으킬 수 있는 문자들을 제거.
- 여기 제시된 문자들은 성능 문제 이외에도, 모델 코드에 따라 런타임 에러를 발생시킬수도 있다.
  - "\u200b", "…", "\ufeff"와 같은 문자들을 제거한다.
  - text = re.sub(r"[\+á?\xc3\xa1]", "", text)를 사용한다.

# 3. 의미가 없는 기호 제거, 변환
- 문장 내에서 의미가 없는 기호를 제거한다. 이런 기호들은 크롤링 과정에서 부산물로도 발생할 수 있다.
  - 수학(,) -> 수학

# 4. 중구난방으로 표현된 수식 등 통일
- 수식을 표현하는 방법이 다양한데, 그대로 두면 같은 의미를 가진 수식도 다른 토큰으로 치환될 수 있다.

```python
punct_mapping = {"‘": "'", "₹": "e", "´": "'", "°": "", "€": "e", "™": "tm", "√": " sqrt ", "×": "x", "²": "2", "—": "-", "–": "-", "’": "'", "_": "-", "`": "'", '“': '"', '”': '"', '“': '"', "£": "e", '∞': 'infinity', 'θ': 'theta', '÷': '/', 'α': 'alpha', '•': '.', 'à': 'a', '−': '-', 'β': 'beta', '∅': '', '³': '3', 'π': 'pi', }
for p in punct_mapping:
    text = text.replace(p, punct_mapping[p])
```

# 5. 중복 제거
- 중복으로 쓰인 띄어쓰기를 제거한다.

```python
text = "하늘이    매우  맑다."
text = re.sub(r"\s+", " ", text).strip()
>>> 하늘이 매우 맑다.
```

- 문장도 제거할 수 있음.
- 
```python
from collections import OrderedDict
texts = list(OrderedDict.fromkeys(texts))
```

## 6. 띄어쓰기 보정
- pykospacing은 띄어쓰기가 잘못된 문장을 보정한다.
- 띄어쓰기가 잘못 추가된 걸 보정하지는 못하는 듯하다.

```python
!pip install git+https://github.com/haven-jeon/PyKoSpacing.git

from pykospacing import Spacing

text = "나는밥을맛있게 먹 고싶다"
spacing = Spacing()
text = spacing(text)
print(text)

>>> 나는 밥을 맛있게 먹 고 싶다
```

## 7. 품사에 따른 문장 필터링
- koNLpy를 이용해 문장 내 품사를 분석하고, 명사(NN), 동사(V), 형용사(J) 포함 여부에 따라 문장을 필터링 할 수 있다.
- 특히 mecab 토크나이저는 다른 토크나이저와 비교할 때, 처리속도 뿐 아니라 다양한 품사를 다루기 때문에 주로 사용된다.

```python
!bash <(curl -s https://raw.githubusercontent.com/konlpy/konlpy/master/scripts/mecab.sh)

from konlpy.tag import Mecab

NN_TAGS = ["NNG", "NNP", "NNB", "NP"]
V_TAGS = ["VV", "VA", "VX", "VCP", "VCN", "XSN", "XSA", "XSV"]
J_TAGS = ["JKS", "J", "JO", "JK", "JKC", "JKG", "JKB", "JKV", "JKQ", "JX", "JC", "JKI", "JKO", "JKM", "ETM"]
    
mecab = Mecab()
answer = []

text = "어머니가 장을 보고 오신다."
morphs = mecab.pos(text, join=False)
nn_flag, v_flag, j_flag = False, False, False
for morph in morphs:
    pos_tags = morph[1].split("+")
    for pos_tag in pos_tags:
        if not nn_flag and pos_tag in NN_TAGS:
            nn_flag = True
        if not v_flag and pos_tag in V_TAGS:
            v_flag = True
        if not j_flag and pos_tag in J_TAGS:
            j_flag = True
    if nn_flag and v_flag and j_flag:
        answer.append(text)
        break
```

## 8. 불용어 필터링

## 9. 최대/최소 길이 필터링


# Reference
- 네이버 AI 부트캠프 (* 강의 자료 바탕으로 재구성)
