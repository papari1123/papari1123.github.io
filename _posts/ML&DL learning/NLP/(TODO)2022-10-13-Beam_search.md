---
layout: single
title: (1) Beam Search and BLEU score
tags: [NLP, Beam Search, BLEU]
categories: nlp
---
# Introduction

# Pre-question
- BLUE의 정의는 무엇이고, 어떤 task에 사용되는가? 단점은?

## Greedy decoding
매 타임스탭마다 확률이 높은 걸 선택해서 Decoding함

예시 : I love you를 번역한다고 하면,
I 다음으로 올, 확률이 가장 높은 워드를 생성,
해당 워드의 다음으로 올 확률이 가장 높은 워드를 생성. 
해서 문장을 생성한다.

이걸 해결하는 법?

Exjaustive search
입력 x라고 하고, y를 출력이라고 해보자.
y1은 출력의 첫 단어이다.
조건부 확률을 이용해 x가 주어졌을 때 y가 나올 확률을 계산할 수 있다.

joint probability
![](./../../../assets/images/(TODO)2022-10-13-Beam_search_images/1665641847384.png)

매우 큰 시간 복잡도

Beam search
Greedy decoding과 exhaustive search의 중간.
![](./../../../assets/images/(TODO)2022-10-13-Beam_search_images/1665641960481.png)
k라는 beam size를 둠.

로그는 단조 증가함수며, 확률값에 로그를 취해주면 음수임.
-> 가장 높은 점수를 픽한다.
![](./../../../assets/images/(TODO)2022-10-13-Beam_search_images/1665642013557.png)

예시 k = 2
![](./../../../assets/images/(TODO)2022-10-13-Beam_search_images/1665642263086.png)

아래 보면 가지를 친다. 
![](./../../../assets/images/(TODO)2022-10-13-Beam_search_images/1665642355245.png)

![](./../../../assets/images/(TODO)2022-10-13-Beam_search_images/1665642375794.png)

## stopping criterion
greedy decoding은 <END> 토큰이 나오면 끝낸다.

beam search decoding은 <END> 토큰이 나온 루트는 끝낸다.

log값(음수)를 계속 더해주기 때문에, 긴 길이의 hypotheses는 낮은 값을 가지게 됨.
![](./../../../assets/images/(TODO)2022-10-13-Beam_search_images/1665642591605.png)

그래서 길이에 대해 normalize하기도 함.

# 평가방법
단어가 밀릴 수도 있다.
![](./../../../assets/images/(TODO)2022-10-13-Beam_search_images/1665642778483.png)

그래서 아래처럼 포함된 단어 개수를 셀수도 있다.
## Precision and Recall
![](./../../../assets/images/(TODO)2022-10-13-Beam_search_images/1665642823849.png)

문제점은 워드의 순서를 지키지 않을 때 생기는 패널티를 고려하지 않는다.
![](./../../../assets/images/(TODO)2022-10-13-Beam_search_images/1665643150923.png)


# BLEU
블루스코어 라고 부르는 BLEU는 n-gram을 사용한다.
uni-gram, bi-gram, tri-gram, four-gram
각 gram마다 계산한 precision을 계산.

![](./../../../assets/images/(TODO)2022-10-13-Beam_search_images/1665643184408.png)
조화평균은 크기가 작은 거에 너무 지나치게 가중치를 줘서, 기하평균을 사용함.

brevity penalty를 통해 recall도 고려한다.

![](./../../../assets/images/(TODO)2022-10-13-Beam_search_images/1665643591163.png)

# Reference

