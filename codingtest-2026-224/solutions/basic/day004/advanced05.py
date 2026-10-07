import sys

input = sys.stdin.readline

def solve() -> None:
    # 입력: 5
    #      10 20 20 5 3
    # 핵심 조건: 정수 N개가 주어진다.
    #           전체 합에서 최댓값 하나만 제외한 합을 출력하라.
    #           최댓값이 여러 번 등장하더라도 하나만 제외한다.
    # 예상 시간복잡도: O(N)
    # 예상 공간복잡도: O(N)
    N = int(input())
    numbers = list(map(int, input().split()))
    max_index = 0
    max_num = numbers[0]
    
    for i in range(1, N):
        if numbers[i] > max_num:
            max_num = numbers[i]
            max_index = i
    
    sum = 0
    
    for i in range(0, N):
        if i != max_index:
            sum += numbers[i]
            
    print(sum)
    
    pass

if __name__ == "__main__":
    solve()
