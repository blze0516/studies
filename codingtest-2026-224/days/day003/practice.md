# Day 3 Practice — 함수 분리

## 오늘 사용할 파일

실습 코드는 아래 위치에 만든다.

```text
solutions/basic/day003/
├── practice01.py
├── practice02.py
├── practice03.py
├── practice04.py
└── integrated.py
```

연습문제 15개는 같은 폴더의 `beginner01.py`부터 `advanced05.py`까지 작성한다.

---

## 실습 전 체크

Day 2에서 배운 내용을 5분만 확인한다.

```text
60 이상을 Python 비교식으로 쓰기
1부터 N까지 반복하는 range 쓰기
합계를 누적하는 변수 만들기
```

함수 안에서도 결국 조건문과 반복문을 사용하므로 Day 2 문법이 그대로 이어진다.

---

# 실습 1 — 두 수 중 큰 값

## 목표

비교 작업을 함수 하나로 분리한다.

## 입력

```text
7 12
```

## 예상 출력

```text
12
```

## 먼저 손으로 풀기

```text
7과 12 비교
12 선택
```

## 풀이 단계

1. `get_larger(a, b)` 함수를 정의한다.
2. 두 값을 비교한다.
3. 더 큰 값을 `return`한다.
4. 입력은 함수 밖에서 받는다.
5. 반환값을 출력한다.

## 작성 파일

```text
solutions/basic/day003/practice01.py
```

## 기준 코드

```python
def get_larger(a, b):
    if a >= b:
        return a
    return b


a, b = map(int, input().split())
answer = get_larger(a, b)
print(answer)
```

## 실행 명령

```bash
python solutions/basic/day003/practice01.py
```

## 확인 기준

- 함수 이름만 보고 역할을 설명할 수 있다.
- `return`과 `print`의 차이를 설명할 수 있다.
- `5 5`, `-3 -10`을 테스트했다.

---

# 실습 2 — 합격 여부

## 목표

조건 판단을 함수로 만들고 문자열을 반환한다.

## 입력

```text
72
```

## 예상 출력

```text
PASS
```

## 풀이 단계

1. `get_result(score)` 함수를 만든다.
2. 60 이상이면 `PASS`를 반환한다.
3. 그렇지 않으면 `FAIL`을 반환한다.
4. 마지막에 한 번 출력한다.

## 작성 파일

```text
solutions/basic/day003/practice02.py
```

## 기준 코드

```python
def get_result(score):
    if score >= 60:
        return "PASS"
    return "FAIL"


score = int(input())
print(get_result(score))
```

## 직접 만든 반례

```text
60
59
100
```

## 확인 기준

- 경계값 60을 포함했다.
- 함수가 직접 입력을 읽지 않는다.
- 함수가 계산 결과를 반환한다.

---

# 실습 3 — 짝수 개수

## 목표

반복문이 들어간 처리 함수를 만든다.

## 입력

```text
7
```

## 예상 출력

```text
3
```

## 먼저 손으로 풀기

```text
2, 4, 6
총 3개
```

## 작성 파일

```text
solutions/basic/day003/practice03.py
```

## 기준 코드

```python
def count_even(n):
    count = 0

    for number in range(1, n + 1):
        if number % 2 == 0:
            count += 1

    return count


n = int(input())
answer = count_even(n)
print(answer)
```

## 시간복잡도

`O(N)`

## 확인 기준

- 반복문이 함수 안에 있어도 복잡도가 `O(N)`인 이유를 말할 수 있다.
- `n = 1`, `n = 2`, `n = 10`을 테스트했다.

---

# 실습 4 — 합격자 수

## 목표

리스트 전체를 처리하는 함수를 만든다.

## 입력

```text
5
45 60 72 59 100
```

## 예상 출력

```text
3
```

## 풀이 단계

1. 입력에서 점수 리스트를 만든다.
2. `count_passed(scores)`에 리스트를 전달한다.
3. 함수 내부에서 각 점수를 확인한다.
4. 60 이상인 점수의 개수를 반환한다.
5. 반환값을 출력한다.

## 작성 파일

```text
solutions/basic/day003/practice04.py
```

## 기준 코드

```python
def count_passed(scores):
    count = 0

    for score in scores:
        if score >= 60:
            count += 1

    return count


n = int(input())
scores = list(map(int, input().split()))

answer = count_passed(scores)
print(answer)
```

## 시간복잡도

`O(N)`

## 공간복잡도

점수 리스트를 저장하므로 `O(N)`

## 확인 기준

- 함수의 입력이 `scores` 리스트라는 점을 설명할 수 있다.
- 모두 탈락하는 경우와 모두 합격하는 경우를 테스트했다.

---

# 통합 문제 — 할인 후 구매 가능 여부

## 목표

계산 함수와 판정 함수를 서로 분리한다.

## 입력

```text
8000 10000 30
```

## 예상 출력

```text
BUY
```

## 작성 파일

```text
solutions/basic/day003/integrated.py
```

## 풀이 단계

1. `get_final_price`가 할인된 가격을 계산한다.
2. `can_buy`가 구매 가능 여부를 반환한다.
3. 입력은 메인 영역에서 받는다.
4. 출력도 마지막에 처리한다.

## 기준 코드

```python
def get_final_price(price, discount):
    discount_amount = price * discount // 100
    return price - discount_amount


def can_buy(money, final_price):
    return money >= final_price


money, price, discount = map(int, input().split())

final_price = get_final_price(price, discount)

if can_buy(money, final_price):
    print("BUY")
else:
    print("NO")
```

## 직접 만든 반례

```text
7000 10000 30
6999 10000 30
10000 10000 0
0 10000 100
```

## 확인 기준

- 함수별 역할을 한 문장으로 말할 수 있다.
- 인자의 순서를 바꾸지 않았다.
- `return`된 값을 다음 함수에 전달하는 흐름을 이해했다.

---

# 오늘의 함수명과 역할 기록

실습을 끝낸 뒤 아래 표를 직접 채운다.

| 파일 | 함수명 | 입력 | 역할 | 반환값 |
|---|---|---|---|---|
| practice01.py |  |  |  |  |
| practice02.py |  |  |  |  |
| practice03.py |  |  |  |  |
| practice04.py |  |  |  |  |
| integrated.py |  |  |  |  |

---

# 실행 명령 모음

```bash
python solutions/basic/day003/practice01.py
python solutions/basic/day003/practice02.py
python solutions/basic/day003/practice03.py
python solutions/basic/day003/practice04.py
python solutions/basic/day003/integrated.py
```
