---
layout: single
title: Transformer
tags: [Transformer]
categories: ml_basic
---
# Introduction
이미지는 

# Pre-question
- 시퀀셜 모델이 겪는 주요 문제는?



어떤 시퀀스가 있다고 할 때,
문장은 항상 길이가 달라질 수 있다.

문장 어순을 좀 바꾸거나, 빠질 수도 있다.
![](./../../../assets/images/(TODO)2022-10-05-Transformer_images/1664944526455.png)

중간에 경로가 바뀐 단어의 경우
이런걸 모델링 하기가 어려워..

기본적으로 self-attention을 사용한다.

![](./../../../assets/images/(TODO)2022-10-05-Transformer_images/1664944582250.png)

트랜스포머는 RNN의 재귀적인 구조가 없다.
attention 구조ㅓ를 활용했다.

기계어 번역에서 처음 트랜스포머가 적용되었다.

시퀀셜 데이터를 인코딩하는 거라..
단순히 

실습에서 트랜스포머를 다룰 거다

제머가 설명한 어텐션과 실습에서 다룬거 달라

시퀀스 투 시퀀스 모델
![](./../../../assets/images/(TODO)2022-10-05-Transformer_images/1664944805770.png)
- 입력과 출력 단위가 다를 수 있군,.
- 인코더는 3개든 100개든 재귀적으로 단어수만큼 안 다뤄

1. n개의 단어가 어떻게 인코더에서 한번에 처리되나
2. 디코더와 인코더 사이에 어떻게 정보가 주고 받나
3. 디코더가 어떻게 generation하나


![](./../../../assets/images/(TODO)2022-10-05-Transformer_images/1664945004323.png)

3개의 벡터가 있다.
![](./../../../assets/images/(TODO)2022-10-05-Transformer_images/1664945039638.png)
3개의 벡터(x1~x3)이 입력으로 들어가 3개의 벡터(z1~z3)를 출력으로 내보낸다.

그런데, z1 출력을 낼 때 x1만 보는 게 아니라 z2~z3도 같이 본다. 이게 self-attention
feed forward는 그냥 같은 뉴런네트워크에 z1을 통과시켜 아웃풋을 내는 것이다.

![](./../../../assets/images/(TODO)2022-10-05-Transformer_images/1664945161439.png)

문장 속에서 단어가 어떤 의미를 가지는지가 중요하다.    

![](./../../../assets/images/(TODO)2022-10-05-Transformer_images/1664945261680.png)

한 단어에 세가지 벡터를 만들어 낸다. Queries, Keys, Values   

![](./../../../assets/images/(TODO)2022-10-05-Transformer_images/1664945337709.png)

 예를 들어 thinking을 임베딩하고 이걸로
score 벡터를 만들어보자.
 인코딩하려는 단어(thinking)의 쿼리 벡터와
나머지 모든 n개 단어의 key 백터를 구하고 이걸 내적해보자..
 (쿼리벡터와 키벡터의 내적)
q1* k1 =, q1*k2 ..

뭘 의미하냐? i번째 단어가 다른 n개의 단어와 얼마나 유사한가.
![](./../../../assets/images/(TODO)2022-10-05-Transformer_images/1664945668160.png)
score 백터 나오면 노멀라이즈 한다. 8로 나눴는데
8은 key벡터와 관련있어
그다음 소프트 맥스를 적용해 .

최종적으로 사용할 것은 value 벡터의 weight sum이다.
![](./../../../assets/images/(TODO)2022-10-05-Transformer_images/1664945907093.png)

쿼리 벡터와 키 벡터는 항상 차원이 같아야 함
하지만 value 벡터는 달라도 돼.

![](./../../../assets/images/(TODO)2022-10-05-Transformer_images/1664946015875.png)
![](./../../../assets/images/(TODO)2022-10-05-Transformer_images/1664946085904.png)

왜 잘될까?
트랜스포머는 
하나의 입력이 고정되었다, 네트워크가 픽스되었따고 해도

인코딩하려는 단어와 그 "옆에 있는 단어들"에 따라서 인코딩된 단어는 달라진다.
즉, 주변 환경을 같이 본다!!!!!!!!
그래서 더 많은 컴퓨테이션이 필요.

네트워크 입력의 일부 dimension이 고정되어있다고 하더라도, 
내가 이 인코딩하려는 단어와 그 옆의 단어에 따라서
인코딩된 단어가 달라질 수 있따.

더 많ㅇ은 걸 표현할 수 있다.

N개의 단어를 처리하려면 N^2만큼 처리해야 함.

N^2이다!!!!

메모리를 많이 먹는다!!

훨씬 더 플랫서블하게 표현 가능한 네트워크다,..

MULTI HEAD ATTENTION(MHA)는 쿼리 키 벨류를 단어당 1개가 아니라 여러개 만드는 거다

![](./../../../assets/images/(TODO)2022-10-05-Transformer_images/1664946517297.png)
여러개의 인코딩된 결과를 내는 것이다..

인코딩 이 쌓여있어서,.. 입력과 출력 차원을 맞춰줘야 하는데 어떻게 해결하나?

입력 단어가 8개고 MHA적용해 10개씩 총 80개의 인코딩된 벡터가 있다고 하자.

이걸 learnable linear map에 적용
![](./../../../assets/images/(TODO)2022-10-05-Transformer_images/1664946613147.png)

근데 이렇게 구현되지 안혹, 실제로는

100개의 dimension을 10개로 나눈다..
-> 실습 때..

왜 positional encoding이 필요할까??
예를 들어 ABCD를 넣든 ACDB를 넣든 인코딩 된 결과는 달라지지 않아
순서에 indenpetned한 attention 연산 구조 때문이다.

따라서 이를 체크하기 위해 postitviaotn encoding이다.

pre-defined 방법으로 postition encoding

최근에는 
![](./../../../assets/images/(TODO)2022-10-05-Transformer_images/1664946783166.png)

그래서 이렇게 z1, zn개의 인코딩된 벡터가 나오면,
add & normalize에서 layer norm을 한다. -> 이거 설명 안함

인코더는 주어진 입력을 설명하는 벡터를 만드는 과정이고,

decoder 쪽은 실제로 생성한다.

![](./../../../assets/images/(TODO)2022-10-05-Transformer_images/1664947204038.png)

뒤에 나올 걸 알 수 없기 때문에 마스킹해서 한다.
![](./../../../assets/images/(TODO)2022-10-05-Transformer_images/1664947355065.png)


![](./../../../assets/images/(TODO)2022-10-05-Transformer_images/1664947510582.png)

![](./../../../assets/images/(TODO)2022-10-05-Transformer_images/1664947538177.png)


![](./../../../assets/images/(TODO)2022-10-05-Transformer_images/1664947621805.png)

# Reference
- 네이버 AI 부트캠프 (* 강의 자료 바탕으로 재구성)   


![](./../../../assets/images/(TODO)2022-10-05-Transformer_images/1665971374670.png)


- Scaled dot attention > Q K dimension 이 커지게 되면, 
softmax 함수의 특성 상 Qkt의 분산이 커지게 된다.
gradient 값이 작아지게 된다.

- 
![](./../../../assets/images/(TODO)2022-10-05-Transformer_images/1665973225431.png)


__8강__

Transformer
- MHA가 필요한 이유는?
어떤 동일한 시퀀스가 주어져도 특정한 쿼리 워드에서 다양한 측면에 대해 정보를 추출해야 함.

- I라는 쿼리 워드에 인코딩을 수행하려면 -> 각 주체가 하는 정보를 뽑아올 수 있다.

learning rate scheduling

![](./../../../assets/images/(TODO)2022-10-05-Transformer_images/1665982084326.png)
