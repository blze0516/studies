import sys

input = sys.stdin.readline

def solve() -> None:
    # 입력: 5
    #      -8 -3 -20 -1 -7
    # 핵심 조건: 정수 N개 중 가장 큰 수를 직접 찾아 출력하라.
    # 예상 시간복잡도: O(N)
    # 예상 공간복잡도: O(N)
    n = int(input())
    numbers = list(map(int, input().split()))
    
    max_number = numbers[0]
    
    for i in range(1, n):
        if numbers[i] > max_number:
            max_number = numbers[i]
            
    print(max_number)    
    
    pass


if __name__ == "__main__":
    solve()
