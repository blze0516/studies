import sys

input = sys.stdin.readline
def solve() -> None:
    # 입력: 4
    #      5 10 15 20
    # 핵심 조건: 정수 N개의 합을 반복문으로 직접 계산해 출력하라.
    # 예상 시간복잡도: O(N)
    # 예상 공간복잡도: O(N)
    n = int(input())
    numbers = list(map(int, input().split()))
    total = 0
    
    for number in numbers:
        total += number
    
    print(total)
        
    pass


if __name__ == "__main__":
    solve()
