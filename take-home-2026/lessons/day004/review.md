# Day 4 Review — Acceptance Criteria + Definition of Done

## 1. 5분 복습

아래 질문에 문서를 보지 않고 답해 본다.

1. Requirement와 Acceptance Criteria의 차이는?
2. Given / When / Then은 각각 무엇인가?
3. Acceptance Criteria와 Test는 왜 같은 것이 아닌가?
4. Acceptance Criteria와 Definition of Done의 차이는?
5. 모호한 정책에 답을 못 받았을 때 어떻게 해야 하는가?

---

## 2. 오늘 핵심 한 문장

> **완료는 느낌이 아니라, 사전에 합의하거나 명시한 검증 가능한 기준을 통과한 상태다.**

---

## 3. 오늘의 산출물 확인

```text
docs/requirements/ACCEPTANCE_CRITERIA.md
```

확인할 것:

- [ ] Core AC 15개
- [ ] Given / When / Then 의미가 명확함
- [ ] Requirement 연결
- [ ] Working Assumption 표시
- [ ] Optional AC 분리
- [ ] Definition of Done
- [ ] Traceability

---

## 4. 빠른 Self Quiz

### Q1
“중복 예약이 잘 막힌다”는 왜 부족한가?

### Q2
`Then Repository.save()가 호출되지 않는다`는 언제 AC로 너무 구체적일 수 있는가?

### Q3
하나의 AC에 Unit Test가 반드시 하나씩 대응해야 하는가?

### Q4
Optional 예약 취소를 구현하지 않았으면 전체 제출이 미완료인가?

### Q5
출제자가 timezone을 알려주지 않았다면 어떻게 기록해야 하는가?

---

## 5. D+1 복습

다음 날 10분 동안 한다.

1. `ACCEPTANCE_CRITERIA.md`를 열지 않고 중복 예약 AC를 하나 다시 작성한다.
2. 과거 시간 AC를 하나 다시 작성한다.
3. AC와 DoD 차이를 30초 안에 말한다.

---

## 6. D+3 복습

새 도메인 하나를 고른다.

예:

```text
재고
게시판
Todo
주문
```

그리고:

```text
Requirement 3개
Acceptance Criteria 6개
Definition of Done 5개
```

를 20분 안에 작성한다.

---

## 7. D+7 복습

Day 4 문서를 다시 보고 다음을 표시한다.

```text
A. 지금도 좋은 AC
B. 너무 모호한 AC
C. 구현 세부에 지나치게 묶인 AC
D. 이후 배운 기술 때문에 더 구체화할 수 있는 AC
```

문서를 한 번 쓰고 버리는 것이 아니라, 뒤의 Test/DB/API Day와 연결해 개선한다.

---

## 8. 면접 60초 연습

다음 질문에 60초 안으로 답해 본다.

```text
"왜 요구사항 문서 외에 Acceptance Criteria까지 작성했나요?"
```

좋은 답의 구성:

```text
요구사항의 모호함
→ 검증 가능한 기준
→ 구현/테스트 정렬
→ 실패/경계 누락 방지
→ 시간 제한 속 scope 관리
```

---

## 9. 다음 Day 준비

Day 5 주제는 **Repository 초기화·Git 전략**이다.

미리 생각할 질문:

```text
좋은 commit은 왜 파일 수가 아니라 변경 의도로 나눠야 할까?
Requirement / AC와 commit message를 연결할 수 있을까?
한 번에 모든 파일을 수정하고 final commit 하나만 남기면 어떤 정보가 사라질까?
```
