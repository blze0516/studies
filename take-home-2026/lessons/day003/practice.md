# Day 3 Practice — Must / Should / Could + Timeboxing

## 실습 목표

Day 2의 `docs/requirements/REQUIREMENTS.md`를 읽고 다음을 완성한다.

1. Must / Should / Could / Won't 분류
2. 4시간 계획
3. 8시간 계획
4. 24시간 계획
5. Stop Rule
6. Cut Order
7. Submission Freeze

최종 파일:

```text
docs/requirements/TIMEBOX_PLAN.md
```

---

## 1. 과제 상황

Day 2 모의 예약 과제의 핵심은 다음과 같다.

```text
- 특정 날짜의 예약 가능한 30분 슬롯 조회
- 이름/이메일로 예약
- 이미 예약된 슬롯은 중복 예약 금지
- 과거 시간 예약 금지
- 잘못된 입력 오류
- README 실행 방법
- 시간이 남으면 예약 취소
- 관리자 페이지 불필요
```

오늘은 구현하지 않는다.

**범위와 시간 배분을 결정하는 연습**이다.

---

## 2. 평가자가 보는 것

- 핵심 요구를 먼저 잡았는가?
- Optional을 구분했는가?
- 시간이 달라져도 핵심 완결성을 지키는가?
- 테스트와 README에 시간을 확보했는가?
- 막혔을 때의 중단 기준이 있는가?
- 제출 직전 위험을 통제하는가?

---

## 3. 내가 먼저 생각할 것

각 항목마다 다음 질문에 답한다.

```text
A. 원문이 직접 요구했는가?
B. 빠지면 핵심 사용자 흐름이 끊기는가?
C. 빠지면 평가자가 즉시 실패를 확인할 수 있는가?
D. Optional이라고 명시되어 있는가?
E. 이번 과제에 없는 기능인가?
```

판단 예:

```text
A/B/C가 강함 → Must
중요하지만 Core 이후 가능 → Should
D → Could
E → Won't
```

---

## 4. 연습 1 — Priority Matrix 작성

빈칸을 직접 먼저 채운 뒤 `TIMEBOX_PLAN.md`와 비교한다.

| ID | Requirement | My Priority | Why |
|---|---|---|---|
| FR-01 | 가능한 슬롯 조회 |  |  |
| FR-02 | 예약 생성 |  |  |
| FR-03 | 중복 예약 금지 |  |  |
| FR-04 | 과거 예약 금지 |  |  |
| FR-05 | 잘못된 입력 오류 |  |  |
| NFR-01 | README 실행법 |  |  |
| OPT-01 | 예약 취소 |  |  |
| OOS-01 | 관리자 페이지 |  |  |

### 검토 질문

- Optional이 Must에 들어갔는가?
- 원문 Out of Scope가 되살아났는가?
- README를 “나중에”로 밀었는가?

---

## 5. 연습 2 — 4시간 Timebox 직접 만들기

총 시간:

```text
240분
```

먼저 아래 표를 채운다.

| 작업 | 분 | Done 조건 |
|---|---:|---|
| 요구사항/계획 |  |  |
| Core 1 |  |  |
| Core 2 |  |  |
| Core 3 |  |  |
| Test |  |  |
| README |  |  |
| Review/Buffer |  |  |
| **합계** | **240** |  |

### 규칙

- Test 0분 금지
- README 0분 금지
- Buffer 0분 금지
- Optional을 Core보다 앞에 두지 않기

---

## 6. 연습 3 — Delay Simulation

### 상황

4시간 과제 시작 110분 후 상황:

```text
완료
- 요구사항 정리
- 슬롯 조회

부분 완료
- 예약 생성 70%

미완료
- validation
- 중복 방지
- 과거 방지
- Test
- README
- Review
```

### 해야 할 일

남은 130분을 다시 배분한다.

조건:

```text
- 예약 취소 금지
- 관리자 기능 금지
- 새 라이브러리 도입 금지
- 제출 20분 전부터 신규 기능 시작 금지
```

### Self Review

답에 반드시 포함되어야 하는 것:

- 예약 생성 마무리
- 중복/과거 방어
- 핵심 테스트
- README
- 최종 Review

---

## 7. 연습 4 — 8시간으로 늘어났을 때

4시간 버전의 Core를 먼저 유지한다.

추가 240분을 무엇에 배분할지 정한다.

후보:

```text
- 더 많은 edge case test
- 더 나은 실행 재현성
- 오류 표현 정리
- 데이터 무결성 검토
- 예약 취소
- 문서 보강
- 불필요한 UI polish
```

### 원칙

```text
Evidence 강화
>
Bonus 기능
>
장식
```

---

## 8. 연습 5 — 24시간으로 늘어났을 때

질문:

```text
시간이 3배가 되면 기능도 3배가 되어야 하는가?
```

아니다.

다음 축을 강화한다.

```text
Correctness
Test Evidence
Reproducibility
Security thinking
Performance thinking
Documentation
Change readiness
```

단, 구체 기술은 이후 Day에서 배운 범위에 맞춰 실제 구현한다.

---

## 9. Stop Rule 만들기

최소 5개를 직접 작성한다.

템플릿:

```text
IF ______________________
AND _____________________
THEN ____________________
BECAUSE __________________
```

예:

```text
IF Optional 예약 취소를 시작하려고 한다
AND 핵심 테스트가 아직 없다
THEN 예약 취소를 시작하지 않는다
BECAUSE Core Evidence가 먼저다
```

---

## 10. Cut Order 만들기

시간이 부족해질 때 **먼저 자를 순서**를 적는다.

권장 방향:

```text
1. 장식/Polish
2. Could
3. 일부 Should
4. 문서의 과도한 상세화
5. 핵심 Must는 마지막까지 보호
```

> README 자체와 핵심 Test를 통째로 자르는 것은 권장 Cut Order가 아니다.

---

## 11. Submission Freeze 정하기

4시간 과제 예:

```text
T-30분: 신규 기능 시작 금지
T-20분: README/실행 명령 최종 확인
T-10분: diff/불필요 파일/secret 확인
T-0분: 제출
```

자신의 버전을 만든다.

---

## 12. 실제 파일 작성

이제 다음 파일을 연다.

```text
docs/requirements/TIMEBOX_PLAN.md
```

확인:

- Priority 근거가 Source와 연결되어 있는가?
- 4h/8h/24h가 별도 계획으로 보이는가?
- Stop Rule이 실제 행동으로 적혀 있는가?
- “남으면 테스트”가 아닌가?

---

## 13. Cursor에서 Self Review

Cursor Explorer에서 두 파일을 나란히 본다.

```text
docs/requirements/REQUIREMENTS.md
docs/requirements/TIMEBOX_PLAN.md
```

검색 키워드:

```text
FR-01
FR-02
FR-03
FR-04
FR-05
OPT-01
OOS-01
```

모든 핵심 ID가 우선순위 문서에서도 추적되는지 확인한다.

---

## 14. Git 검토

```bash
git diff -- docs/requirements lessons/day003
```

확인:

- 요구사항을 수정한 것이 아니라 계획을 추가한 것인가?
- 원문에 없는 기능이 갑자기 Must가 되지 않았는가?
- 시간표 합계가 맞는가?

---

## 15. 실습 완료 조건

- [ ] Priority Matrix 완료
- [ ] 4시간 계획 완료
- [ ] 8시간 계획 완료
- [ ] 24시간 계획 완료
- [ ] Stop Rule 5개 이상
- [ ] Cut Order 존재
- [ ] Submission Freeze 존재
- [ ] Optional 예약 취소는 Core 이후
- [ ] Test와 README가 별도 Timebox를 가짐
- [ ] `TIMEBOX_PLAN.md` 생성 완료
