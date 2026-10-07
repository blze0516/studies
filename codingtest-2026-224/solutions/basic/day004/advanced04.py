import sys

input = sys.stdin.readline

def solve() -> None:
    # 입력: 6
    #      10 13 8 20 19 25
    # 핵심 조건: 정수 N개가 주어진다.
    #           서로 이웃한 두 값에서 뒤의 값이 더 큰 경우에만 상승량을 계산한다.
    #           가장 큰 상승량을 출력하라.
    #           상승한 구간이 하나도 없으면 0을 출력한다.
    # 예상 시간복잡도: O(N)
    # 예상 공간복잡도: O(N)
    N = int(input())
    numbers = list(map(int, input().split()))
    increase_list = []
    
    for i in range(1, N):
        if numbers[i] > numbers[i - 1]:
            increase_list.append(numbers[i] - numbers[i - 1])
    
    if len(increase_list) == 0:
        print(0)
        return 0
    
    max_increase = increase_list[0]
    
    for i in range(1, len(increase_list)):
        if increase_list[i] > max_increase:
            max_increase = increase_list[i]
            
    print(max_increase)
    
    pass

if __name__ == "__main__":
    solve()
