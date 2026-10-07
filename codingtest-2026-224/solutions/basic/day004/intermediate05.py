import sys

input = sys.stdin.readline

def solve() -> None:
    # 입력: 5
    #      8 3 10 4 7
    # 핵심 조건: 정수 N개가 주어진다.
    #           첫 번째 값과 마지막 값의 합을 출력하라.
    # 예상 시간복잡도: O(N)
    # 예상 공간복잡도: O(N)
    N = int(input())
    numbers = list(map(int, input().split()))
        
    print(numbers[0] + numbers[N - 1])

    pass


if __name__ == "__main__":
    solve()
