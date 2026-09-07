# Reservation Take-home — REQUIREMENTS.md

- 작성 목적: Day 2 요구사항 추출 및 Ambiguity Log 실습
- Source 성격: **학습용 모의 과제** — 실제 기업 기출 아님
- 상태: Draft for implementation planning
- 다음 단계: Day 3에서 Must/Should/Could + Timebox 결정

---

## 1. Original Brief

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

> 아래 내용은 원문 자체가 아니라 **원문에서 추출한 requirement + 명시적 질문/가정**이다.

---

## 2. Functional Requirements

| ID | Requirement | Source | Priority status |
|---|---|---|---|
| FR-01 | 사용자는 특정 날짜의 예약 가능한 시간 슬롯을 조회할 수 있다. | “원하는 날짜의 예약 가능한 시간을 볼 수” | Day 3 결정 |
| FR-02 | 사용자는 이름과 이메일을 제공해 예약 가능한 슬롯 하나를 예약할 수 있다. | “이름과 이메일을 입력해 예약” | Day 3 결정 |
| FR-03 | 이미 예약된 슬롯에는 새로운 예약이 생성되지 않아야 한다. | “이미 예약된 시간에는 다른 사람이 예약할 수 없어야” | Day 3 결정 |
| FR-04 | 과거 시간에 대한 예약 요청은 성공하지 않아야 한다. | “과거 시간은 예약할 수 없습니다” | Day 3 결정 |
| FR-05 | 잘못된 입력은 성공 처리하지 않고 오류로 응답해야 한다. | “잘못된 입력에는 적절한 오류” | Day 3 결정 |

---

## 3. Non-functional / Delivery Requirements

| ID | Requirement | Verification idea |
|---|---|---|
| NFR-01 | 평가자가 README만 읽고 실행 절차를 이해할 수 있어야 한다. | Day 6 clean-run/clean-clone 관점 검증 |
| NFR-02 | 구현은 과제 범위에 맞게 단순하게 유지하고 불필요한 인프라/기능을 추가하지 않는다. | Self Review에서 불필요 dependency/architecture 확인 |
| NFR-03 | 오류는 호출자가 실패 이유를 구분할 수 있는 일관된 방식으로 표현한다. | Day 11 Error Contract에서 구체화 |

> `NFR-03`은 원문의 “적절한 오류”를 구현 가능한 방향으로 해석한 초안이다. 정확한 HTTP status/body는 아직 확정하지 않는다.

---

## 4. Constraints

| ID | Constraint | Source / Note |
|---|---|---|
| CON-01 | 예약 슬롯 길이는 30분이다. | 원문 명시 |
| CON-02 | 과거 시작 시각은 예약 대상이 될 수 없다. | 원문 명시, timezone/경계 정의 필요 |
| CON-03 | 하나의 슬롯에 동시에 유지될 수 있는 유효 예약은 최대 1건이다. | 원문의 중복 금지에서 추출, 동시 요청 세부는 Q-03 |
| CON-04 | 예약 생성에 이름과 이메일이 필요하다. | 원문 명시 |

---

## 5. Optional

| ID | Optional item | Rule |
|---|---|---|
| OPT-01 | 예약 취소 | Core requirements 완료 후 시간이 남을 때만 구현 후보 |

---

## 6. Out of Scope

| ID | Item | Reason |
|---|---|---|
| OOS-01 | 관리자 페이지 | 원문에서 명시적으로 불필요 |
| OOS-02 | 결제 | 원문 요구 없음 |
| OOS-03 | 이메일/SMS 알림 발송 | 원문 요구 없음 |
| OOS-04 | 회원가입/로그인/인증 | 원문 요구 없음. Day 5 학습 범위를 미리 끌어오지 않음 |
| OOS-05 | 다중 지점/리소스/직원 스케줄링 | 원문 요구 없음 |

---

## 7. Ambiguity Log

| ID | Ambiguity | Impact | Why it matters | Proposed handling |
|---|---|---|---|---|
| AMB-01 | 예약 가능한 영업시간 범위가 없다. | High | 슬롯 생성/조회 결과 전체가 달라짐 | Q-01 |
| AMB-02 | 시간 계산 timezone이 없다. | High | 과거/미래 판정과 날짜 경계가 달라짐 | Q-02 |
| AMB-03 | 거의 동시에 같은 슬롯을 예약하는 요청의 기대가 명시되지 않았다. | High | 중복 예약 보장 수준과 데이터 무결성에 영향 | Q-03 |
| AMB-04 | “적절한 오류”의 HTTP status/body 형식이 없다. | Medium/High | 자동 grading이 정확한 contract를 볼 수 있음 | Q-04, starter/test 우선 확인 |
| AMB-05 | 같은 이메일의 하루 예약 횟수 제한이 없다. | Medium | business rule이 달라질 수 있음 | Q-05 또는 fallback ASM-04 |
| AMB-06 | 이름 길이/공백 처리 기준이 없다. | Low | validation 세부에 영향 | 합리적 가정 가능 |
| AMB-07 | 이메일 대소문자/정규화 기준이 없다. | Low/Medium | 동일인 판정이 필요할 경우 영향 | 현재 동일인 rule 없으므로 defer |
| AMB-08 | 가능한 슬롯 목록 정렬 기준이 없다. | Low | 응답 순서만 달라짐 | ASM-01 |
| AMB-09 | 현재 시각과 정확히 같은 시작 시각을 허용할지 불명확하다. | Medium | boundary test에 영향 | Q-02와 함께 시간 정책 확정 |
| AMB-10 | 가능한 시간 조회에서 이미 지난 슬롯을 제외해야 하는지 명시가 간접적이다. | Medium | 조회 결과에 영향 | FR-04와 일관되게 제외하는 방향, 질문 가능 |

---

## 8. Questions

우선순위는 `핵심 behavior/data/test expectation을 크게 바꾸는가?` 기준이다.

| ID | Question | Priority | Fallback if unanswered |
|---|---|---|---|
| Q-01 | 예약 가능한 영업시간 범위가 정해져 있나요? | High | 학습용 기본값을 명시적으로 정하고 `ASM-02`로 기록 |
| Q-02 | 날짜/과거 여부 판정에 사용할 timezone이 정해져 있나요? 또한 현재와 같은 시각은 예약 가능한가요? | High | 하나의 고정 timezone 정책을 문서화하고 경계값을 일관되게 적용 |
| Q-03 | 같은 슬롯에 거의 동시에 여러 예약 요청이 들어와도 최종적으로 한 건만 성공해야 하나요? | High | 원문의 “다른 사람이 예약할 수 없어야”를 강한 무결성 요구로 해석 |
| Q-04 | 오류 응답의 HTTP status와 body schema가 제공되어 있나요? | High | starter/tests가 없으면 일관된 REST 오류 계약을 자체 정의하고 README에 명시 |
| Q-05 | 동일 이메일 사용자가 하루에 여러 슬롯을 예약해도 되나요? | Medium | 별도 제한이 없다고 가정 (`ASM-04`) |

---

## 9. Assumptions

> 아래는 **원문 사실이 아니다.** 질문에 답이 없거나 영향이 낮은 부분에서 진행을 위해 채택한 fallback이다.

| ID | Assumption | Reason | Risk |
|---|---|---|---|
| ASM-01 | 슬롯 목록은 시작 시각 오름차순으로 반환한다. | 예측 가능하고 변경 비용이 낮음 | Low |
| ASM-02 | 학습용 구현에서 별도 답이 없으면 영업시간을 하나의 명시적 설정값으로 둔다. | 하드코딩된 숨은 규칙보다 설정/문서화가 낫다 | Medium; 실제 과제 답변 우선 |
| ASM-03 | 인증/회원 시스템은 구현하지 않는다. | 원문 요구가 없고 범위가 크게 증가함 | Low; 실제 과제에 auth 요구가 있으면 폐기 |
| ASM-04 | 동일 이메일의 하루 예약 횟수는 제한하지 않는다. | 원문에 제한 없음 | Medium; Q-05 답변 시 변경 |
| ASM-05 | 이름은 trim 후 빈 문자열이면 유효하지 않다. | 최소 입력 품질 보장, 원문 취지와 충돌 가능성 낮음 | Low |
| ASM-06 | 이메일은 최소한 이메일 형태가 아닌 입력을 거절한다. | “잘못된 입력”의 자연스러운 최소 해석 | Low/Medium |

---

## 10. Acceptance Criteria

### FR-01 — 가능한 슬롯 조회

- **AC-01-1**: Given 유효한 날짜가 주어졌을 때, When 가능한 시간 조회를 요청하면, Then 해당 날짜에서 예약 가능한 30분 슬롯을 반환한다.
- **AC-01-2**: Given 이미 예약된 슬롯이 있을 때, When 가능한 시간 조회를 요청하면, Then 그 슬롯은 예약 가능 목록에 포함되지 않는다.
- **AC-01-3**: Given 현재 시각 기준 이미 지난 슬롯이 있을 때, When 가능한 시간 조회를 요청하면, Then 시간 정책이 확정된 후 과거 슬롯은 예약 가능 목록에 포함되지 않는다.

### FR-02 — 예약 생성

- **AC-02-1**: Given 미래의 예약 가능한 슬롯이 있을 때, When 유효한 이름과 이메일로 예약 요청을 보내면, Then 예약이 생성되고 생성된 예약 정보를 확인할 수 있다.
- **AC-02-2**: Given 이름 또는 이메일이 유효하지 않을 때, When 예약 요청을 보내면, Then 예약이 생성되지 않고 오류가 반환된다.

### FR-03 — 중복 예약 금지

- **AC-03-1**: Given 이미 예약된 슬롯이 있을 때, When 다른 예약 요청을 같은 슬롯으로 보내면, Then 두 번째 예약은 성공하지 않는다.
- **AC-03-2**: Given 같은 슬롯에 복수 요청이 겹치는 상황일 때, Then 최종적으로 하나의 유효 예약만 남아야 한다는 강한 해석을 fallback으로 사용한다. Q-03 답변이 있으면 그 답이 우선한다.

### FR-04 — 과거 예약 금지

- **AC-04-1**: Given 시간 정책상 과거인 슬롯일 때, When 예약 요청을 보내면, Then 예약은 생성되지 않는다.
- **AC-04-2**: 현재 시각과 동일한 경계값의 동작은 Q-02/최종 시간 정책과 일치해야 한다.

### FR-05 — 잘못된 입력 오류

- **AC-05-1**: Given 필수 입력이 누락되거나 최소 validation을 통과하지 못할 때, When 예약 요청을 보내면, Then 성공 응답이 아니며 예약 데이터가 생성되지 않는다.
- **AC-05-2**: 오류 응답 형식은 Q-04 또는 이후 Day 11의 Error Contract 결정과 일치해야 한다.

### NFR-01 — 실행 재현성

- **AC-NFR-01-1**: 평가자는 README에 적힌 절차만 보고 필요한 준비, 실행, 테스트 방법을 찾을 수 있다.
- **AC-NFR-01-2**: Day 6/47의 clean-run/clean-clone 검증에서 README 명령을 그대로 재현한다.

---

## 11. Requirement → Planned Evidence Traceability

| Requirement | Planned Evidence | Main curriculum connection |
|---|---|---|
| FR-01 | API contract + API test | Day 9, Day 17 |
| FR-02 | validation + API/integration test | Day 10, Day 17~18 |
| FR-03 | DB integrity + concurrency evidence | Day 25~26 |
| FR-04 | boundary/unit/API test | Day 16~18 |
| FR-05 | validation/error contract test | Day 10~11, Day 17 |
| NFR-01 | README + clean clone report | Day 6, Day 47 |
| CON-01 | API/domain validation + DB model | Day 9~10, Day 22 |
| OPT-01 | 구현 여부를 Day 3 timebox에서 결정 | Day 3 |

---

## 12. Risks to Carry Forward

1. **Timezone / 영업시간 미정**: 슬롯 결과와 과거 판정의 기대값이 달라질 수 있다.
2. **동시 중복 예약 의미**: Day 4에서 race condition과 DB integrity 관점으로 다시 검증해야 한다.
3. **오류 계약 미정**: Day 11에서 machine-readable error contract를 구체화한다.
4. **Optional scope creep**: 예약 취소를 core 완료 전에 시작하지 않는다.

---

## 13. Definition of “Ready for Day 3”

- [x] 핵심 기능이 식별되어 있다.
- [x] 제약이 기능과 분리되어 있다.
- [x] Optional과 Out of Scope가 보인다.
- [x] High-impact Ambiguity가 질문으로 올라가 있다.
- [x] 질문 답이 없을 때 fallback Assumption이 있다.
- [x] 핵심 요구사항에 Acceptance Criteria가 있다.
- [x] 이후 어떤 Evidence로 검증할지 연결되어 있다.
- [ ] Must/Should/Could는 아직 정하지 않았다 — **Day 3 작업**
