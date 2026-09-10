# SQL Day Lecture Generator Prompt

이 파일은 SQL 코딩테스트 일일 강의를 생성할 때 사용하는 규칙이다.

## 고정 조건

- 과정: 6주 30일, `curriculum/sql_coding_test_6week_curriculum.md`를 따른다.
- DBMS: PostgreSQL 18.6
- 도구: DBeaver Community 26.2.0
- Dataset: `dataset/backend_sql_interview_dataset.sql`만 사용한다.
- Schema: `interview_lab`
- 파일명: `lectures/dayNN_sql_coding_test_lecture.md`

## 생성 규칙

1. 오늘 범위와 하지 않을 범위를 강의 앞부분에 명시한다.
2. 새 테이블이나 새 seed를 만들지 않는다. 기존 Master Dataset만 조회한다.
3. 예제는 `SET search_path TO interview_lab;`를 전제로 한다.
4. 결과는 grain(한 행이 무엇을 의미하는지)을 함께 적는다.
5. Top-N 예제에는 tie-breaker를 넣는다.
6. 연습 SQL 위치는 `practice/dayNN/`, 풀이는 `solutions/dayNN/`이다.
7. 원문 커리큘럼에 없는 주제를 끼워 넣지 않는다.

## 산출물 체크

- 학습 목표
- 오늘 사용할 테이블
- 이론 → 예제 → 실습 → 연습
- 완료 기준
- 오늘 패턴을 `docs/sql-patterns.md`에 추가할지 여부
