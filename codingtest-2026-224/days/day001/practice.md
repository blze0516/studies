# Day 1 Practice

## 오늘 사용할 파일

- `templates/python_fastio.py`
- 직접 생성할 연습 파일 권장 위치: `solutions/basic/day001_*.py`
- 강의: `days/day001/lecture.md`
- 문제: `days/day001/exercises.md`
- 복기: `days/day001/review.md`

## 시작 전 환경 확인

Cursor에서 프로젝트 폴더 `codingtest-2026-224`를 연다.

Terminal에서:

```bash
python --version
```

기대 기준:

```text
Python 3.14.7
```

Cursor 버전은 앱의 About/Update 화면에서 `3.18` 기준으로 사용한다.

---

## 실습 1 — Hello 입력/출력

- 목표: 문자열 한 줄을 읽고 정확한 형식으로 출력
- 권장 파일: `solutions/basic/day001_hello.py`

### 입력

```text
Nara
```

### 예상 출력

```text
Hello, Nara!
```

### 풀이 단계

1. `name = input().strip()`으로 읽기
2. f-string으로 출력
3. 불필요한 디버그 문장 없는지 확인

### 실행 명령

```bash
python solutions/basic/day001_hello.py
```

### 확인 기준

- 이름이 한 글자여도 정상 동작
- 이름 중간 공백은 유지
- 출력 끝 `!` 포함

---

## 실습 2 — 두 수의 합

- 목표: `split`, `map`, `int` 사용
- 권장 파일: `solutions/basic/day001_sum.py`

### 입력

```text
7 13
```

### 예상 출력

```text
20
```

### 손으로 먼저 계산

7 + 13 = 20

### 풀이 단계

1. 한 줄을 공백으로 나누기
2. 각 문자열을 정수로 변환
3. 합 출력

### 반례

```text
0 0
-5 5
1000000000 1000000000
```

---

## 실습 3 — PASS / FAIL

- 목표: `if / else`, 경계값 확인
- 권장 파일: `solutions/basic/day001_pass.py`

### 입력

```text
60
```

### 예상 출력

```text
PASS
```

### 반드시 테스트

| 입력 | 출력 |
|---:|---|
| 59 | FAIL |
| 60 | PASS |
| 61 | PASS |

### 확인 기준

`score > 60`으로 잘못 쓰지 않았는지 확인한다.

---

## 실습 4 — 양수 개수

- 목표: 리스트 입력 + 반복문 + 조건문을 맛보기로 연결
- 권장 파일: `solutions/basic/day001_positive_count.py`

### 입력

```text
5
-2 0 7 3 -1
```

### 예상 출력

```text
2
```

### 풀이 단계

1. N 읽기
2. N개 정수 목록 읽기
3. 원소를 한 번씩 확인
4. `x > 0`이면 count 증가
5. count 출력

### 복잡도 확인

N개를 한 번씩 보므로 O(N).

---

## 실습 5 — 두 수 비교

- 목표: `if / elif / else` 세 갈래 분기
- 권장 파일: `solutions/basic/day001_compare.py`

### 규칙

- A > B → A
- A < B → B
- A == B → SAME

### 반드시 테스트

```text
1 2
2 1
2 2
```

---

## 통합 문제 — 버스 요금 계산기

- 목표: 입력 + 조건문 + 경계값 + O(1) 분석
- 권장 파일: `solutions/basic/day001_bus_fare.py`

### 규칙

- 7세 이하 → 0
- 8~18세 → `fare // 2`
- 19세 이상 → `fare`

### 입력

```text
15 1400
```

### 예상 출력

```text
700
```

### 구현 전 체크

- `7`, `8`, `18`, `19`를 종이에 표시
- `fare`가 홀수일 때 `//` 결과 확인
- 분기는 세 개면 충분한지 확인

### 직접 만든 반례

```text
7 1400   -> 0
8 1400   -> 700
18 1501  -> 750
19 1501  -> 1501
```

---

## 기본 템플릿 직접 손코딩

강의를 보지 않고 다음 구조를 직접 작성한다.

```python
import sys

input = sys.stdin.readline


def solve() -> None:
    pass


if __name__ == "__main__":
    solve()
```

### 확인 기준

- `solve()`가 실제로 호출되는가?
- 들여쓰기가 맞는가?
- 문자열 입력에서는 개행 제거를 의식하는가?

---

## 오늘의 20분 마무리 루틴

1. 실습 1~5 중 틀린 것만 다시 작성 — 10분
2. 버스 요금 경계값 4개 직접 테스트 — 3분
3. O(1), O(N), O(N²)을 각각 한 문장으로 설명 — 3분
4. `templates/python_fastio.py`를 안 보고 다시 입력 — 4분

완료 후 `review.md`의 체크박스를 채운다.
