---
layout: single
title: Advanced Self-supervised Pre-trained Models
tags: [NLP, GPT-2]
categories: nlp
---
# Introduction

# Pre-question
- ALBERT에서는 어떤 방법으로 모델을 경량화시켰을까?


GPT-2
: 더 큰 transformer기반  Language model


- 파라미터나 구조 변경없이도. LM이 down-stream task를 zero-shot seetting을 가능하게 한다.
- GPT1의 다양한 NLP task를 QA(Question Answering)로 통합했는데 예를 들면,    
   - 긍부정 분류: ‘Is this sentence positive or negative?’,     
   - 요약: ‘What is the summarization of this paragraph?’

 

# 참고 : 업스트림과 다운스트림
그림2의 Task1은 업스트림(upstream) 태스크라고 부르고 Task2는 이와 대비된 개념으로 다운스트림(downstream) 태스크라고 부릅니다. Task1은 다음 단어 맞히기, 빈칸 채우기 등 대규모 말뭉치의 문맥을 이해하는 과제이며, Task2는 문서 분류, 개체명 인식 등 우리가 풀고 싶은 자연어 처리의 구체적 문제들입니다.

업스트림 태스크를 학습하는 과정을 프리트레인(pretrain)이라고 합니다. 다운스트림 태스크를 본격적으로 수행하기에 앞서(pre) 학습(train)한다는 의미에서 이런 용어가 붙은 것으로 생각합니다.

I love this movie.
-> question을 생성한다.
multitask learning -> QA

![](./../../../assets/images/(TODO)2022-10-18-Advanced_Sellf-supervised_Pre-training_model_images/1666143910584.png)
![](./../../../assets/images/(TODO)2022-10-18-Advanced_Sellf-supervised_Pre-training_model_images/1666144207940.png)
zero shot inference :
아래 article을 주고, TL;DR을 마지막에 준다. 학습데이터에서 TL;DR이 나오면
앞쪽 문장을 보고 1줄 요약이라는 TASK를 수행한다.
![](./../../../assets/images/(TODO)2022-10-18-Advanced_Sellf-supervised_Pre-training_model_images/1666144266420.png)

GPT-3
![](./../../../assets/images/(TODO)2022-10-18-Advanced_Sellf-supervised_Pre-training_model_images/1666144442066.png)
- 이렇게 파라미터가 커져도 모델 학습이 잘 될 수 있는 이유는 무엇일까?


![](./../../../assets/images/(TODO)2022-10-18-Advanced_Sellf-supervised_Pre-training_model_images/1666144516064.png)
영어문장을 프랑스어로 번역하는 task를 고려해보자 
- zero-shot : 영어 문장으로 프랑스어를 번역하는 어떤 학습데이터도 주어지지 않는다. 
- one-shot : 번역 예시를 하나만 준다. 동일한 패턴으로 예측한다.
- few-shot : 예시를 여러개 주었을 때 

- 13B를 보면 one-shot learning만 해도 성능이 크게 오른 것으로 보아, 동적인 적응 능력이 뛰어남을 볼 수 있다.
![](./../../../assets/images/(TODO)2022-10-18-Advanced_Sellf-supervised_Pre-training_model_images/1666144850491.png)

# ALBERT
경량화된 버트
이전 모델들은 대규모 메모리 모델이다.
![](./../../../assets/images/(TODO)2022-10-18-Advanced_Sellf-supervised_Pre-training_model_images/1666145350328.png)

self-attention block을 쌓아가면서 점점 더 high level, 의미론적으로 유의미한
정보를 추출해나가는 과정 = 딥러닝에서 layer를 쌓아가는 과정.

임베딩 레이어에서 워드가 가지는 정보를 전체 시퀀스에서 문장을 고려해서 저장.

이를 줄이자.
모델 사이즈를 줄이기 위한 방법. 
입력 데이터를 2차원

# Factorized Embedding Parameterization
![](./../../../assets/images/(TODO)2022-10-18-Advanced_Sellf-supervised_Pre-training_model_images/1666145587344.png)
여기서 E x H가 W라는 선형변환이라고 하면, 아래 그림과 같이
파라미터 수를 줄일 수 있다.
Param. 개수가 V * H개에서 V * E + E * H개로 감소

![](./../../../assets/images/(TODO)2022-10-18-Advanced_Sellf-supervised_Pre-training_model_images/1666148123394.png)


## Cross-layer Parameter Sharing
적층해서 쌓는 self-attention block
서로 다른 block에서 사용하는 선형변환 matrix를 공통적으로 사용하도록 변경.
![](./../../../assets/images/(TODO)2022-10-18-Advanced_Sellf-supervised_Pre-training_model_images/1666154040291.png)

# Sentence Order Prediction
NSP는 
두개의 문장을 같은 문서에서 나왔는지, 관련없는 두 가지 문서에서
랜덤하게 나왔는지,
그러나 NSP TASK가 크게 실효성이 없다. -> MLM 성능은 떨어지지 않음

SOP를 도입한다.
(정방향으로 된 문장연결인지 아니면 거꾸로 되었는지 binary)
원래 있던 순서대로 분류 : positive sample
순서를 뒤바꾸어 분류 : negative sample
SOP는 NLP 모델이 글의 논리적인 흐름을 파악할 수 있는 방법이며, 관련된 Task에서 유의미한
효과를 거둘 수 있다.

SP Tasks = Sentence Prediction Task
![](./../../../assets/images/(TODO)2022-10-18-Advanced_Sellf-supervised_Pre-training_model_images/1666155662867.png)

# ELECTRA : Efficiently Learning an Encoder that Classifies Token Replacements Accurately
기존 MLM task에서 한발 더 나간 기법으로, GAN에서 착안한 Pre-training 모델이다.
Generator 역할을 하는 BERT로 부터 생성된 단어들이 원래 단어가 맞는지, 예측 모델에 의해
대체된 불완전한 단어인지 discriminator를 통해 예측한다.
이때 discriminator는 pre-training 모델로 사용한다. 
같은 계산량으로 다른 모델보다 더 좋은 성능을 보여준다.
![](./../../../assets/images/(TODO)2022-10-18-Advanced_Sellf-supervised_Pre-training_model_images/1666156421341.png)

# Light-weight Models
![](./../../../assets/images/(TODO)2022-10-18-Advanced_Sellf-supervised_Pre-training_model_images/1666158001962.png)


## DistillBert
Knowledge distillation를 적용하고, triple loss를 사용함.

- Knowledge distillation 이란?
: Teacher model과 이를 경량화한 student model이 있다. 
  Teacher 모델의 softmax 출력층에서 나온 확률 값은 Student model의 Ground Truth 확률로 사용한다. 
이로써 **Student model이 Teacher model의 에측값을 최대한 모사(distillation)하도록 설계**함.
 
- Triple loss : soft target loss($L_ce$), hard target loss($L_mlm$), cosine embedding loss($L_cos$) 사용
- soft target loss (Lce)
수식

Lce=∑iti∗log(si)
ti: teacher model의 output(soft target), si: student model의 output
temperature T 사용
hard target loss (Lmlm)
BERT에서 사용하는 일반적인 MLM(Masked Language Model) loss
dynamic masking 사용
cosine embedding loss (Lcos)

teacher model과 student model의 hidden vector들의 direction을 align하는 효과

## TinyBERT
- DistillBERT의 Knowledge distillation에 더해,
Teacher model의 각 layer별 중간 출력 (hidden state, embedding weight)들도
모사하도록 하는 모델.

## Fusing Knowledge Graph into Language Model
bert는 주어진 문장, 더 긴 문장이 있을 때 문맥을 잘 파악하고 관계를 파악하긴 하지만,
주어져 있지 않은 추가적인 정보들을 효과적으로 활용하지는 못한다.

주어진 문장 : 땅을 팠다. 
추가 문장 : 꽃을 심기 위해, 집을 짓기 위해
QA: 땅을 무슨 도구로 팠을까?
무슨 도구를 팠을지는 나타나있지 않아.
그러나 사람의 경우는 꽃을 심기 위해,작은 부삽사용. 집은 포크레인 같은 걸 사용할 것이다.
즉, 외부 지식(상식)을 이용해 추론을 할 수 있는지?

문장과 QA를 이어주는 객체 : 부삽, 포크레인이 된다.
이걸 어떻게 정의하는가?
-> Knowledge graph


# Discussion


# Reference
- 네이버 AI 부트 (* 강의 자료 바탕으로 재구성)
- [트랜스퍼 러닝](https://ratsgo.github.io/nlpbook/docs/introduction/transfer/)
- [DistilBERT](https://cpm0722.github.io/paper-review/distilbert-a-distilled-version-of-bert-smaller-faster-cheaper-and-lighter)