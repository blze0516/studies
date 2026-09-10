# SQL Coding Test Lab

대기업 IT / 백엔드 / 서버 개발자 SQL 코딩테스트 6주(30일) 실습 워크스페이스.

## 고정 환경

- PostgreSQL **18.6**
- DBeaver Community **26.2.0**
- Master Dataset: `dataset/backend_sql_interview_dataset.sql`
- Schema: `interview_lab`

버전 근거는 `docs/environment.md`를 따른다. 과정 중 별도 요청이 없으면 위 버전을 유지한다.

## 시작하기

1. PostgreSQL 18.6에 접속한다.
2. DBeaver에서 `dataset/backend_sql_interview_dataset.sql` 전체를 실행한다.
3. 새 스크립트마다 먼저 실행한다.

```sql
SET search_path TO interview_lab;
```

4. 오늘 강의는 `lectures/day01_sql_coding_test_lecture.md`를 연다.
5. 연습 SQL은 `practice/day01/`에 저장한다.

## 폴더 구조

```text
sql-coding-test-lab/
├── README.md
├── curriculum/
│   └── sql_coding_test_6week_curriculum.md
├── dataset/
│   └── backend_sql_interview_dataset.sql
├── prompts/
│   └── sql_day_lecture_generator_prompt.md
├── docs/
│   ├── environment.md
│   ├── course-progress.md
│   ├── sql-patterns.md
│   └── troubleshooting.md
├── lectures/
│   └── day01_sql_coding_test_lecture.md
├── practice/
│   └── day01/
├── solutions/
│   └── day01/
├── explain/
│   ├── plans/
│   └── notes/
└── scratch/
```

이후 Day 자료는 같은 규칙으로 `lectures/`, `practice/dayNN/`, `solutions/dayNN/`에 추가한다.

## Source of Truth

- 커리큘럼: `curriculum/sql_coding_test_6week_curriculum.md`
- 데이터셋: `dataset/backend_sql_interview_dataset.sql`
- 강의 생성 규칙: `prompts/sql_day_lecture_generator_prompt.md`

실습 중 Master Dataset의 테이블 구조와 seed를 임의로 고치지 않는다. 다시 실행하면 `interview_lab` 스키마가 초기화된다.
