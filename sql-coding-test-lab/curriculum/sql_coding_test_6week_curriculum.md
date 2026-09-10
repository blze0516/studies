# SQL 코딩테스트 6주 커리큘럼

> **기준일:** 2026-09-10  
> **기간:** 6주 × 5일 = 30일  
> **대상:** 대기업 IT / 백엔드 / 서버 개발자 SQL 코딩테스트  
> **DBMS:** PostgreSQL 18.6  
> **도구:** DBeaver Community 26.2.0  
> **Master Dataset:** `dataset/backend_sql_interview_dataset.sql`  
> **Schema:** `interview_lab`

전체 30일 동안 같은 데이터셋을 사용한다. Day마다 새 테이블을 만들지 않고, 조회 패턴만 확장한다.

## Week 1 — 한 테이블 조회

| Day | 주제 | 아직 하지 않는 것 |
|---|---|---|
| 1 | SELECT / WHERE / ORDER BY / LIMIT | JOIN, 집계 |
| 2 | NULL 처리 | 문자열 패턴 |
| 3 | 문자열 함수 / LIKE | 날짜 함수 |
| 4 | 날짜 함수 | GROUP BY |
| 5 | GROUP BY / HAVING | JOIN |

## Week 2 — JOIN

| Day | 주제 |
|---|---|
| 6 | INNER JOIN |
| 7 | LEFT JOIN |
| 8 | 다중 JOIN / grain 유지 |
| 9 | JOIN + WHERE vs JOIN + ON |
| 10 | JOIN 연습 종합 |

## Week 3 — 서브쿼리

| Day | 주제 |
|---|---|
| 11 | 스칼라 서브쿼리 |
| 12 | IN / EXISTS |
| 13 | 파생 테이블 |
| 14 | 상관 서브쿼리 |
| 15 | 서브쿼리 연습 종합 |

## Week 4 — Window Function

| Day | 주제 |
|---|---|
| 16 | ROW_NUMBER |
| 17 | RANK / DENSE_RANK |
| 18 | SUM/AVG OVER |
| 19 | LAG / LEAD |
| 20 | Window 연습 종합 |

## Week 5 — 실행 계획과 성능

| Day | 주제 |
|---|---|
| 21 | EXPLAIN 읽기 |
| 22 | 인덱스와 필터 |
| 23 | 정렬 / LIMIT 비용 |
| 24 | JOIN 전략 기초 |
| 25 | 느린 쿼리 고치기 |

## Week 6 — 혼합 모의고사

| Day | 주제 |
|---|---|
| 26 | 조회 + 집계 세트 |
| 27 | JOIN + Window 세트 |
| 28 | 함정 조건 / NULL / 동률 |
| 29 | 시간 제한 모의고사 |
| 30 | 오답 복기 / 패턴 정리 |

## 매일 산출물 위치

```text
lectures/dayNN_sql_coding_test_lecture.md
practice/dayNN/
solutions/dayNN/
```

실행 계획은 `explain/plans/`, 메모는 `explain/notes/`에 남긴다.
