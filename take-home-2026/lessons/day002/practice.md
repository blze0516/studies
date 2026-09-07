# Day 2 Practice — 모호한 예약 과제를 요구사항으로 바꾸기

## 0. 실습 규칙

- 시간: **45~60분**
- 모드: 내가 먼저 작성, AI는 마지막 누락 검토에만 사용
- 오늘은 구현하지 않는다.
- 목표는 “문서를 많이 쓰기”가 아니라 **잘못된 구현을 막는 최소한의 명확성**이다.

---

# 1. 모의 과제 원문

> 이 문장은 학습용으로 재구성한 모의 과제다. 실제 기업 기출이 아니다.

```text
간단한 예약 서비스를 만들어 주세요.

사용자는 원하는 날짜의 예약 가능한 시간을 볼 수 있어야 하고,
이름과 이메일을 입력해 예약할 수 있어야 합니다.
예약은 30분 단위이며 이미 예약된 시간에는 다른 사람이 예약할 수 없어야 합니다.
과거 시간은 예약할 수 없습니다.

잘못된 입력에는 적절한 오류를 반환하고,
평가자가 쉽게 실행할 수 있도록 README에 실행 방법을 적어 주세요.
가능한 한 간단하게 구현해 주세요.

시간이 남으면 예약 취소 기능도 추가해 주세요.
관리자 페이지는 필요 없습니다.
```

---

# 2. 실습 1 — 원문을 Atomic Statement로 쪼개기

## 실습 목표

한 문장에 여러 규칙이 섞인 상태를 그대로 두지 않는다.

## 내가 먼저 쓸 것

아래 표를 직접 채운다.

| No. | Atomic Statement | Source phrase |
|---:|---|---|
| 1 | 날짜별 예약 가능한 시간 조회 | 원하는 날짜의 예약 가능한 시간을 볼 수 있어야 |
| 2 | 예약 생성 | 예약할 수 있어야 |
| 3 | 예약 입력에 이름 필요 | 이름과 이메일을 입력 |
| 4 | 예약 입력에 이메일 필요 | 이름과 이메일을 입력 |
| 5 | 슬롯은 30분 단위 | 예약은 30분 단위 |
| 6 | 동일 슬롯 중복 예약 금지 | 이미 예약된 시간에는 다른 사람이 예약할 수 없어야 |
| 7 | 과거 예약 금지 | 과거 시간은 예약할 수 없습니다 |
| 8 | 잘못된 입력 오류 | 적절한 오류를 반환 |
| 9 | README 실행법 | README에 실행 방법 |
| 10 | 단순한 구현 | 가능한 한 간단하게 |
| 11 | 예약 취소는 선택 | 시간이 남으면 |
| 12 | 관리자 페이지 제외 | 필요 없습니다 |

### Self Review

- [ ] 한 문장에 서로 다른 규칙 2개가 있으면 분리했는가?
- [ ] 원문에 없는 기능을 추가하지 않았는가?

---

# 3. 실습 2 — 분류하기

다음 prefix를 사용한다.

```text
FR   Functional Requirement
NFR  Non-functional Requirement
CON  Constraint
OPT  Optional
AMB  Ambiguity
OOS  Out of Scope
```

초안 예:

| ID | Requirement | Type |
|---|---|---|
| FR-01 | 날짜별 예약 가능한 슬롯을 조회할 수 있다. | Functional |
| FR-02 | 이름과 이메일로 슬롯을 예약할 수 있다. | Functional |
| CON-01 | 슬롯 길이는 30분이다. | Constraint |
| FR-03 | 이미 예약된 슬롯에는 새 예약이 생성되지 않는다. | Functional/Data rule |
| FR-04 | 과거 시간에는 예약이 생성되지 않는다. | Functional/Validation rule |
| NFR-01 | README에 실행 절차를 제공한다. | Delivery NFR |
| OPT-01 | 예약 취소 | Optional |
| OOS-01 | 관리자 페이지 | Out of Scope |

직접 `docs/requirements/REQUIREMENTS.md`와 비교하면서 빠진 항목을 찾는다.

---

# 4. 실습 3 — Ambiguity Hunt 10분

아래 질문을 사용하지 말고 먼저 스스로 찾아본다.

10분 뒤 참고용 힌트:

```text
영업시간?
timezone?
현재 시각과 정확히 같은 슬롯?
가능한 시간 조회에서 과거 슬롯 제외?
동일 이메일 하루 횟수?
이메일 형식 validation?
이름 길이/공백?
중복 예약의 동시 요청 의미?
오류 status/body?
예약 목록 정렬?
```

각 모호함을 아래 형식으로 쓴다.

```md
### AMB-01 — [제목]
- Why ambiguous:
- Impact: High / Medium / Low
- Evidence available:
- Decision: Ask / Assume / Defer
- Fallback if unanswered:
```

---

# 5. 실습 4 — Ask / Assume 결정

다음 결정 규칙을 적용한다.

```text
1. 원문/테스트/starter code에 답이 있나?
2. 잘못 해석하면 핵심 동작이 달라지나?
3. 되돌리기 비용이 큰가?
4. 질문 답을 기다릴 시간이 있나?
```

권장 질문 후보:

```text
Q-01 예약 가능한 영업시간 범위가 있나요?
Q-02 시간 판정에 사용할 timezone이 정해져 있나요?
Q-03 동일 슬롯 중복 예약은 거의 동시에 들어오는 요청에서도 반드시 한 건만 성공해야 하나요?
Q-04 오류 응답의 HTTP status/body 계약이 제공되어 있나요?
```

권장 가정 후보:

```text
ASM-01 목록은 시작 시각 오름차순으로 반환한다.
ASM-02 예약 ID의 내부 형식은 구현 세부사항으로 둔다.
ASM-03 별도 인증 요구가 없으므로 회원가입/로그인은 구현하지 않는다.
```

주의: 이 가정들은 **오늘 모의 원문**에 대한 예시다. 실제 과제의 starter/test/API contract가 있으면 그것이 우선이다.

---

# 6. 실습 5 — Acceptance Criteria 작성

최소 다음 요구사항에 대해 작성한다.

```text
FR-01 가능한 슬롯 조회
FR-02 예약 생성
FR-03 중복 예약 금지
FR-04 과거 예약 금지
NFR-01 README 실행법
```

형식:

```text
Given [상태]
When [행동]
Then [관찰 가능한 결과]
```

예:

```text
Given 이미 예약된 슬롯이 있을 때
When 같은 슬롯으로 두 번째 예약 요청을 보내면
Then 새 예약은 생성되지 않는다.
```

---

# 7. 실습 6 — Traceability Map

아직 테스트 구현은 하지 않지만 계획한다.

| Requirement | Planned Evidence | Later Day |
|---|---|---:|
| FR-01 | API contract/test | Day 9, 17 |
| FR-02 | API + integration test | Day 17, 18 |
| FR-03 | DB integrity + concurrency test | Day 25~26 |
| FR-04 | boundary test | Day 16~18 |
| NFR-01 | clean clone README check | Day 6, 47 |

이 표의 목적은 미래 기술을 오늘 구현하는 것이 아니라, **요구사항이 검증되지 않은 채 사라지지 않게 하는 것**이다.

---

# 8. 최종 파일 점검

완성 파일:

```text
docs/requirements/REQUIREMENTS.md
```

확인 명령:

```bash
test -f docs/requirements/REQUIREMENTS.md && echo "REQUIREMENTS exists"
grep -n 'FR-' docs/requirements/REQUIREMENTS.md
grep -n 'AMB-\|Q-\|ASM-' docs/requirements/REQUIREMENTS.md
grep -n 'AC-' docs/requirements/REQUIREMENTS.md
```

---

# 9. AI를 쓴다면 마지막에만

내 초안이 끝난 뒤 Cursor Agent에게 다음처럼 요청할 수 있다.

```text
이 REQUIREMENTS.md를 수정하지 말고 리뷰만 해줘.
원문과 비교해 다음만 찾아줘:
1) 원문에 있는데 빠진 requirement
2) 원문에 없는데 내가 추가한 requirement
3) 여러 해석이 가능한데 Ambiguity에 없는 항목
4) pass/fail이 불가능한 Acceptance Criteria
결과는 표로만 제시하고, 최종 결정은 내가 하게 해줘.
```

AI가 “이 기능도 있으면 좋다”고 추천해도 원문 근거가 없으면 Must에 넣지 않는다.

---

# 10. 오늘 실습 완료 조건

- [ ] 원문을 atomic statement로 분리했다.
- [ ] FR/NFR/Constraint/Optional/Out of Scope를 구분했다.
- [ ] 모호함을 최소 5개 찾았다.
- [ ] Ask/Assume 판단 이유를 적었다.
- [ ] 핵심 기능에 Acceptance Criteria가 있다.
- [ ] 이후 Evidence 계획이 있다.
- [ ] 원문에 없는 기능을 Must로 추가하지 않았다.
