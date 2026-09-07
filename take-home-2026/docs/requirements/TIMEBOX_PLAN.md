# Reservation Take-home — TIMEBOX_PLAN.md

- 작성 목적: Day 3 Must / Should / Could + Timeboxing 실습
- Source: `REQUIREMENTS.md`
- Source 성격: **학습용 모의 과제** — 실제 기업 기출 아님
- 상태: Planning baseline
- 원칙: **Core Complete > Bonus Feature**

---

## 1. Priority Principle

우선순위는 다음 순서로 판단한다.

```text
1. 원문이 직접 요구했는가?
2. 빠지면 핵심 사용자 흐름이 끊기는가?
3. 평가자가 즉시 실패를 확인할 가능성이 큰가?
4. 실행/검증 가능성을 위해 최소한 필요한가?
5. Optional이라고 명시되어 있는가?
6. 원문에 없는 기능인가?
```

`Must`는 “좋아 보이는 기능”이 아니라 **빠질 경우 제출이 실패할 가능성이 큰 범위**다.

---

## 2. Must / Should / Could / Won't

### Must

| ID | Item | Why Must | Minimum Evidence |
|---|---|---|---|
| FR-01 | 특정 날짜의 예약 가능한 30분 슬롯 조회 | 핵심 사용자 진입 흐름 | 대표 조회 성공 확인 |
| FR-02 | 이름/이메일로 예약 생성 | 과제의 핵심 상태 변화 | 정상 예약 생성 확인 |
| FR-03 | 이미 예약된 슬롯 중복 예약 금지 | 원문 직접 요구, 데이터 무결성 핵심 | 두 번째 예약 실패 확인 |
| FR-04 | 과거 시간 예약 금지 | 원문 직접 요구 | 과거 슬롯 실패 확인 |
| FR-05 | 잘못된 입력 오류 | 원문 직접 요구 | 잘못된 입력이 성공하지 않음 |
| NFR-01 | README 실행/테스트 방법 | 평가자가 실행하지 못하면 기능 검증 불가 | Quick Start / Test 명령 |
| PLAN-EV-01 | 핵심 Test Evidence | 완료 주장을 검증할 최소 근거 | 핵심 성공/실패 규칙 확인 |
| PLAN-EV-02 | 제출 전 Self Review | 불필요 변경·누락 위험 감소 | diff/파일/명령 검토 |

### Should

| ID | Item | Why Should | Must보다 뒤인 이유 |
|---|---|---|---|
| NFR-03 | 오류 응답을 일관된 방식으로 정리 | 평가/디버깅 품질 향상 | Day 2 원문은 형식을 구체화하지 않음 |
| S-01 | 경계/실패 테스트 보강 | 회귀 위험 감소 | 최소 핵심 Test 이후 깊이를 늘릴 수 있음 |
| S-02 | Assumption/Trade-off 짧은 문서화 | 설명 가능성 향상 | Core 실행을 깨면서까지 먼저 할 필요는 없음 |

### Could

| ID | Item | Why Could | Start Gate |
|---|---|---|---|
| OPT-01 | 예약 취소 | 원문이 “시간이 남으면”이라고 명시 | 모든 Must + 핵심 Test + README 초안 완료 후 |
| C-01 | 추가 UX/문서 polish | 제출 경험 개선 | Submission-ready 상태 확보 후 |

### Won't / Out of Scope

| ID | Item | Reason |
|---|---|---|
| OOS-01 | 관리자 페이지 | 원문에서 명시적으로 불필요 |
| OOS-02 | 결제 | 원문 요구 없음 |
| OOS-03 | 이메일/SMS 알림 | 원문 요구 없음 |
| OOS-04 | 회원가입/로그인/인증 | 원문 요구 없음 |
| OOS-05 | 다중 지점/직원 스케줄링 | 원문 요구 없음 |
| W-01 | Microservice / Kafka / Kubernetes | 과제 범위 대비 과설계 |

---

## 3. Core Complete Gate

Could를 시작하기 전에 아래가 모두 True여야 한다.

- [ ] FR-01 가능한 슬롯 조회가 동작한다.
- [ ] FR-02 예약 생성이 동작한다.
- [ ] FR-03 중복 예약이 거절된다.
- [ ] FR-04 과거 예약이 거절된다.
- [ ] FR-05 잘못된 입력이 거절된다.
- [ ] 핵심 성공/실패 Test Evidence가 있다.
- [ ] README에 실행/테스트 절차 초안이 있다.
- [ ] 현재 상태를 제출해도 Core 요구를 설명할 수 있다.

하나라도 False면 `OPT-01 예약 취소`를 시작하지 않는다.

---

## 4. 4시간 Plan — 240분

목표: **가장 작은 제출 가능한 Core**

| 구간 | 시간 | 누적 | 목표 | 종료 조건 |
|---|---:|---:|---|---|
| Requirements / Assumption 재확인 | 20분 | 20 | Day 2 범위 재확정 | Must/Could/Won't가 명확함 |
| 최소 실행 뼈대 | 25분 | 45 | 실행 가능한 기본 구조 | 최소 실행 명령 성공 가능 상태 |
| FR-01 슬롯 조회 | 35분 | 80 | 가능한 30분 슬롯 조회 | 대표 정상 시나리오 확인 |
| FR-02 + FR-05 예약 생성/입력 검증 | 45분 | 125 | 유효 예약 생성 + 잘못된 입력 거절 | 성공/실패 대표 케이스 확인 |
| FR-03 + FR-04 중복/과거 방어 | 35분 | 160 | 핵심 business rule | 두 규칙이 성공하지 않음을 확인 |
| 핵심 Test Evidence | 35분 | 195 | 회귀 가능한 핵심 검증 | Must 핵심 규칙 test 확인 |
| README Quick Start / Test | 20분 | 215 | 평가자 실행 경로 | 실행/테스트 명령이 문서에 있음 |
| Self Review + Buffer | 25분 | 240 | 제출 안정화 | 신규 기능 없이 누락/오류 점검 |

### 4시간에서 하지 않는 것

```text
- 예약 취소
- 인증
- 관리자 기능
- 복잡한 UI polish
- 고급 CI/Observability
- 과도한 Architecture 리팩토링
```

### 4시간 Cut Order

시간이 부족하면 다음 순서로 줄인다.

```text
1. 장식/Polish
2. Could 전부
3. Should의 상세화
4. 테스트의 중복/저위험 케이스 수
5. 문서의 과도한 설명
```

다음은 가능한 한 보호한다.

```text
Must behavior
핵심 Test
README 실행법
최종 Self Review
```

---

## 5. 8시간 Plan — 480분

목표: **4시간 Core + 더 강한 Evidence와 재현성**

| 구간 | 시간 | 누적 | 목표 |
|---|---:|---:|---|
| Requirement / Plan | 30분 | 30 | 질문·가정·Must 확정 |
| Core 구현 1차 | 180분 | 210 | FR-01~FR-05 동작 |
| 핵심 Test | 70분 | 280 | 성공/실패/경계 Evidence |
| 데이터 무결성/오류/구조 점검 | 55분 | 335 | 가장 위험한 규칙 보강 |
| 실행 재현성/README | 45분 | 380 | 평가자 실행 경로 강화 |
| Should 보강 | 35분 | 415 | 추가 실패 케이스/문서 |
| Could Gate 판단 | 20분 | 435 | Core Complete 확인 |
| Optional 또는 추가 품질 | 20분 | 455 | 예약 취소 또는 더 중요한 품질 보강 |
| Final Review / Buffer | 25분 | 480 | 제출 안정화 |

### 8시간 의사결정

`OPT-01 예약 취소`를 자동으로 구현하지 않는다.

다음이 더 위험하면 먼저 처리한다.

```text
- 핵심 Test 부족
- 실행 명령 불안정
- 중복 예약 위험
- 잘못된 입력 처리 불명확
- README 불완전
```

---

## 6. 24시간 Plan — 1440분 범위

24시간은 “24시간 연속 코딩”을 의미하지 않는다.

실제 과제 정책에 맞춰 수면/식사/휴식/일정도 고려한다. 아래는 **전체 제출 window를 관리하는 예시**다.

### Phase A — Core Complete

| Phase | 예산 | 목표 |
|---|---:|---|
| Requirements / Plan | 45분 | 범위·질문·가정·Done 기준 |
| Core Implementation | 240분 | FR-01~FR-05 |
| Core Test / Fix | 120분 | 핵심 성공/실패 검증 |
| README 1차 | 45분 | 실행/테스트 절차 |

소계: **450분**

### Phase B — Evidence 강화

| Phase | 예산 | 목표 |
|---|---:|---|
| Integration/Data Integrity 보강 | 120분 | 실제 failure 위험 보강 |
| Error/Boundary Test 보강 | 75분 | edge case |
| Reproducibility 보강 | 75분 | clean run 관점 |
| Security/Performance 사고 점검 | 60분 | 과도하지 않은 위험 확인 |
| Trade-off / Assumption 문서 | 45분 | 설명 가능성 |

소계: **375분**

누적: **825분**

### Phase C — Optional / Change Readiness

| Phase | 예산 | 목표 |
|---|---:|---|
| Optional 예약 취소 또는 가치 높은 개선 | 90분 | Core가 안정적일 때만 |
| 추가 사용자 흐름 검증 | 75분 | 제출 신뢰도 보강 |
| 변경 영향/리팩토링 최소 점검 | 60분 | 과도한 rewrite 금지 |

소계: **225분**

누적: **1050분**

### Phase D — 휴식/예비/제출 안정화

나머지 **390분**은 정책과 개인 상황에 따라 다음으로 배분한다.

```text
- 식사/휴식/수면
- 예상치 못한 bug buffer
- 최종 실행 재검증
- README 최종 검토
- diff review
- 제출 준비
```

핵심은 24시간이 있다고 **1440분을 모두 신규 기능에 소비하지 않는 것**이다.

---

## 7. Stop Rules

1. **Core Complete 전에는 Could를 시작하지 않는다.**
2. 새 dependency 조사에 15분 이상 쓰면 정말 필요한지 다시 판단한다.
3. Optional 기능이 예상 시간의 2배를 넘기면 중단/축소를 우선 검토한다.
4. 구조 리팩토링은 핵심 behavior 검증 전에 시작하지 않는다.
5. 저위험 polish가 Must 구현을 지연시키면 즉시 중단한다.
6. 제출 30분 전에는 신규 기능을 시작하지 않는다.
7. 최종 20분은 README/명령/diff 확인에 예약한다.
8. 핵심 Must 실패는 Could보다 더 많은 디버깅 시간을 허용하되, 진행 상황을 일정 간격으로 재평가한다.

---

## 8. Delay Recovery Rule

예상보다 늦어졌을 때:

```text
1. 남은 Must 수 확인
2. 제출까지 남은 시간 확인
3. Could 전부 제거
4. Should 상세화 축소
5. Must를 가장 작은 동작 가능한 형태로 축소
6. 핵심 Test와 README 시간은 보호
7. Known Limitation을 문서화
8. Submission Freeze 유지
```

---

## 9. Submission Freeze

### 4시간 기준

```text
T-30분: 신규 기능 시작 금지
T-25분: Core smoke check
T-20분: README 실행/테스트 명령 확인
T-15분: 불필요 파일 / debug / secret 확인
T-10분: diff review
T-5분: 제출 파일/브랜치 최종 확인
T-0분: 제출
```

8시간/24시간도 동일한 원칙으로 마지막 안정화 구간을 확보한다.

---

## 10. Known Limitations Template

Optional을 하지 않은 경우 변명처럼 쓰지 않는다.

예:

```text
## Known Limitations

- Reservation cancellation was intentionally excluded from the 4-hour scope.
- The original brief marked cancellation as optional.
- I prioritized the core booking flow, duplicate/past-time rejection,
  core tests, and reproducible run instructions first.
- With additional time, cancellation would be the next functional addition.
```

핵심은:

```text
무엇을 안 했나
왜 안 했나
무엇을 대신 지켰나
다음 순서는 무엇인가
```

를 설명하는 것이다.

---

## 11. Priority Traceability

| Requirement | Priority | 4h | 8h | 24h |
|---|---|---|---|---|
| FR-01 | Must | 구현 | 구현+검증 | 구현+강화 |
| FR-02 | Must | 구현 | 구현+검증 | 구현+강화 |
| FR-03 | Must | 구현/대표 검증 | 무결성 강화 | 동시성/통합 Evidence 강화 |
| FR-04 | Must | 구현/대표 검증 | 경계 보강 | 시간 정책/경계 보강 |
| FR-05 | Must | 최소 오류 처리 | 오류 일관성 강화 | contract/docs 강화 |
| NFR-01 | Must | README | 재현성 강화 | clean-run 관점 강화 |
| OPT-01 | Could | 제외 | Gate 통과 시 고려 | Core 안정 후 고려 |
| OOS-01 | Won't | 제외 | 제외 | 제외 |

> 이후 Day에서 배우는 구체 기술은 그 Day의 학습 범위에 맞춰 적용한다. 이 문서는 오늘 시점의 범위/시간 의사결정 문서다.

---

## 12. Day 3 Definition of Done

- [x] Must / Should / Could / Won't가 구분되어 있다.
- [x] 예약 취소는 Could다.
- [x] 관리자 페이지는 Won't다.
- [x] 4시간 계획은 240분이다.
- [x] 8시간 계획은 480분이다.
- [x] 24시간은 전체 window와 실제 작업/휴식/예비 시간을 분리해서 생각한다.
- [x] Test / README / Review가 남는 시간 취급이 아니다.
- [x] Stop Rule이 있다.
- [x] Cut Order가 있다.
- [x] Submission Freeze가 있다.
- [x] Core Complete Gate가 있다.
- [ ] Must의 완료를 더 구체적인 Acceptance Criteria/Definition of Done으로 정제한다 — **Day 4 작업**
