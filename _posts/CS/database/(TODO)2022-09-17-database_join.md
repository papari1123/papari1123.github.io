---
layout: single
title: Database - 조인의 종류
tags: [DB, JOIN]
categories: database
---
# Introduction
SQL로 작업을 하다보면, 여러 테이블을 묶어서 하나의 결과물을 만들어줘야 할 때가 있다.
이를 조인(Join)이라고 한다.

# 조인의 사용 
MYSQL에서는 JOIN이란 쿼리로, MongoDB에서는 lookup이라는 쿼리로 처리가 가능하다.   
(단, MongoDB의 lookup은 되도록 사용하지 말아야 한다. 관계형 데이터베이스보다 성능이 떨어진다고 알려져 있기 때문)

# 조인의 종류
왼쪽 테이블을 A, 오른쪽 테이블을 B라 한 경우,

## 내부 조인
두 테이블 간의 교집합.
```sql
SELECT * FROM TableA A
INNER JOIN TableB B ON
A.key = B.key
```

# 왼쪽 조인
왼쪽 조인은 A의 모든 행이 결과 테이블에 표기된다.
B의 경우는 A와 key가 일치하는 레코드만 결과 테이블에 포함시킨다.
```sql
SELECT * FROM TableA A
LEFT JOIN TableB B ON
A.key = B.key
```

# 오른쪽 조인
오른쪽 조인은 B 의 모든 행이 결과 테이블에 표기된다.

```sql
SELECT * FROM TableA A
RIGHT JOIN TableB B ON
A.key = B.key
```

# Reference
면접을 위한 CS 전공지식 노트 - 주홍철 지음         