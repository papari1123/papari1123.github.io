---
layout: single
title: Transformer
tags: [Transformer]
categories: ml_basic
---
# Introduction
이미지는 

# Pre-question
- attention 모듈이 추가되면서 Seq2Seq이 변경되는 점은 뭘까
-

- 
- 
# 어텐션 구조
attention 스코어가 나옴.

![](./../../../assets/images/(TODO)2022-10-13-Attention_images/1665635264936.png)

decoder의 마지막 timestep에서 출력되는 output vector를 복사해 encoder에서 출력되는 output vector의 내적을 구한다.
= attention score
- attention distribution을 알기 위해 softmax를 적용한다.

장점
- 전단계에서 추론을 잘못해도 괜차늠 encoder에 의한 attention 때문

**Teacher forcing**
매 timestep마다 GT를 넣어서 학습하는 방식.
학습이 좀 더 빠르고 용이. 그러나, test 환경과 다름.

Teacher forcing아 이닌 경우 : 
GT를 매 timestep마다 넣어주는 것이 아니라, 실제 예측값을 넣는 경우.

둘을 결합한 방법도 있음.

$h_t$ 디코도에서 주어지는 히튼 스테이트
인코더 단에서 각 워드별 히든 스테이트

의 유사도를 구하기 위해 
1. 그냥 내적을 구하거나,
2. generalize dot product (htWahs)를 할 수 있다.
![](./../../../assets/images/(TODO)2022-10-13-Attention_images/1665636621115.png)
이 가운데 들어가는 행렬은 Wb
내적보다 조금 더 복잡하게, 좀 더 일반화된 곱.
3. 

# Reference
- 네이버 AI 부트캠프 (* 강의 자료 바탕으로 재구성)   
