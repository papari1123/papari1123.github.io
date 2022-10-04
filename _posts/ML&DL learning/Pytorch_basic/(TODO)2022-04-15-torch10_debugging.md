---
layout: single
title: pytorch(8) monitoring tool
tags: [pytorch, model load, freezing]
categories: pytorch
---
# Introduction
pytorch로 커스텀 모델을 만들 수 있다. 커스텀 모델을 만들기 위한 nn.Module 사용법 등을 알아본다.
 
# Pre-question

![](./../../../assets/images/(TODO)2022-04-15-torch9_hyperparm_tuning_images/1664810726861.png)
BOHB 기법
![](./../../../assets/images/(TODO)2022-04-15-torch9_hyperparm_tuning_images/1664810850649.png)

![](./../../../assets/images/(TODO)2022-04-15-torch9_hyperparm_tuning_images/1664810886043.png)

모델 불*러*오기

bert = 대세

fine-tuning
: transfer learning

학습 결과를 공유하고 싶다.
: 
학습 중간 과정의 저장을 통해 최선의 결과 모델을 선택함.
만든 모델을 외부 연구자와 공유해 학습 재연성 향상.

![](./../../../assets/images/2022-04-15-torch7_fine_tunungl_images/1664427154000.png)
  
![](./../../../assets/images/2022-04-15-torch7_fine_tunungl_images/1664427207011.png)

![](./../../../assets/images/2022-04-15-torch7_fine_tunungl_images/1664428123715.png)

![](./../../../assets/images/2022-04-15-torch7_fine_tunungl_images/1664428511156.png)


![](./../../../assets/images/2022-04-15-torch7_fine_tunungl_images/1664429583498.png)
NLP는 허깅패이스가 푲ㄴ

Freezing-pretrained MODEL

![](./../../../assets/images/2022-04-15-torch7_fine_tunungl_images/1664431438132.png)

요즘은
stepping freezing -> 순차적으로 freezing해서 한다.
![](./../../../assets/images/2022-04-15-torch7_fine_tunungl_images/1664432336711.png)

pth -> pytorch extensing
![](./../../../assets/images/2022-04-15-torch7_fine_tunungl_images/1664432515111.png)

# Reference
- 네이버 AI 부트캠프

- 
- https://www.youtube.com/watch?v=O2wJ3tkc-TU