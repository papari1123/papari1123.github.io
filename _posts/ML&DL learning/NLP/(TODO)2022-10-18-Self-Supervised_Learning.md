---
layout: single
title: Semi-Supervised Learning 소개
tags: [NLP]
categories: nlp
---
# Introduction


# Pre-question
Representation Learning이 뭘까?

데이터 -> 옛날에는 전통적으로 

데이터가 폭발하고 있다.

인간의 인지 영역 : 마음만 먹으면 문명의 이기로 인해
소싱가능한 데이터가 많이 있다 -> 이 데이터로 의사결정을 할 수 있다.

그러나 내 주변에는 회색영역이 있다. -> AI로 해결한다.

Human History
-> Symbol History

CH4+2O2 =-> 2H2O _ CO2
: 어떤 물질이 만나면 이런 물질이 생기는 구나! > 정교한 틀
=> Symbol history

과거에는 세상을 기호로 바라보았다.

기호로 표현하는 세상은, 기호가 없으면 그 데이터를 표현할 방법이 없다.

사다리, 우리는 알고 있다.

그런데 뭐냐고 설명할거냐

Symbol : 두 개의 축으로 이루어져 있고, 사람이 올라가고 내려갈 수 있는 구조다.

이런 심볼을 기계에게 어떻게 넣어줄 것인가.

최근의 방법 : 사다리에 구멍을 뚫어본다.

기계에게 한 문장에서 

Representation Learning
: 어떻게 인지시켜줄거냐?


우리의 뇌가 종합적으로 내용을 이해한다.

현실을 센싱한다.
__
사과를 인지할 때, 사과의 특징은 무엇인가 생각하고
나열함. key-value
- color : 빨강
- flavor : 향긋

기계는 숫자 임베딩된 벡터로 셜명

Self-Supervised Learning


예전에는 task 기준 , 아키텍쳐 기준으로 설계한다.

이제는 모델을 large scale로 가고, large raw 데이터를 가져가서
학습시킨다. (2017~~~~)

Easy & Free Task
: Large-scale data
: Efficient task
: Way of Human Learning -> 정답이 있는 문제집만 가지고 풀지는 않는다.


![](./../../../assets/images/(TODO)2022-10-18-Self-Supervised_Learning_images/1666773367337.png)


AutoEncoder : 데이터를 저차원으로 compact하게 만든다. => 컴팩트한 representation

Denosing AUTO Encoder
: 노이즈를 가한다.
: encoder 후 decoder, 라벨은 원래 이미지로
-> 노이즈가 없는 데이터보다 더 성능이 올라가더라

이렇게 얻으려면 모델은 원래 이미지의 본질에 더 가까워야 할 것이다.


Contrastive loss


![](./../../../assets/images/(TODO)2022-10-18-Self-Supervised_Learning_images/1666773841561.png)

가운데 이미지랑 특정 이미지 던져주고, 그 이미지가 어디 붙어있는지 이해할 수 있다.
귀가 어디달렸는지 알 수 있다.
![](./../../../assets/images/(TODO)2022-10-18-Self-Supervised_Learning_images/1666773957466.png)

![](./../../../assets/images/(TODO)2022-10-18-Self-Supervised_Learning_images/1666774081276.png)

# Discussion


# Reference
- 네이버 AI 부트 (* 강의 자료 바탕으로 재구성)
