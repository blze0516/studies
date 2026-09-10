# Day 4 Exercises — Acceptance Criteria + Definition of Done

정답은 포함하지 않는다. 답은 `exercise-solutions.md`에 작성한다.

---

## 초급 5문제

### 1
Requirement와 Acceptance Criteria의 차이를 각각 한 문장으로 설명하라.

### 2
Given / When / Then에서 각각 무엇을 적는지 설명하라.

### 3
다음 문장이 왜 나쁜 Acceptance Criteria인지 설명하라.

```text
예약 기능이 정상적으로 동작한다.
```

### 4
Acceptance Criteria와 Test는 같은 것인가? 아니라면 차이를 설명하라.

### 5
Definition of Done이 필요한 이유를 두 가지 적어라.

---

## 중급 5문제

### 6
다음 Requirement를 Given / When / Then으로 바꿔라.

```text
과거 시간은 예약할 수 없다.
```

### 7
다음 Acceptance Criteria의 문제를 찾고 수정하라.

```text
Given 사용자가 있고
When 예약하면
Then DB의 reservations 테이블에 INSERT SQL이 정확히 한 번 실행된다.
```

### 8
다음 원문이 있다.

```text
잘못된 입력에는 적절한 오류를 반환해 주세요.
```

오늘까지 배운 범위 안에서 최소 3개의 Acceptance Criteria로 분해하라. 특정 HTTP status는 아직 강제하지 않는다.

### 9
다음 중 Core Acceptance Criteria와 Optional Acceptance Criteria를 구분하고 이유를 적어라.

```text
- 유효 예약 생성
- 중복 예약 거절
- 과거 슬롯 거절
- 시간 남으면 예약 취소
- README에서 실행 방법 확인
```

### 10
다음 DoD 항목을 검토하라.

```text
- 코드가 예쁘다.
- 테스트가 많다.
- 최신 기술을 썼다.
- 적절한 문서가 있다.
```

각 항목을 Yes/No로 판정 가능한 기준으로 수정하라.

---

## 고급 5문제

### 11
출제자에게 다음 질문을 보냈지만 답이 없다.

```text
현재 시각과 정확히 같은 슬롯은 예약 가능한가요?
```

4시간 과제이고 구현을 계속해야 한다. Requirement를 몰래 바꾸지 않으면서 Acceptance Criteria와 Assumption을 어떻게 작성할지 단계별로 설명하라.

### 12
다음 두 AC를 비교하라.

```text
A:
Given 이미 예약된 슬롯이 있고
When 같은 슬롯을 예약하면
Then 두 번째 예약은 성공하지 않는다.

B:
Given 이미 예약된 슬롯이 있고
When 같은 슬롯을 예약하면
Then 서비스는 DuplicateReservationException을 던지고
Repository.save는 호출되지 않으며
HTTP 409와 errorCode DUPLICATE_SLOT을 반환한다.
```

Day 4 시점에는 어느 쪽이 더 적절한지 설명하고, B의 세부 사항이 언제 정당화될 수 있는지도 적어라.

### 13
어떤 기능이 Acceptance Criteria는 모두 통과했지만 README에 실행 명령이 없고, 실제 검증 명령도 기록하지 않았다. 이 상태를 Done이라고 부를 수 있는지 DoD 관점에서 답하라.

### 14
Requirement → Acceptance Criteria → Test 간 Traceability가 깨지는 사례를 하나 만들고, 평가 전에 어떻게 발견할지 설명하라.

### 15
다음 변경 요청을 받았다.

```text
동일 이메일은 하루에 최대 한 번만 예약할 수 있습니다.
```

현재 Day 4 문서에서 어떤 Requirement, Ambiguity/Assumption, Acceptance Criteria, DoD 항목을 확인하거나 수정해야 하는지 Impact Map을 작성하라. 아직 구현 방법이나 DB 기술을 정답으로 요구하지 않는다.
