import sys

input = sys.stdin.readline

def solve() -> None:
    # 입력: 5
    #      12 3 8 -2 7
    # 핵심 조건: 정수 N개가 주어진다.
    #           최댓값에서 최솟값을 뺀 값을 출력하라.
    # 예상 시간복잡도: O(N)
    # 예상 공간복잡도: O(N)
    N = int(input())
    numbers = list(map(int, input().split()))
    
    max_num = numbers[0]
    min_num = numbers[0]
    
    for i in range(1, N):
        if numbers[i] > max_num:
            max_num = numbers[i]
        
        if numbers[i] < min_num:
            min_num = numbers[i]
    
    print(max_num - min_num)

    pass

if __name__ == "__main__":
    solve()
