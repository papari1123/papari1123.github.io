---
layout: single
title: (8) Optimization
tags: [deep learning, Optimization]
categories: ml_basic
---

# Introduction
언어라는 것은 잘못된 understanding의 원인이다.

용어를 제대로 통일하지 않으면 문제가 생길 거다.



# Pre-question
- Cross-Validation을 하기 위해서는 어떤 방법들이 존재할까?
- Time series의 경우 일반적인 K-fold CV를 사용해도 될까?


![](./../../../assets/images/(TODO)2022-10-04-optimization_images/1664850540882.png)



![](./../../../assets/images/(TODO)2022-10-04-optimization_images/1664850595713.png)
학습된 데이터

![](./../../../assets/images/(TODO)2022-10-04-optimization_images/1664850702913.png)

bias, 
variance

![](./../../../assets/images/(TODO)2022-10-04-optimization_images/1664850870905.png)

cost를 최소호한다는 것은 bias 제곱과 variance, noise를 최소화한다는 것이다.
![](./../../../assets/images/(TODO)2022-10-04-optimization_images/1664850995898.png)

![](./../../../assets/images/(TODO)2022-10-04-optimization_images/1664851090691.png)
몇개의 샘플만 뽑고 그 결과를 봄. 이 과정을 반복해서 나온 결과들이 일치하는지 확인.

모델들이 예측한 값의 
uncertainity

서브 샘플링을 통해 여러 모델들을 만들고 메트릭을 만들어 뭘 하겠다..

![](./../../../assets/images/(TODO)2022-10-04-optimization_images/1664851283084.png)
bagging 부스트래핑을 통해 여러 모델들을 만들고 그 결과를 평균내겠다. (앙상블과 비슷한 의미)

80% 데이터로 N의 모델을 만들어보는게 더 나은 성능을 낼 수 있다.


![](./../../../assets/images/(TODO)2022-10-04-optimization_images/1664851366020.png)
데이터 100개 중에 80갠 잘 예측하고, 20개는 못 예측한다면
그 20개 데이터를 잘 예측하는 모델 B를 만들고, 이것들을 합친다.

![](./../../../assets/images/(TODO)2022-10-04-optimization_images/1664851528470.png)

![](./../../../assets/images/(TODO)2022-10-04-optimization_images/1664851564114.png)

![](./../../../assets/images/(TODO)2022-10-04-optimization_images/1664851572386.png)

Sharp보단 flat minimumm 도달이 낫다.
![](./../../../assets/images/(TODO)2022-10-04-optimization_images/1664851711497.png)

![](./../../../assets/images/(TODO)2022-10-04-optimization_images/1664851742495.png)


![](./../../../assets/images/(TODO)2022-10-04-optimization_images/1664851870838.png)

![](./../../../assets/images/(TODO)2022-10-04-optimization_images/1664852032301.png)

이전 움직임(at)을 다음 번에도 활용한다. 베타는 모멘텀
기존 gradient의 움직임을 유지하기 때문에, 좀 gradient descent가 흔들려도 
![](./../../../assets/images/(TODO)2022-10-04-optimization_images/1664851948727.png)
얘는 한번 이동해, 현재 정보로 한번 이동한 후 계산한걸 가지고 축적
![](./../../../assets/images/(TODO)2022-10-04-optimization_images/1664852132001.png)

모멘텀을 관성이라고 생각하며느,
local minimum을 지나서 슬로프 반대편에서 올라갔다가 다시 원래 위치로 갔다가..
local minimum으로 도달하지 못하는 문제가 있다.

nesterov는 한번 지나간 그 점에서 그레디언트를 계산함
![](./../../../assets/images/(TODO)2022-10-04-optimization_images/1664852190970.png)

뉴럴 넷이 얼마나 변화했는지 확인

많이 변한건 적게 변화시키고
적게 변화된 건 많이 변화시킴

변화정도는 아래 Gt임
![](./../../../assets/images/(TODO)2022-10-04-optimization_images/1664852358838.png)
G는 누적되니깐..
G가 무한대면 w항이 업데이트가 거의 안되겠지
LRAGE g가 커지는 걸 막겠다.

![](./../../../assets/images/(TODO)2022-10-04-optimization_images/1664852394724.png)
근데 t가 time-window를 너무 길게 가져가면 GPT-3같이 파라미터 많은
모델은 터질거니깐, t를 최대한 적게 가져갈 수 있도록 moving averaging 방법 사용

montotonically decresing -> Ht-1 + epliron 텀으로 막음
![](./../../../assets/images/(TODO)2022-10-04-optimization_images/1664857619522.png)

![](./../../../assets/images/(TODO)2022-10-04-optimization_images/1664857630830.png)

![](./../../../assets/images/(TODO)2022-10-04-optimization_images/1664857717446.png)
아래 텀은 중요하진 않은데, unbiased estimator가 되기 위해서.. 넣은 것
![](./../../../assets/images/(TODO)2022-10-04-optimization_images/1664857804270.png)

구현할 필욘 없다.

학습을 방해하는 것. 어떻게 목적에 맞게..


![](./../../../assets/images/(TODO)2022-10-04-optimization_images/1664857883346.png)


![](./../../../assets/images/(TODO)2022-10-04-optimization_images/1664857966735.png)

loss cost에 w를 넣는다.
![](./../../../assets/images/(TODO)2022-10-04-optimization_images/1664857999727.png)

데이터셋이 적다.. 면

![](./../../../assets/images/(TODO)2022-10-04-optimization_images/1664858083928.png)

weight에도 노이즈를 넣는다.
![](./../../../assets/images/(TODO)2022-10-04-optimization_images/1664858199341.png)


![](./../../../assets/images/(TODO)2022-10-04-optimization_images/1664858328557.png)

![](./../../../assets/images/(TODO)2022-10-04-optimization_images/1664858417593.png)

batch normalization
internal covariate shift > 논란 용어

; 적용하려는 레이어의 통계량을 정규화한다.
![](./../../../assets/images/(TODO)2022-10-04-optimization_images/1664858454387.png)

각각의 레이어가 1000개의 파라미터로 구성되어 있다.
각 파라미터의 값이 mean = 0, stand = 1

![](./../../../assets/images/(TODO)2022-10-04-optimization_images/1664858687768.png)


# Discussion


# Summary




# Reference
- 네이버 AI 부트캠프 (* 강의 자료 바탕으로 재구성)     