---
layout: single
title: vision 딥러닝 역사
tags: [vision, deep learning]
categories: vision
---

# Introduction


# Pre-question


![](./../../../assets/images/(TODO)2022-10-05-VISION_APP_images/1664935889339.png)
일반적인 cnn이다.

이렇게 완전히 cnn만 쓰자.
![](./../../../assets/images/(TODO)2022-10-05-VISION_APP_images/1664935937532.png)

파라미터도 똑같다. 왜 이렇게 하냐?
![](./../../../assets/images/(TODO)2022-10-05-VISION_APP_images/1664936082849.png)

1. input dimension에 상관없이 (이미지 크기에 상관없이) 동작함
2. 고양이가 어디있는지 heatmap이 나오겠다.
다만, 출력이 줄어드는 단점이 있네?

![](./../../../assets/images/(TODO)2022-10-05-VISION_APP_images/1664936237542.png)
deconvolton : spatial dimension을 늘림
![](./../../../assets/images/(TODO)2022-10-05-VISION_APP_images/1664936293609.png)
3x3 정보를 하나의 픽셀로 만들어서, 그걸 복원할 수 있느냐
못하자너..
엄밀히는 conv의 반대는 아니지만 비슷하게 생각할 수 있다.

R-CNN
![](./../../../assets/images/(TODO)2022-10-05-VISION_APP_images/1664936452434.png)

이미지에서 2000개의 region을 뽑고 region 크기를 동일하게 만든다음 서포트 벡터 머신으로 분류한다.

R-CNN은 바운딩 박스 2000개에 대해 다 CNN 통과시켜야 됨.
그래서 GPU에서 1개 처리하는 데 1분 걸림.
이미지에서 CNN은 (regiondㅔ서 가져와서) 1번 뽑자. SPPNET
![](./../../../assets/images/(TODO)2022-10-05-VISION_APP_images/1664936702380.png)


![](./../../../assets/images/(TODO)2022-10-05-VISION_APP_images/1664937107254.png)

RPN이 추가된다.
![](./../../../assets/images/(TODO)2022-10-05-VISION_APP_images/1664937132836.png)
RPN이 뭐냐?
이미지의 패치에 물체가 있는지 없는지 proposal을 해주는 것이다.
템플릿을 고정한다.
fc 레이어를 모두 돌아가서 찍는데, 패치마다 물체가 있는지 없는지 들고 있는 것
![](./../../../assets/images/(TODO)2022-10-05-VISION_APP_images/1664937218425.png)
![](./../../../assets/images/(TODO)2022-10-05-VISION_APP_images/1664937294223.png)
4: BBOX 크기 변경을 위해 WIDTH, HEIGHT, X, Y 를 조절
2: YES OR NO

YOLO는 BBOX를 따로 뽑는 region proposal이 없다.
![](./../../../assets/images/(TODO)2022-10-05-VISION_APP_images/1664937504717.png)


![](./../../../assets/images/(TODO)2022-10-05-VISION_APP_images/1664937595154.png)


# Discussion


# Summary


# Reference
- 네이버 AI 부트캠프 (* 강의 자료 바탕으로 재구성)     