# Day 2 Practice — 변수·조건문·반복문

## 오늘 사용할 파일

실습 코드는 아래 위치에 만든다.

```text
solutions/basic/day002/
├── practice01.py
├── practice02.py
├── practice03.py
├── practice04.py
├── practice05.py
└── integrated.py
```

연습문제 15개는 같은 폴더의 `beginner01.py`부터 `advanced05.py`까지 작성한다.

---

## 시작 전 — Day 1 D+3 재풀이

오늘은 Day 1 D+3 복습일이다.

### 목표

10~15분 안에 아래 세 항목을 다시 구현한다.

1. 60점 이상 PASS
2. 두 수 비교
3. 버스 요금 계산

### 확인 기준

- 경계값을 코드보다 먼저 적었는가?
- 불필요한 출력이 없는가?
- 입력과 출력 형식을 정확히 맞췄는가?

---

# 실습 1 — 현재 금액 계산

## 목표

변수에 값을 저장하고 대입 연산으로 값을 갱신한다.

## 입력

```text
5000 1800
```

## 예상 출력

```text
3200
```

## 풀이 단계

1. `money`, `price`에 입력값을 저장한다.
2. `money`에서 `price`를 뺀다.
3. 남은 `money`를 출력한다.

## 작성 파일

```text
solutions/basic/day002/practice01.py
```

## 기준 코드

```python
money, price = map(int, input().split())

money -= price

print(money)
```

## 실행 명령

```bash
python solutions/basic/day002/practice01.py
```

## 확인 기준

- `money -= price`의 의미를 설명할 수 있다.
- 입력 두 개의 순서를 바꾸지 않았다.

---

# 실습 2 — 놀이기구 탑승 판정

## 목표

두 조건을 `and`로 결합한다.

## 입력

```text
15 130
```

## 예상 출력

```text
RIDE
```

## 풀이 단계

1. 나이와 키를 읽는다.
2. 나이가 14 이상인지 확인한다.
3. 키가 120 이상인지 확인한다.
4. 둘 다 참일 때만 `RIDE`를 출력한다.

## 작성 파일

```text
solutions/basic/day002/practice02.py
```

## 기준 코드

```python
age, height = map(int, input().split())

if age >= 14 and height >= 120:
    print("RIDE")
else:
    print("NO")
```

## 직접 만든 반례

```text
14 120
13 200
20 119
13 119
```

## 확인 기준

- `and`와 `or`의 차이를 말할 수 있다.
- `14`, `120` 경계값을 테스트했다.

---

# 실습 3 — 1부터 N까지 짝수 합

## 목표

`for`, `range`, 조건문, 누적 변수를 함께 사용한다.

## 입력

```text
6
```

## 예상 출력

```text
12
```

## 손으로 먼저 풀기

```text
1 제외
2 더하기 → 2
3 제외
4 더하기 → 6
5 제외
6 더하기 → 12
```

## 작성 파일

```text
solutions/basic/day002/practice03.py
```

## 기준 코드

```python
n = int(input())

total = 0

for number in range(1, n + 1):
    if number % 2 == 0:
        total += number

print(total)
```

## 시간복잡도

`O(N)`

## 확인 기준

- `n + 1`을 쓰는 이유를 설명할 수 있다.
- `total = 0`의 초기값 의미를 설명할 수 있다.

---

# 실습 4 — 점수 등급

## 목표

여러 구간을 `if / elif / else`로 빠짐없이 나눈다.

## 입력

```text
83
```

## 예상 출력

```text
B
```

## 작성 파일

```text
solutions/basic/day002/practice04.py
```

## 기준 코드

```python
score = int(input())

if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 60:
    print("C")
else:
    print("F")
```

## 조건 누락 검증

아래 값으로 실행한다.

```text
90
89
80
79
60
59
```

## 확인 기준

- 조건을 높은 점수부터 검사한다.
- 모든 점수가 정확히 한 분기로 들어간다.

---

# 실습 5 — N개의 점수에서 합격자 수 세기

## 목표

입력을 N번 받고 조건을 만족한 횟수를 센다.

## 입력

```text
5
70
59
60
100
42
```

## 예상 출력

```text
3
```

## 작성 파일

```text
solutions/basic/day002/practice05.py
```

## 기준 코드

```python
import sys

input = sys.stdin.readline

n = int(input())
pass_count = 0

for _ in range(n):
    score = int(input())

    if score >= 60:
        pass_count += 1

print(pass_count)
```

## 시간복잡도

`O(N)`

## 확인 기준

- N명의 점수를 정확히 N번 읽는다.
- 60점을 합격으로 처리한다.
- 합격자가 0명인 경우도 처리한다.

---

# 통합 문제 — 출석 보상 계산기

## 목표

조건 구간과 반복을 결합한다.

## 입력 예시

```text
5
20
60
135
45
100
```

## 예상 출력

```text
8 3
```

## 작성 파일

```text
solutions/basic/day002/integrated.py
```

## 풀이 전 체크

- [ ] 보상 구간을 표로 적었다.
- [ ] `120`, `60`, `30`을 경계값으로 표시했다.
- [ ] 총점 변수와 날짜 수 변수를 분리했다.
- [ ] 보상 조건은 서로 하나만 적용되도록 했다.
- [ ] 60분 이상 날짜 수는 별도 `if`로 검사했다.

## 기준 코드

```python
import sys

input = sys.stdin.readline

n = int(input())
total_point = 0
over_sixty_count = 0

for _ in range(n):
    study_time = int(input())

    if study_time >= 120:
        total_point += 3
    elif study_time >= 60:
        total_point += 2
    elif study_time >= 30:
        total_point += 1

    if study_time >= 60:
        over_sixty_count += 1

print(total_point, over_sixty_count)
```

## 직접 만든 반례

### 경계값 120

```text
1
120
```

예상:

```text
3 1
```

### 경계값 60

```text
1
60
```

예상:

```text
2 1
```

### 경계값 30

```text
1
30
```

예상:

```text
1 0
```

### 30 미만

```text
1
29
```

예상:

```text
0 0
```

---

# 오늘의 실행 루틴

Cursor Terminal에서 다음 순서로 실행한다.

```bash
python solutions/basic/day002/practice01.py
python solutions/basic/day002/practice02.py
python solutions/basic/day002/practice03.py
python solutions/basic/day002/practice04.py
python solutions/basic/day002/practice05.py
python solutions/basic/day002/integrated.py
```

각 파일마다 최소 세 개의 입력을 직접 넣어 본다.

---

# 오늘의 제출 전 체크리스트

- [ ] `=`와 `==`를 구분했다.
- [ ] `이상/초과/이하/미만`을 올바르게 번역했다.
- [ ] `and`와 `or`가 문제 문장과 일치한다.
- [ ] `if / elif / else` 구간이 빠지지 않았다.
- [ ] `range`의 끝값이 포함되지 않는다는 점을 반영했다.
- [ ] 반복 횟수가 정확하다.
- [ ] 누적 변수 초기값이 있다.
- [ ] `while`을 사용했다면 종료 방향으로 값이 변한다.
- [ ] 최소 경계값 3개를 테스트했다.
- [ ] 문제에서 요구하지 않은 문자열을 출력하지 않는다.
