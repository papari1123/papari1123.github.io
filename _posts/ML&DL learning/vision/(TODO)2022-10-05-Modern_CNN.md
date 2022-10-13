---
layout: single
title: vision 딥러닝 역사
tags: [vision, deep learning]
categories: vision
---

# Introduction


# Pre-question


AlexNet

네트워크를 깊게 쌓는데 어떻게 하면 파라미터를 줄일 수 있는가

11x11 receptive field는 커지지만, 파라미터 수는 많아진다.
![](./../../../assets/images/(TODO)2022-10-05-Modern_CNN_images/1664934079544.png)

AlexNet
- ReLU 사용
- GPU 2개 사용
- Data augmentation
- Dropout
    

![](./../../../assets/images/(TODO)2022-10-05-Modern_CNN_images/1664934254327.png)

VGGNet
![](./../../../assets/images/(TODO)2022-10-05-Modern_CNN_images/1664934330166.png)
Receptive field : 고려할 수 있는 입력의 spatial dimension

![](./../../../assets/images/(TODO)2022-10-05-Modern_CNN_images/1664934423307.png)



![](./../../../assets/images/(TODO)2022-10-05-Modern_CNN_images/1664934707907.png)

Receptive field도 그대로 가져간다.
![](./../../../assets/images/(TODO)2022-10-05-Modern_CNN_images/1664934861767.png)


이런 방법들로 구글넷이 파라미터가 제일 적다
![](./../../../assets/images/(TODO)2022-10-05-Modern_CNN_images/1664934934928.png)

![](./../../../assets/images/(TODO)2022-10-05-Modern_CNN_images/1664935016179.png)

![](./../../../assets/images/(TODO)2022-10-05-Modern_CNN_images/1664935079854.png)

차원을 맞춰주기 위해 1x1 con 사용함 보통은 simple shortcut 사용함.
![](./../../../assets/images/(TODO)2022-10-05-Modern_CNN_images/1664935120195.png)
batch norm을 relu 뒤에 쓰냐 앞에 쓰냐 논란이 있음

resnet은 conv 아웃을 더하지 말고, concat하자.
![](./../../../assets/images/(TODO)2022-10-05-Modern_CNN_images/1664935365909.png)
근데 concat하면 채널이 커진다.. 파라미터 수도 커진다.
그래서 채널 수를 줄이기 위해 1x1 conv를 쓴다. 

![](./../../../assets/images/(TODO)2022-10-05-Modern_CNN_images/1664935429989.png)

# Discussion


# Summary
- Vision 분야에서 쓰이는 CNN 계열 모델들은 깊이는 깊게, Receptive field는 유지, 파라미터 수는 줄이는 방향으로 진화했다.
- VGG : repeated 3x3 blocks으로 receptive field는 유지하면서 파라미터 수를 줄인다.
- GoogleLeNet : 1x1 convolution으로 채널수를 줄여 파라미터 수를 줄인다.
- Resnet : skip-connection으로 레이어를 깊게 쌓아도 성능이 나오도록 한다.
- DenseNet : concatenation



# Reference
- 네이버 AI 부트캠프 (* 강의 자료 바탕으로 재구성)     