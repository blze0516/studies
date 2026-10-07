# Day 5 Exercises — Repository 초기화·Git 전략

> 총 15문제. 먼저 혼자 풀고 `exercise-solutions.md`에 답을 작성한다. 모범답안은 기본 제공하지 않는다.

## 초급 5문제

### 1
Working Tree, Staging Area, Commit을 각각 한 문장으로 설명하라.

### 2
`git status`와 `git diff`가 보여 주는 정보의 차이를 설명하라.

### 3
`update`라는 commit message가 좋지 않은 이유를 두 가지 적어라.

### 4
다음 중 commit 직전에 가장 직접적으로 확인해야 할 명령을 고르고 이유를 적어라.

```text
git diff --staged
git tag
git clone
```

### 5
Tag와 branch의 차이를 쉬운 말로 설명하라.

## 중급 5문제

### 6
README 오타 수정, 예약 생성 규칙 수정, 검증 체크리스트 추가가 동시에 working tree에 있다. commit을 어떻게 나눌지 제안하라.

### 7
`git add .` 뒤 `.env`가 stage된 것을 발견했다. commit 전에 어떻게 대응할지 순서와 명령을 작성하라.

### 8
4시간 Take-home에서 `main`, `develop`, `release`, 기능 branch 6개를 사용하려 한다. 장단점을 분석하고 더 단순한 대안을 제안하라.

### 9
`git log --oneline --decorate --graph --all`을 PR 전 확인하는 이유를 설명하라.

### 10
기능과 테스트를 같은 commit에 넣는 경우와 별도 commit으로 나누는 경우의 trade-off를 설명하라.

## 고급 5문제

### 11
작업 branch의 5개 commit 중 2개가 순수 formatting 변경이라 핵심 diff를 읽기 어렵게 만든다. 제출 20분 전이라면 어떤 판단을 할지 근거와 함께 작성하라.

### 12
이미 commit한 뒤 secret이 포함된 것을 발견했다. “파일에서 삭제하고 다음 commit을 하면 끝”이 아닌 이유를 설명하라.

### 13
평가자가 commit history를 본다고 알려진 과제에서 `initial commit` 하나만 제출하는 전략의 장단점을 분석하라.

### 14
PR branch 전체 변경을 리뷰할 때 “공통 출발점 이후의 변경”을 보는 것이 왜 중요한지 설명하라.

### 15
60분 live change request가 들어왔다. 별도 branch/commit을 만들지, 기존 branch에서 바로 수정할지 결정하는 기준을 시간·위험·리뷰 관점으로 제시하라.
