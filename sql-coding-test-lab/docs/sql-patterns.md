# SQL Patterns

Day 1부터 반복해서 쓰는 기본 패턴이다. 이후 Day에서 패턴이 늘면 이 파일에 누적한다.

```sql
-- 필요한 컬럼 조회
SELECT
    column1,
    column2
FROM table_name;
```

```sql
-- 행 필터
SELECT
    ...
FROM table_name
WHERE condition;
```

```sql
-- 여러 후보 값
WHERE column IN ('A', 'B', 'C')
```

```sql
-- 포함 범위
WHERE column BETWEEN lower_value AND upper_value
```

```sql
-- 결정적인 Top-N
SELECT
    ...
FROM table_name
WHERE ...
ORDER BY
    sort_column DESC,
    id DESC
LIMIT 20;
```

```sql
-- 중복 값 종류 확인
SELECT DISTINCT
    column
FROM table_name
ORDER BY column;
```
