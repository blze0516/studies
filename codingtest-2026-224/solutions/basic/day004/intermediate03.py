import sys

input = sys.stdin.readline

def solve() -> None:
    # 입력: 5 10
    #      3 10 15 7 12
    # 핵심 조건: 정수 N개와 기준값 K가 주어진다.
    #           N개의 값 중 K 이상인 값의 개수를 출력하라.
    # 예상 시간복잡도: O(N)
    # 예상 공간복잡도: O(N)
    N, K = map(int, input().split())    
    numbers = list(map(int, input().split()))
    count = 0
    
    for number in numbers:
        if number >= K:
            count += 1

    print(count)
    pass


if __name__ == "__main__":
    solve()
