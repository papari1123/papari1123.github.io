---
layout: single
title: Generative vs Discriminative 
tags: [Generative, Discriminative]
categories: ml_basic
---
# Introduction



# Pre-question
=
Discriminate : classifier
Generative : 단어를 하나하나 생성하는 것,

좀 더 설명하자면,
discriminative model : 조건부 확률에 의해 unseen data에 대한 예측을 수행한다. X, Y를 각각 입출력이라고 하면 P(Y|X)가 일련의 함수로 구해질 수 있다고 가정하고, 이 함수에 대한 파라미터를 학습데이터(XY pair)에 의해 구하는 것이다. 함수는 당연히 P(Y|X)가 최대화되도록 파라미터가 정해질 것이다.
classificication 문제나 regression 문제에 주로 사용된다. 지도학습에 주로 사용하는 방법이라고도 할 수 있음.

generative model : 데이터의 분포에 초점을 맞춰, 주어진 샘플이 관측될 확률을 구한다. 
 generative model도 궁극적으로 P(Y|X)를 구하는 걸 목표로 한다. 대신 관점이 다른데, P(Y|X)는 베이즈 룰에 따라 P(Y)P(X|Y)=P(X, Y)에 비례하기 때문에, P(X, Y)를 구하는 문제로 환원할 수 있다. 
이는 XY페어의 확률 분포를 의미하며, 새로운 XY 페어 데이터(모집단에서 추출한, 기존에 없던 데이터)에 대한 확률을 구한다고도 볼 수 있다. 가장 확률이 크게 나온 XY 페어는 가장 관측이 잘되는 샘플=새로 생성(실제로는 분포를 알 수 없는 모집단에서 추출한다고 불 수 있는)하기 가장 합당한 데이터가 된다. 이 때문에 비지도학습에 주로 사용된다.
https://www.analyticsvidhya.com/blog/2021/07/deep-understanding-of-discriminative-and-generative-models-in-machine-learning/

# Reference
- [Deep Understanding of Discriminative and Generative Models in Machine Learning](https://www.analyticsvidhya.com/blog/2021/07/deep-understanding-of-discriminative-and-generative-models-in-machine-learning/)