# Day 5 Practice — 문자열 기초

## 오늘 사용할 파일

```text
solutions/basic/day005/
├── practice01.py
├── practice02.py
├── practice03.py
├── practice04.py
├── practice05.py
└── integrated.py
```

Cursor에서 프로젝트 루트 `codingtest-2026-224`를 연 뒤 위 폴더에 파일을 만든다.

실행 예:

```bash
python solutions/basic/day005/practice01.py
```

---

## 시작 전 10분 복습

Day 4의 D+3 예정일은 2026-09-13이었다.

아직 못 했다면 오늘 시작 전에 다음 중 하나를 빈 파일에서 다시 구현한다.

- List 전체 합
- 최댓값 직접 찾기
- 양수 개수 세기

이미 완료했다면 바로 Day 5로 넘어간다.

---

## 실습 1 — 첫 문자와 마지막 문자

### 목표

- 문자열 인덱스 이해
- `len`과 마지막 인덱스 연결

### 입력

```text
coding
```

### 예상 출력

```text
c g
```

### 풀이 단계

1. 문자열을 입력받는다.
2. 첫 인덱스 0의 문자를 확인한다.
3. 마지막 문자를 확인한다.
4. 두 문자를 출력한다.

### 직접 작성할 기본 코드 형태

```python
word = input().strip()

print(word[0], word[-1])
```

### 실행 명령

```bash
python solutions/basic/day005/practice01.py
```

### 확인 기준

- 길이 1인 입력에서도 오류가 없어야 한다.
- 첫 문자와 마지막 문자를 정확히 출력해야 한다.

### 반례

```text
a
```

```text
ABC
```

```text
12345
```

---

## 실습 2 — 단어 개수

### 목표

- `split` 결과가 List임을 이해
- `len`으로 단어 개수 계산

### 입력

```text
we study python
```

### 예상 출력

```text
3
```

### 풀이 단계

1. 한 줄 문자열을 입력받는다.
2. `split()`으로 단어를 나눈다.
3. 결과 List 길이를 출력한다.

### Python 전체 코드

```python
text = input().strip()
words = text.split()

print(len(words))
```

### 실행 명령

```bash
python solutions/basic/day005/practice02.py
```

### 확인 기준

- 단어 하나일 때 1을 출력한다.
- 여러 공백이 있어도 단어 수를 올바르게 센다.

### 반례

```text
hello
```

```text
red   blue
```

```text
one two three four
```

---

## 실습 3 — 가운데 세 글자

### 목표

- slice 시작 포함, 끝 제외 규칙 이해

### 문제 조건

길이가 5 이상인 문자열이 주어진다. 인덱스 1부터 3까지 세 글자를 출력한다.

### 입력

```text
python
```

### 예상 출력

```text
yth
```

### 풀이 단계

1. 필요한 실제 인덱스를 적는다: 1, 2, 3.
2. 끝 위치는 포함되지 않으므로 4를 사용한다.
3. `text[1:4]`를 출력한다.

### Python 전체 코드

```python
text = input().strip()

print(text[1:4])
```

### 실행 명령

```bash
python solutions/basic/day005/practice03.py
```

### 확인 기준

`1:4`가 정확히 3글자를 가져오는 이유를 말로 설명할 수 있어야 한다.

### 반례

```text
abcde
```

```text
12345
```

```text
ABCDE
```

---

## 실습 4 — 구분자 제거

### 목표

- `replace`로 새 문자열 생성
- 원본과 결과 구분

### 입력

```text
2026-09-14
```

### 예상 출력

```text
20260914
```

### 풀이 단계

1. 입력 문자열을 받는다.
2. `-`를 빈 문자열로 바꾼다.
3. 새 문자열을 출력한다.

### Python 전체 코드

```python
text = input().strip()
changed = text.replace("-", "")

print(changed)
```

### 실행 명령

```bash
python solutions/basic/day005/practice04.py
```

### 확인 기준

- 바꿀 문자가 없어도 원본이 그대로 출력되어야 한다.
- `""`와 `" "`의 차이를 설명할 수 있어야 한다.

### 반례

```text
20260914
```

```text
-a-b-
```

```text
---
```

---

## 실습 5 — 개수와 첫 위치

### 목표

- `count`와 `index` 역할 구분
- 없는 값에 대한 안전 처리

### 입력

첫째 줄: 문자열
둘째 줄: 찾을 문자 하나

```text
banana
a
```

### 예상 출력

```text
3
1
```

### 풀이 단계

1. `count`로 등장 개수를 센다.
2. 대상이 문자열 안에 있는지 확인한다.
3. 있으면 `index`로 첫 위치를 구한다.
4. 없으면 -1을 사용한다.

### Python 전체 코드

```python
text = input().strip()
target = input().strip()

print(text.count(target))

if target in text:
    print(text.index(target))
else:
    print(-1)
```

### 실행 명령

```bash
python solutions/basic/day005/practice05.py
```

### 확인 기준

- 대상이 없을 때 오류가 나지 않아야 한다.
- `count`와 `index` 출력 의미를 구분해야 한다.

### 반례

```text
banana
z
```

```text
aaaa
a
```

```text
hello
h
```

---

## 통합 문제 — 메시지 정리기

### 목표

오늘 배운 다섯 가지 문자열 처리 기능을 한 문제 안에서 연결한다.

### 입력

```text
java-and-python
```

### 예상 출력

```text
java and python
3
java 
3
1
```

### 풀이 순서

```text
replace
→ split
→ slice
→ count
→ index
```

### Python 전체 코드

```python
message = input().strip()

cleaned = message.replace("-", " ")
words = cleaned.split()
prefix = cleaned[:5]
a_count = cleaned.count("a")

if "a" in cleaned:
    first_a = cleaned.index("a")
else:
    first_a = -1

print(cleaned)
print(len(words))
print(prefix)
print(a_count)
print(first_a)
```

### 실행 명령

```bash
python solutions/basic/day005/integrated.py
```

### 직접 만든 반례

```text
hello-world
```

```text
abc
```

```text
a-a-a
```

```text
python
```

---

## 오늘 실습 완료 체크

- [ ] 문자열 첫 문자와 마지막 문자를 읽을 수 있다.
- [ ] `split()` 결과가 List라는 것을 설명할 수 있다.
- [ ] slice의 끝 위치가 제외된다는 것을 설명할 수 있다.
- [ ] `replace` 결과를 새 변수에 저장할 수 있다.
- [ ] `count`와 `index` 차이를 설명할 수 있다.
- [ ] `index` 대상이 없을 때 안전하게 처리할 수 있다.
- [ ] 각 문제에서 반례를 최소 3개 실행했다.
