import sys

input = sys.stdin.readline

def solve() -> None:
    # 입력: 5
    #      4 8 1 10 3
    # 핵심 조건: 정수 N개가 주어진다.
    #           서로 이웃한 두 원소의 합 중 가장 큰 값을 출력하라.
    # 예상 시간복잡도: O(N)
    # 예상 공간복잡도: O(N)
    N = int(input())
    numbers = list(map(int, input().split()))
    sum_list = []
    
    for i in range(1, N):
        sum_list.append(numbers[i] + numbers[i - 1])
        
    max_num = sum_list[0]
    
    for i in range(1, len(sum_list)):
        if sum_list[i] > max_num:
            max_num = sum_list[i]
            
    print(max_num)
    
    pass


if __name__ == "__main__":
    solve()
