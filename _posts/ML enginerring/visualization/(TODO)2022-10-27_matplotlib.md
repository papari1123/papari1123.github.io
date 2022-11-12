---
layout: single
title: 시각화도구(1) matplotlib
tags: [Visualization, matplotlib]
categories: visualization
---
# Introduction

# ㄴ
```python
fig = plt.figure(figsize = (10,5))
ax1 = fig.add_subplot(121) # 1x2 plot의 첫번째 subplot 
ax2 = fig.add_subplot(122) # 1x2 plot의 두번째 subplot

ax1.plot(x1)
ax2.plot(x2)
ax2.bar(x3) # 겹칠 수 있음
ax1.set_title("title") # 각각의 subplot 제목 지정
ax1.legend() # 범례 지정
fig.suptitle('fig') # plot의 대제목 설정
ax1.set_xticks([0, 1, 2]) # 눈금 설정

ax.annotatle(text = "anno", xy=(1, 2)) # annotation을 설정할 수 있다.
plt.show()
```
ax
# bar plot
```commandline


``` 
![](./../../../assets/images/2022-10-27_matplotlib_images/1666868792220.png)
![](./../../../assets/images/(TODO)2022-10-27_matplotlib_images/1666868863278.png)

# Reference
- 네이버 AI 부트캠프 (* 강의 자료 바탕으로 재*구*성)