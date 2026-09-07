# Day 2 Review — 요구사항 추출과 Ambiguity Log

## 1. 10분 Self Review

파일을 보지 않고 답한다.

1. Functional Requirement와 Constraint의 차이는?
2. Ambiguity와 Assumption의 차이는?
3. 어떤 모호함을 질문 우선으로 처리하는가?
4. Acceptance Criteria가 왜 필요한가?
5. Out of Scope가 시간제한 과제에서 왜 중요한가?

막히는 질문만 `lecture.md`에서 다시 본다.

---

## 2. REQUIREMENTS.md Self Review

`../../docs/requirements/REQUIREMENTS.md`를 열고 확인한다.

- [ ] 원문과 내가 추가한 해석이 구분되어 있다.
- [ ] FR/NFR/Constraint/Optional이 구분되어 있다.
- [ ] 모호함이 `AMB-`로 드러나 있다.
- [ ] 질문은 `Q-`, 가정은 `ASM-`로 분리되어 있다.
- [ ] High-impact 가정을 몰래 확정하지 않았다.
- [ ] Acceptance Criteria가 pass/fail 가능하다.
- [ ] 관리자 페이지 등 제외 범위가 명시되어 있다.
- [ ] 원문에 없는 인증/결제/알림을 Must로 추가하지 않았다.
- [ ] 이후 테스트 Evidence와 연결할 수 있다.

---

## 3. 5분 Oral Defense

다음 순서로 말한다.

```text
1분: 원문에서 찾은 핵심 기능
1분: 제약과 Optional
1분: 가장 위험한 모호함 2개
1분: 질문 vs 가정 판단 기준
1분: Acceptance Criteria로 완료를 정의한 방법
```

설명할 때 “그냥 그렇게 생각했다” 대신 **impact / source / rollback cost**를 근거로 말한다.

---

## 4. Diff Review

Day 1 이후 변경을 확인한다.

```bash
git diff -- lessons/day002 docs/requirements README.md
```

아직 Git 저장소가 아니라면 파일 비교만 한다.

확인:

- [ ] 원문에 없는 기능이 슬쩍 추가되지 않았는가?
- [ ] Optional이 핵심 요구사항과 섞이지 않았는가?
- [ ] 같은 용어를 여러 뜻으로 사용하지 않았는가?
- [ ] 질문과 가정이 중복되지 않았는가?

---

## 5. D+3 복습

3일 뒤 새로운 짧은 과제 설명 하나를 골라 15분 동안 다음만 만든다.

```text
FR 5개 이하
Constraint 3개 이하
Ambiguity 5개 이하
Ask 2개 이하
Assumption 3개 이하
Acceptance Criteria 5개 이하
```

목표는 **짧게 써도 핵심을 놓치지 않는 것**이다.

---

## 6. D+7 복습

7일 뒤 Day 2 자료를 보지 않고 다음 문장을 완성한다.

> “질문해야 할 모호함은 ________________________________.”

권장 방향:

**잘못 해석했을 때 핵심 동작·데이터·테스트 기대값이 크게 달라지고, 되돌리기 비용이 큰 빈칸.**

---

## 7. 다음 Day 준비

Day 3에서는 오늘 문서의 모든 항목을 다 구현하려 하지 않는다.

다음 표를 미리 머릿속으로 생각한다.

```text
Must
Should
Could
Won't
```

특히 `OPT-01 예약 취소`가 왜 Must가 아닌지, `FR-03 중복 예약 금지`는 왜 Must일 가능성이 높은지 설명할 준비를 한다.
