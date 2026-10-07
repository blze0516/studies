import sys

input = sys.stdin.readline

def solve() -> None:
    # 입력: 6
    #      1 2 4 7 9 10
    # 핵심 조건: 정수 N개 중 짝수의 개수를 출력하라.
    # 예상 시간복잡도: O(N)    
    # 예상 공간복잡도: O(N)
    N = int(input())
    numbers = list(map(int, input().split()))
    count = 0
    for number in numbers:
        if number % 2 == 0:
            count += 1
            
    print(count)

    pass


if __name__ == "__main__":
    solve()
