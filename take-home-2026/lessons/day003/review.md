# Day 3 Review — Must / Should / Could + Timeboxing

## 1. 10분 Self Review

파일을 보지 않고 답한다.

1. Must는 어떤 기준으로 정하는가?
2. Optional은 언제 시작하는가?
3. Timebox와 Deadline의 차이는 무엇인가?
4. Stop Rule은 왜 필요한가?
5. 4시간과 24시간 과제의 차이를 “기술 개수”가 아닌 다른 말로 설명하라.

---

## 2. TIMEBOX_PLAN.md Review

다음 파일을 연다.

```text
docs/requirements/TIMEBOX_PLAN.md
```

체크:

- [ ] FR-01~FR-05가 모두 Must로 추적되는가?
- [ ] README가 Must 범위에 포함되는가?
- [ ] OPT-01 예약 취소가 Could인가?
- [ ] 관리자 페이지가 Won't/Out of Scope인가?
- [ ] 4시간 합계가 240분인가?
- [ ] Test 시간이 0분이 아닌가?
- [ ] README 시간이 0분이 아닌가?
- [ ] Buffer가 있는가?
- [ ] Could 시작 Gate가 있는가?
- [ ] Submission Freeze가 있는가?

---

## 3. 5분 Oral Defense

다음 순서로 말한다.

```text
1분: 내가 정한 Must
1분: Could/Won't
1분: 4시간 전략
1분: Stop Rule
1분: 24시간이어도 과설계하지 않는 이유
```

---

## 4. Red Flag Review

다음 문장이 내 계획에 숨어 있지 않은지 확인한다.

```text
“테스트는 남으면 한다.”
“README는 마지막 5분에 쓴다.”
“시간이 있으니 기술을 더 넣는다.”
“Optional이지만 구현하기 재밌어서 먼저 한다.”
“이미 1시간 썼으니 끝날 때까지 계속한다.”
```

하나라도 해당하면 Timebox를 수정한다.

---

## 5. Diff Review

```bash
git diff -- docs/requirements/TIMEBOX_PLAN.md lessons/day003
```

확인:

- [ ] Day 2 요구사항을 다시 작성하면서 의미를 바꾸지 않았는가?
- [ ] 원문과 가정을 섞지 않았는가?
- [ ] Optional이 Must로 승격되지 않았는가?
- [ ] 시간표가 현실적인가?

---

## 6. D+3 복습

3일 뒤 새로운 2~4시간짜리 과제 설명을 하나 고른다.

15분 안에 다음만 만든다.

```text
Must 3~5개
Should 1~3개
Could 1~2개
Won't 2개
Timebox
Stop Rule 3개
```

목표는 “완벽한 계획”이 아니라 **빨리 범위를 통제하는 것**이다.

---

## 7. D+7 복습

7일 뒤 다음 상황에 5분 안에 답한다.

```text
과제 60% 시간이 지났는데 Must 2개가 남았다.
Optional은 아직 시작하지 않았다.
무엇을 자르고 무엇을 지킬 것인가?
```

답에는 최소 다음이 들어가야 한다.

```text
Core
Test
README
Buffer
Known Limitation
```

---

## 8. 다음 Day 준비

Day 4에서는 다음 질문을 다룬다.

```text
“Must라고 정했는데, 정확히 언제 끝났다고 말할 수 있지?”
```

예:

```text
나쁜 완료 기준
- 예약 기능 구현 완료

좋은 완료 기준
- 유효한 미래 슬롯 예약은 성공한다.
- 이미 예약된 슬롯의 두 번째 예약은 실패한다.
- 과거 슬롯 예약은 실패한다.
- 잘못된 입력은 데이터 생성 없이 오류가 난다.
```

이 차이를 생각해 오면 된다.
