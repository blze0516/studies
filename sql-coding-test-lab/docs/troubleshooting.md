# Troubleshooting

## 테이블을 찾을 수 없다

`SET search_path TO interview_lab;`를 실행했는지 확인한다. 또는 스키마를 명시한다.

```sql
SELECT *
FROM interview_lab.users;
```

## 데이터 건수가 강의와 다르다

Master Dataset 일부만 실행했을 수 있다. `dataset/backend_sql_interview_dataset.sql` **전체**를 다시 실행한다. 이 스크립트는 `interview_lab`을 삭제 후 재생성한다.

예상 건수:

| 테이블 | COUNT |
|---|---:|
| users | 300 |
| products | 120 |
| orders | 2502 |

## 같은 ORDER BY인데 결과가 매번 바뀐다

정렬 키가 동률이다. PK 같은 tie-breaker를 추가한다.

```sql
ORDER BY order_date DESC, order_id DESC
```

## DBeaver에서 스키마가 안 보인다

연결 후 스키마 트리를 새로고침한다. 스크립트가 다른 데이터베이스에 실행되지 않았는지 확인한다.
