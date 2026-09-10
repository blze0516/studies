# Day 4 Practice — 배열/List 기초

## 오늘 사용할 파일

```text
solutions/basic/day004/
├── practice01.py
├── practice02.py
├── practice03.py
├── practice04.py
├── practice05.py
└── integrated.py
```

연습문제 15개는 같은 폴더에서 다음 이름으로 푼다.

```text
beginner01.py ~ beginner05.py
intermediate01.py ~ intermediate05.py
advanced01.py ~ advanced05.py
```

---

# 실습 전 10분 복습

Day 3의 함수 분리 핵심을 확인한다.

```text
입력
→ 처리
→ 출력
```

오늘의 리스트 계산도 가능하면 처리 함수로 분리해 볼 수 있다.

예:

```python
def get_total(numbers):
    total = 0
    for number in numbers:
        total += number
    return total
```

---

# 실습 1 — 리스트 생성과 인덱스

## 목표

- 여러 정수를 List에 저장한다.
- 첫 원소와 마지막 원소를 읽는다.
- 마지막 인덱스가 `N - 1`임을 확인한다.

## 입력

```text
5
8 3 10 4 7
```

## 예상 출력

```text
8 7
```

## 풀이 단계

1. N을 읽는다.
2. N개의 정수를 List로 만든다.
3. `numbers[0]`을 출력한다.
4. `numbers[-1]`을 출력한다.

## 작성 파일

```text
solutions/basic/day004/practice01.py
```

## 기준 코드

```python
n = int(input())
numbers = list(map(int, input().split()))

print(numbers[0], numbers[-1])
```

## 실행 명령

```bash
python solutions/basic/day004/practice01.py
```

## 확인 기준

- [ ] `N = 1`을 테스트했다.
- [ ] `numbers[n]`이 왜 틀린지 설명할 수 있다.
- [ ] `numbers[-1]`의 뜻을 말할 수 있다.

---

# 실습 2 — 리스트 전체 순회

## 목표

List의 값을 처음부터 끝까지 하나씩 출력한다.

## 입력

```text
4
5 8 1 3
```

## 예상 출력

```text
5
8
1
3
```

## 작성 파일

```text
solutions/basic/day004/practice02.py
```

## 기준 코드

```python
n = int(input())
numbers = list(map(int, input().split()))

for number in numbers:
    print(number)
```

## 시간복잡도

`O(N)`

## 확인 기준

- [ ] 값만 필요할 때 인덱스를 쓰지 않아도 된다는 것을 이해했다.
- [ ] N개의 원소가 정확히 N번 출력된다.

---

# 실습 3 — 합계 직접 구하기

## 목표

누적 변수를 이용해 전체 합을 계산한다.

## 입력

```text
5
10 20 30 40 50
```

## 예상 출력

```text
150
```

## 작성 파일

```text
solutions/basic/day004/practice03.py
```

## 기준 코드

```python
n = int(input())
numbers = list(map(int, input().split()))

total = 0

for number in numbers:
    total += number

print(total)
```

## 실행 명령

```bash
python solutions/basic/day004/practice03.py
```

## 확인 기준

- [ ] `total = 0`을 반복문 밖에 두었다.
- [ ] 음수만 있는 입력도 테스트했다.
- [ ] 시간복잡도가 `O(N)`임을 설명할 수 있다.

---

# 실습 4 — 최댓값 직접 구하기

## 목표

첫 번째 값을 초기 최대값으로 잡아 리스트에서 가장 큰 값을 찾는다.

## 입력

```text
5
-10 -3 -20 -4 -8
```

## 예상 출력

```text
-3
```

## 작성 파일

```text
solutions/basic/day004/practice04.py
```

## 기준 코드

```python
n = int(input())
numbers = list(map(int, input().split()))

max_value = numbers[0]

for number in numbers:
    if number > max_value:
        max_value = number

print(max_value)
```

## 직접 만든 반례

```text
1
-5
```

```text
4
-10 -20 -30 -40
```

```text
5
7 7 7 7 7
```

## 확인 기준

- [ ] 초기값을 0으로 두지 않았다.
- [ ] 음수만 있는 입력에서 맞는다.

---

# 실습 5 — 최솟값 직접 구하기

## 목표

첫 번째 값을 초기 최소값으로 잡아 가장 작은 값을 찾는다.

## 입력

```text
6
8 -2 14 3 14 0
```

## 예상 출력

```text
-2
```

## 작성 파일

```text
solutions/basic/day004/practice05.py
```

## 기준 코드

```python
n = int(input())
numbers = list(map(int, input().split()))

min_value = numbers[0]

for number in numbers:
    if number < min_value:
        min_value = number

print(min_value)
```

## 확인 기준

- [ ] `N = 1`을 테스트했다.
- [ ] 최솟값이 마지막 원소인 입력을 테스트했다.

---

# 통합 문제 — 점수 요약

## 목표

한 번의 순회로 다음을 모두 구한다.

```text
합계
최솟값
최댓값
60점 이상 개수
```

## 입력

```text
6
45 60 72 59 100 80
```

## 예상 출력

```text
416
45
100
4
```

## 먼저 손으로 풀기

```text
합계 = 416
최솟값 = 45
최댓값 = 100
60 이상 = 60, 72, 100, 80 → 4개
```

## 풀이 단계

1. 리스트를 읽는다.
2. `total`은 0으로 시작한다.
3. 최소와 최대는 첫 원소로 시작한다.
4. 각 점수를 한 번씩 본다.
5. 합계, 최소, 최대, 합격자 수를 갱신한다.
6. 결과를 출력한다.

## 작성 파일

```text
solutions/basic/day004/integrated.py
```

## 기준 코드

```python
n = int(input())
scores = list(map(int, input().split()))

total = 0
min_score = scores[0]
max_score = scores[0]
pass_count = 0

for score in scores:
    total += score

    if score < min_score:
        min_score = score

    if score > max_score:
        max_score = score

    if score >= 60:
        pass_count += 1

print(total)
print(min_score)
print(max_score)
print(pass_count)
```

## 시간복잡도

`O(N)`

## 공간복잡도

`O(N)`

## 직접 만든 반례

### 반례 1

```text
1
60
```

### 반례 2

```text
4
0 0 0 0
```

### 반례 3

```text
5
100 99 98 97 96
```

### 반례 4

```text
5
59 59 59 59 59
```

### 반례 5

```text
5
-10 0 10 60 100
```

---

# 오늘의 인덱스 실수 실험

다음 코드를 일부러 실행한다.

```python
numbers = [10, 20, 30]
print(numbers[3])
```

예상 결과:

```text
IndexError
```

그 다음 다음 코드로 고친다.

```python
numbers = [10, 20, 30]
print(numbers[2])
```

오늘은 오류를 피하는 것뿐 아니라 **왜 오류가 발생했는지 설명하는 것**까지가 목표다.

---

# 실습 완료 체크리스트

- [ ] 첫 원소와 마지막 원소를 읽을 수 있다.
- [ ] `len`의 의미를 설명할 수 있다.
- [ ] 값을 직접 순회할 수 있다.
- [ ] 합계를 직접 누적할 수 있다.
- [ ] 최댓값을 첫 원소 기준으로 찾을 수 있다.
- [ ] 최솟값을 첫 원소 기준으로 찾을 수 있다.
- [ ] `N = 1` 반례를 확인했다.
- [ ] 마지막 인덱스가 `N - 1`임을 설명할 수 있다.
- [ ] `i + 1` 접근 시 반복 범위를 다시 계산해야 함을 이해했다.
