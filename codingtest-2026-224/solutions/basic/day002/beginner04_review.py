import sys

input = sys.stdin.readline


def solve() -> None:
    # [채점] 정답
    # 시간복잡도: O(N)  — 원본과 동일. 1부터 N까지 한 번씩 더한다.
    # 공간복잡도: O(1)  — 누적 변수만 사용한다.
    # 참고: 원본의 변수명 sum은 내장 함수 이름을 가리므로 total로 바꿨다.
    num = int(input())
    total = 0

    for i in range(1, num + 1):
        total += i

    print(total)


if __name__ == "__main__":
    solve()
