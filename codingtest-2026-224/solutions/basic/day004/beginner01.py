import sys

input = sys.stdin.readline

def solve() -> None:
    # 입력: 4
    #      7 2 9 1
    # 핵심 조건: 정수 N개가 주어진다. 첫 번째 숫자를 출력하라.
    # 예상 시간복잡도: O(N)
    # 예상 공간복잡도: O(N)
    n = int(input())
    
    numbers = list(map(int, input().split()))
    
    print(numbers[0])
    pass


if __name__ == "__main__":
    solve()
