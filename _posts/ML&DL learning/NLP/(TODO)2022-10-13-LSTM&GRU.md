---
layout: post
title: paper-review-template
subtitle: pape-review
cover-img: /assets/img/path.jpg
thumbnail-img: /assets/img/thumb.png
share-img: /assets/img/path.jpg
tags: [paper-review]
---
# Paper Title


## Keyword


## After review


# Introduction

각각의 단어를 특정 벡터로 표현하기 위한 워드 임베딩에 대해 배워본다.


의미가 비슷한 love, like는 워드 임베딩에서 유사한 벡터값을 가지게 된다.
-> 분류 문제에서 잘 분류하게 됨.


# Pre-question


# Word2Vec
같은 문장에서 나타난 인접 단어는 비슷한 의미를 가진다.
예를 들어 문장 내 cat이 있을 때 주변단어를 보면 주변단어와의 연관성을 알 수 있다.

![](./../../../assets/images/(TODO)2022-10-05-paper_nlp_images/1665541255437.png)

window 사이즈 결정. window범위 내에서 단어 쌍을 구성.
V는 문장의 단어 수, N은 임베딩 차원 수이다.
W1은 입력, W2는 출력으로 쓴다.
![](./../../../assets/images/(TODO)2022-10-05-paper_nlp_images/1665541313068.png)
 

![](./../../../assets/images/(TODO)2022-10-05-paper_nlp_images/1665543039374.png)

Glove
: 차이는 각 입출력 단어 쌍에 대해
몇번 등장했는지 사전에 계산하고, 입력 워드의 vi 출력 워드의 vj
한 window 내에서 총 몇 번 나오나
viTvj가 logPij와 비슷하게 나오도록 학습한다.

애초에 동시에 등장하는 값(P)을 미리 계산 -> 로그 -> 내적값의 ground th로 써서
중복되는 데이터를 줄여준다.


