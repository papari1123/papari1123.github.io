---
layout: single
title: ML pipeline의 이해
tags: [ML Pipeline]
categories: dataset
---
# Introduction


파이프라인 단어의 뜻
: 산업 혁명 시대를 생각해보자. -> 자동차를 조립하는 조립 라인.
-> 12시간에서 3 시간을 줄였다.

생산성 향상
예측 가능한 품질
장애 대응능력 향상

모델 퍼포먼스 측정ㅇ ㅣ필요하다.

모델 서빙한 후 지속적으로 품질이 떨어진다.

이런걸 시스템화 해야 한다. 또한 장애에 대한 대응 능력도 향상되어야 한다.

대부분의 회사에서 머신러닝 모델으 배포는 쉬워졌다.
그러나 운영하기가 좀 어렵다.

배포 0 = mlops 0

서빙된 모델의 성능을 측정하고 지속적인 모델을 갖추기..

ML 시스템 개발 및 배포는 비교적 쉽고 빠르다. 그러나 해당 시스템 유지 관리는 많은 비용이 든다.


기술부채를 줄이는 건 오버헤드가 있지만 장기적으론 의미를 가진다.
 

- 리팩토링
- 종속성 제거
- 단위 테스트
- API 강화
- 미사용 코드 삭제
- 문서화

-> 유지보수성 향상

소프트웨어 공학에서 추상황의 경계가
ML 시스템에서는 미묘하게 무너진다.
왜?
: 하나의 거대한 모델을 일부만 고치는 게 안돼...
: 유닛 테스트도 안돼...
:

기존의 코드 수준의 기술 부채 제거로는 어렵다.


## 머신러닝 문제의 특징
- 쉬운/어려운 머신러닝 문제

- 머신러닝 프로그래밍 문제의 특징

- bentoml
- conda install bentoml -c conda-forge

AWS
https://github.com/bentoml/bentoctl/blob/main/docs/quickstart.md


AWS CLI 계정 연동
https://blog.naver.com/ksh60706/221721931542

https://github.com/bentoml/bentoctl/blob/main/docs/quickstart.md

# 벤또 모델 서비스로 docker image 만들기
https://docs.bentoml.org/en/latest/tutorial.html

# bentoctl로 AWS에 올리기
https://github.com/bentoml/aws-sagemaker-deploy
# torch to onnx 변환
https://tutorials.pytorch.kr/advanced/super_resolution_with_onnxruntime.html

# lambda git 안될 때 : yum 사용
RUN yum -y install git

https://chaelinyeo.github.io/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4%EC%9D%B8%EA%B3%B5%EC%A7%80%EB%8A%A5%EC%8A%A4%EC%BF%A8/AWS%EB%A5%BC%EC%9D%B4%EC%9A%A9%ED%95%9C%EC%9D%B8%EA%B3%B5%EC%A7%80%EB%8A%A5%EB%AA%A8%EB%8D%B8%EB%B0%B0%ED%8F%AC/


# Lambda로 pytorch
sam build && sam deploy –-guided --stack-name kobert --image-repository 002134135717.dkr.ecr.us-east-1.amazonaws.com/kobert  --capabilities CAPABILITY_IAM

https://aws.amazon.com/ko/blogs/machine-learning/using-container-images-to-run-pytorch-models-in-aws-lambda/


# Reference
머신러닝 엔지니어 실무 강의, Chris Song 저