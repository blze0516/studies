# Day 5 Practice — Git 흐름 직접 수행

## 이 파일의 역할

`lecture.md`의 실습예제는 설명을 보면서 따라 하는 **Guided Practice**다.

이 `practice.md`에서는 명령을 그대로 복사하는 데서 끝내지 않고, 본인이 변경 범위와 commit 경계를 결정한다.

## 어디에 작업하나?

```text
take-home-2026/
└── drills/
    └── repository/
        └── day005-git-flow/
```

제공 zip에는 `.git` 폴더가 없다. **직접 `git init`해야 한다.**

---

## 과제 상황

당신은 짧은 예약 Take-home을 시작했다.

현재 문서에는 다음 문제가 있다.

- 예약 규칙이 모호하다.
- PR 설명이 비어 있다.
- Git 전략을 아직 결정하지 않았다.

평가자는 최종 파일뿐 아니라 변경 흐름도 확인할 수 있다고 가정한다.

## 해야 할 일

### 1. Repository 초기화

직접 초기화하고 starter snapshot을 commit한다.

검증해야 할 것:

```text
현재 branch 이름
untracked files
첫 commit 내용
```

### 2. 작업 branch 생성

branch 이름은 작업 목적이 드러나게 직접 정한다.

금지 예:

```text
work
new
branch1
```

### 3. 예약 규칙 명확화

`reservation-rules.md`의 TODO를 직접 해결한다.

주의:

- 강의에서 배우지 않은 DB lock 같은 미래 Day 개념을 답으로 요구하지 않는다.
- 지금은 요구사항 문장 자체를 명확하게 만드는 것이 목적이다.

### 4. 첫 번째 commit

다음 근거를 적은 뒤 commit한다.

```text
이 commit의 한 가지 목적:
왜 별도 commit인가:
commit message:
```

### 5. PR Draft 작성

`PR_DRAFT.md`를 자신의 실제 diff 기준으로 작성한다.

최소 항목:

```text
What
Why
How verified
Risk / limitation
```

### 6. 두 번째 commit

PR draft 변경을 별도 commit으로 할지 첫 변경과 합칠지 직접 판단한다.

이미 첫 commit이 끝났으므로 오늘 실습에서는 **별도 commit**으로 남겨 두 변경을 비교한다.

### 7. 전체 branch diff review

직접 실행한다.

```bash
git status
git log --oneline --decorate --graph --all
git diff main...HEAD
```

다음 항목을 체크한다.

- [ ] 요구사항 밖 파일 없음
- [ ] secret 없음
- [ ] debug/임시 문구 없음
- [ ] commit별 목적 설명 가능
- [ ] PR Draft가 실제 diff와 일치

### 8. Tag

마지막 상태가 Day 5 완료 기준을 만족하면 annotated tag를 만든다.

### 9. `GIT_STRATEGY.md` 작성

다음 파일의 TODO를 직접 채운다.

```text
docs/reviews/GIT_STRATEGY.md
```

---

# 실습 완료 Evidence

아래 결과를 `review.md`에 직접 기록한다.

```text
git status 결과 요약:
현재 branch:
commit 개수:
commit 제목들:
tag:
branch diff에서 발견한 실수:
수정한 내용:
```

# Self Review

1. commit을 단순히 파일별로 나누지 않았는가?
2. 각 commit에 하나의 이유가 있는가?
3. commit 전에 staged diff를 실제로 읽었는가?
4. Git 작업 자체가 실습 목적보다 과도하게 복잡해지지 않았는가?
5. 지금 이 history를 면접관에게 2분 안에 설명할 수 있는가?
