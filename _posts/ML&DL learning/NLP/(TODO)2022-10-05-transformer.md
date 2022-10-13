---
layout: single
title: NLP 기초
tags: [NLP]
categories: nlp
---

# Discussion


# Reference
- 네이버 AI 부트
- 
- 

- Pretrained language model paper (PLM,LM ,LLM: Large Language model)
    - 해당모델이 어떤 contribution(어떤 차별점)이 있는지
    - 
    - 어떤 모델을 토대로 하는지 (Transformer ? 혹은 다른 아키텍쳐?)
    - 
    - pretraining 목적함수가 무엇인지
    - 
    - 실험에 사용한 데이터가 무엇인지
    - 
- downstream task paper : fine-tuning
- 읽기전에..
    - **모델의 제목으로 해당 모델이 어떤 방법론일지 가설 세워보기**
    - 
    - **모델의 메인 figure를보고 감 잡아보기**
    - 
    - 코드가 있는지 체크해보기
    - 
    - 풀고자 하는 문제가 무엇인지 (Task 정의)
    - 
    - 기존 paper들은 이 task를 어떻게 풀어왔는지
    - 
    - 기존 paper 대비 이 논문은 어떤 점이 강점이며, Contribution인지
    - 
    - 내가 가설을 세운 이 모델의 특징과, 실제 해당 모델의 주장이 어느정도 일치하는지
- 논문을 읽을 때 어떤 부분이 해결되지 않는지 체크해두기
    - 코드를 보고 해당 부분 체크해야함
    - 논문내용과 내 생각을 짧게라도 정리해두기


embedding vector
- 특정 단어를 벡터로 변환해주는 변환기

- 임베딩 디멘젼이 
embedding 매트릭스는 어떻게 생성되나요? 
: 학습 
트랜스포머 이후는 대량의 쿼터스로 미리 임벧딩 메트릭스를 학습해서
사용한다.

미리 학습한 걸, 이걸 잘 활용하는 모델이 word2vec, fasttext , bert, gpt, bart

이런거 안 쓰고
rnn, cnn은 그냥 초기화한 임베딩 매트릭스를 학습시키는 방법

모델을 도리면서 임베딩 매트릭스 학습 보통 시키냐?

금융데이터에 대해 학습 -> 

torch.embedding을 그냥 불러오면?
초기화된 임베딩 메트릭스를 그냥 가져온다.

트렌슴포머는 레이어가 너무 많아

레이어마다 나오는 값을 노멀라이제이션하면 안정적으로 학습시킨다

배치는 이미지에서 많이 사용한다.

Transformer survey study

self encoder 

encoder - decoder 

논문 
https://github.com/aladdinpersson/Machine-Learning-Collection/blob/master/ML/Pytorch/more_advanced/transformer_from_scratch/transformer_from_scratch.py

유튜바ㅡ 내용
https://www.youtube.com/watch?v=x_8cp4Vdnak&ab_channel=%EA%B3%A0%EB%A0%A4%EB%8C%80%ED%95%99%EA%B5%90%EC%82%B0%EC%97%85%EA%B2%BD%EC%98%81%EA%B3%B5%ED%95%99%EB%B6%80DSBA%EC%97%B0%EA%B5%AC%EC%8B%A4캠프 (* 강의 자료 바탕으로 재구성)