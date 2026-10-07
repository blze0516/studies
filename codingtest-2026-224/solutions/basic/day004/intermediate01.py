import sys

input = sys.stdin.readline

def solve() -> None:
    # 입력: 5
    #      8 3 12 -4 7
    # 핵심 조건: 정수 N개 중 가장 작은 수를 직접 찾아 출력하라.
    # 예상 시간복잡도: O(N)
    # 예상 공간복잡도: O(N)
    N = int(input())
    numbers = list(map(int, input().split()))
    
    min_number = numbers[0]
    
    for i in range(1, N):
        if numbers[i] < min_number:
            min_number = numbers[i]
            
    print(min_number)

    pass


if __name__ == "__main__":
    solve()
