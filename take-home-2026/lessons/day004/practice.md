# Day 4 Practice — Acceptance Criteria + Definition of Done

## 실습 목표

강의의 완성 예시를 그대로 복사하는 데서 끝내지 않고, 다른 모호한 Take-home brief를 직접 검증 가능한 기준으로 바꾼다.

---

# 실습 1 — 모호한 게시판 과제 분석

## 과제 상황

다음은 학습용 모의 과제다.

```text
간단한 게시판을 만들어 주세요.
사용자는 글을 작성하고 목록을 볼 수 있어야 합니다.
제목과 내용이 이상하면 적절히 처리해 주세요.
삭제된 글은 목록에 보이면 안 됩니다.
가능하면 검색도 추가해 주세요.
README에 실행 방법을 적어 주세요.
```

실제 기업 기출이 아니다.

## 평가자가 보는 것

- “이상하면 적절히” 같은 모호함을 그대로 구현하지 않는가?
- Must와 Optional을 구분하는가?
- 정상/실패 behavior를 검증 가능한 기준으로 표현하는가?

## Step 1 — Requirement 분류

아래 표를 직접 채운다.

| ID | 유형 | Requirement | 근거 |
|---|---|---|---|
| FR-01 | Functional |  |  |
| FR-02 | Functional |  |  |
| FR-03 | Functional |  |  |
| FR-04 | Functional |  |  |
| NFR-01 | Delivery |  |  |
| OPT-01 | Optional |  |  |

## Step 2 — Ambiguity 3개 이상 찾기

예시 형식:

```text
AMB-01
- 모호함:
- 왜 중요한가:
- 질문:
- 답이 없을 때 가정:
```

최소 3개 작성한다.

---

# 실습 2 — Given / When / Then 8개 직접 작성

위 게시판 과제에 대해 **8개** 작성한다.

조건:

```text
정상 흐름 최소 2개
잘못된 입력 최소 2개
삭제 관련 최소 2개
README/Delivery 최소 1개
나머지 1개 자유
```

템플릿:

```text
AC-01
Given
When
Then
연결 Requirement:
```

작성 후 각 AC에 대해 다음을 체크한다.

```text
[ ] Pass/Fail 가능한가?
[ ] 구현 세부가 아닌 behavior인가?
[ ] 원문에 없는 사실을 추가하지 않았는가?
[ ] 모호한 부분은 가정 표시가 있는가?
```

---

# 실습 3 — 나쁜 AC 고치기

다음을 고쳐라.

### A

```text
Then 게시글이 잘 저장된다.
```

### B

```text
Then 적절한 에러를 준다.
```

### C

```text
Then PostService.createPost()가 실행된다.
```

### D

```text
Then 검색이 매우 빠르다.
```

각 문장에 대해:

```text
1. 무엇이 문제인가?
2. 어떤 정보가 더 필요한가?
3. 수정한 Given/When/Then
```

을 작성한다.

---

# 실습 4 — Definition of Done 직접 설계

게시판 과제의 4시간 제출이라고 가정한다.

다음 네 범주로 DoD를 작성한다.

## Scope

- [ ]
- [ ]

## Behavior

- [ ]
- [ ]
- [ ]

## Evidence

- [ ]
- [ ]

## Delivery

- [ ]
- [ ]

### 금지

아직 배우지 않은 기술을 의무로 넣지 않는다.

예:

```text
Kafka 필수
Kubernetes 배포 필수
분산 tracing 필수
```

원문과 오늘까지 배운 범위에 맞춰 작성한다.

---

# 실습 5 — AC vs Test 분리

다음 항목을 `Acceptance Criteria` 또는 `Test / Evidence`로 분류하라.

```text
1. 이미 예약된 슬롯에 두 번째 예약이 성공하지 않는다.
2. JUnit 테스트 15개를 작성한다.
3. README에서 실행 명령을 확인할 수 있다.
4. curl로 잘못된 이메일 예약을 한 번 호출해 본다.
5. 실패한 요청이 새 예약을 만들지 않는다.
6. Integration Test에서 실제 DB를 사용한다.
```

그리고 설명한다.

```text
Acceptance Criteria = ?
Test / Evidence = ?
왜 둘을 구분해야 하는가?
```

---

# 오늘의 실습 제출물

필수:

```text
docs/requirements/ACCEPTANCE_CRITERIA.md
```

추가 연습 답안은 원하는 경우 다음처럼 로컬에 작성해도 된다.

```text
lessons/day004/practice-notes.md
```

`practice-notes.md`는 제공 답안이 아니라 **자기 실습 기록용 파일**이다.

---

# Self Review

- [ ] Requirement와 AC를 혼동하지 않았는가?
- [ ] Given에 상태가 있는가?
- [ ] When이 지나치게 많은 행동을 담고 있지 않은가?
- [ ] Then이 observable한가?
- [ ] Optional을 Core Done과 분리했는가?
- [ ] Assumption을 사실처럼 쓰지 않았는가?
- [ ] DoD를 Yes/No로 체크할 수 있는가?

---

# 더 해보기

Day 2의 `REQUIREMENTS.md`에 있는 기존 Acceptance Criteria 초안과 Day 4의 `ACCEPTANCE_CRITERIA.md`를 비교한다.

질문:

```text
1. 어떤 기준이 더 검증 가능해졌는가?
2. 어떤 모호함은 아직 남아 있는가?
3. 어떤 AC는 나중에 Test로 바로 변환하기 쉬운가?
4. 어떤 AC는 출제자의 추가 답변이 필요할 수 있는가?
```
