---
layout: single
title: subword 토큰화
tags: [NLP, ]
categories: nlp_engineering
---
# Introduction

서브워드는 하나의 단어를 여러 개의 단어로 분리했을 때 하나의 단위를 말한다.

캐릭터 임베딩 = 다 공백으로 나눠서 : 이 길이 자체가 너무 길어..!!!

vocab = list(set(chain.from_iterable(corpus) | {WORD_END}))
coupus = [' '.join(word + WORD+END)]


# Reference
- 네이버 AI 부트캠프 (* 강의 자료 바탕으로 재구성)
