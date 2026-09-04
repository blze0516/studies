# Day 1 Practice — 공개 과제 3개에서 평가항목 역추적하기

## 목표

공개 Take-home README를 “문제 내용”만 읽지 않고 **평가자가 관찰하려는 행동과 Evidence** 관점으로 읽는다.

오늘은 코드 구현을 하지 않는다. 각 source를 직접 읽고 `assessment_landscape.md`를 수정하는 것이 실습이다.

## Source 성격

아래 3개는 이 과정에서 **기업 first-party 공개 Take-home / assignment** 연습 자료로 취급한다.

1. Simplify Backend Take-home  
   https://github.com/SimplifyJobs/backend-take-home
2. FeedMe SE Take-home Assignment  
   https://github.com/feedmepos/se-take-home-assignment
3. ElloTechnology 2025 Full-stack Take-home  
   https://github.com/ElloTechnology/2025-full-stack-take-home

> 원문 전체를 이 저장소에 복제하지 않는다. 회사 repository가 제시하는 공개/제출 정책이 있으면 그 취지를 우선한다.

---

# 1. 45~60분 Timebox

```text
0~5분    세 링크 열기, 작성 템플릿 준비
5~18분   Simplify Backend blind read
18~31분  FeedMe blind read
31~44분  Ello blind read
44~52분  공통점/차이점 정리
52~60분  assessment_landscape.md 갱신 + self review
```

AI를 쓴다면 52분 이후 “내가 놓친 평가 신호가 있는지” 검토하는 용도로만 사용한다. 먼저 답을 받아 읽지 않는다.

---

# 2. 각 과제에서 사실만 추출하기

각 README를 읽으며 아래 양식을 채운다.

```md
## [과제명]

### Observed Facts
- Source type:
- Starting point:
- Explicit timebox:
- AI policy:
- Internet/document policy:
- Required behavior:
- Test/build/run requirement:
- Submission format:
- Documentation requirement:
- Public/fork restriction:

### Unknown / Not stated
- ...
```

중요: 원문에 없는 것을 빈칸으로 두는 것이 틀린 답이 아니다. “모름”을 “아마 이럴 것”으로 채우지 않는다.

---

# 3. 평가 신호를 추론하기

사실을 적은 다음에만 아래를 작성한다.

```md
### Inferred Evaluation Signals
1. Signal:
   - Evidence from README:
   - Why I infer this:

2. Signal:
   - Evidence from README:
   - Why I infer this:

3. Signal:
   - Evidence from README:
   - Why I infer this:
```

예시:

```text
Observed: 기존 테스트가 있으며 깨뜨리지 않아야 한다.
Inferred: 기존 behavior를 존중하고 regression을 막는 능력을 볼 가능성이 높다.
```

“가능성이 높다”라고 표현한다. 공식 평가표가 공개되지 않았다면 단정하지 않는다.

---

# 4. 후보자 Evidence 역추적

과제별로 최소 3개를 적는다.

```md
### Candidate Evidence
- [ ] 실행 명령
- [ ] 핵심 test
- [ ] diff가 작은 이유
- [ ] README / assumptions
- [ ] PR description
- [ ] AI usage / verification
- [ ] known limitation
```

선택 이유를 한 줄씩 붙인다.

---

# 5. 과제별 관찰 포인트

아래는 커리큘럼이 이 공개 과제를 선정한 학습 포인트다. 먼저 원문을 읽은 뒤 비교용으로 본다.

## Simplify Backend

학습 초점:

- starter repository 읽기
- mock grading server / 기존 tests 이해
- 필요한 behavior의 최소 구현
- 기존 test 보존
- repository에서 필요한 위치를 빠르게 찾기

질문:

1. 새 프로젝트를 만들지 않고 기존 구조를 존중해야 할 신호는 무엇인가?
2. grading/test 환경이 있다는 사실이 구현 순서를 어떻게 바꾸는가?
3. “잘 동작하는 큰 rewrite”와 “작은 안전한 patch” 중 어느 쪽이 설명하기 쉬운가?

## FeedMe

학습 초점:

- AI 활용 가능
- 직접 testing 필수
- GitHub Flow / PR
- GitHub Actions check
- 과도한 기술보다 clean implementation

질문:

1. AI 허용과 “직접 테스트” 요구가 동시에 있을 때 무엇을 평가하려는가?
2. PR 형식은 최종 code 외에 어떤 정보를 보여주는가?
3. CI가 있으면 로컬 test는 생략해도 되는가? 왜 아닌가?

## Ello 2025 Full-stack

학습 초점:

- 4~8시간 timebox
- AI assistant 사용을 장려하는 full-stack AI 과제
- voice/session 비동기 흐름
- LLM integration
- architecture/data flow/failure handling
- AI usage 설명

질문:

1. 4~8시간 제한이 기능 욕심을 어떻게 제어해야 하는가?
2. 외부 AI/voice 서비스가 들어오면 성공 경로 외에 무엇을 설명해야 하는가?
3. AI assistant를 썼다는 사실보다 어떤 검증 Evidence가 더 중요한가?

---

# 6. 세 과제 비교표 작성

`assessment_landscape.md`에 최소 다음 열을 사용한다.

```md
| Source | Shape | AI policy | Time/Scope signal | Direct evidence | Inferred signal | Candidate evidence |
|---|---|---|---|---|---|---|
```

한 셀에 장문을 넣기 어렵다면 과제별 상세 섹션으로 분리한다.

---

# 7. Cursor 사용

## Explorer

`lessons/day001/assessment_landscape.md`를 연다.

## Split Editor

왼쪽: 웹 브라우저의 공개 과제 README  
오른쪽: Cursor의 `assessment_landscape.md`

## Search

README가 길면 다음 단어를 검색한다.

```text
time
hours
AI
test
run
submit
PR
fork
assumption
production
```

단어가 있다고 곧바로 평가항목으로 단정하지 말고 문맥을 읽는다.

## Markdown Preview

표와 Mermaid를 확인한다.

---

# 8. AI를 쓰는 경우의 Prompt

Blind read가 끝난 뒤에만 사용한다.

```text
내가 아래 공개 과제 README를 읽고 Observed Facts와 Inferred Signals를 분리했다.
내 분석에서 '원문 사실을 추론처럼 쓰거나, 추론을 사실처럼 단정한 부분'만 찾아줘.
새로운 평가 기준을 만들어내지 말고, 내가 준 근거 안에서 검토해줘.
```

이 Prompt의 목적은 답안을 대신 만드는 것이 아니라 **분류 오류를 찾는 것**이다.

---

# 9. 완료 체크

- [ ] 세 원문을 직접 열어 읽었다.
- [ ] 각 원문에서 사실 5개 이상을 적었다.
- [ ] 원문에 없는 내용은 `Unknown`으로 남겼다.
- [ ] 과제별 평가 신호를 3개 이상 추론했다.
- [ ] 각 추론에 근거를 붙였다.
- [ ] 후보자 Evidence를 과제별 3개 이상 적었다.
- [ ] 세 과제의 공통 평가 신호를 3개 적었다.
- [ ] 세 과제의 차이를 2개 이상 적었다.
- [ ] AI를 썼다면 blind read 이후에 사용했다.
- [ ] 원문 전체를 복제하지 않았다.
