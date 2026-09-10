import sys

input = sys.stdin.readline

def get_sum(n):
    sum = 0
    for i in range(1, n + 1):
        sum += i
    return sum

def solve() -> None:
    # 입력: 30000
    # 핵심 조건: 정수 N이 주어진다. get_sum(n) 함수를 작성해 1부터 N까지의 합을 반복문으로 계산해 반환하라.
    # 예상 시간복잡도: O(N)
    N = int(input())
            
    print(get_sum(N))

    pass


if __name__ == "__main__":
    solve()
