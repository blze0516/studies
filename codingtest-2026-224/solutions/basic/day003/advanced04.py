import sys

input = sys.stdin.readline

def sum_at_least(numbers, k):
    sum = 0
    for number in numbers:
        if(number >= k):
            sum += number
    return sum

def solve() -> None:
    # 입력: 6 5
    #       1 5 7 3 9 2
    # 핵심 조건: N개의 정수와 기준값 K가 주어진다.
    # K 이상인 값들만 더해 반환하는 sum_at_least(numbers, k) 함수를 작성하라.
    # 예상 시간복잡도: O(N)
    N, K = map(int, input().split())
    numbers = list(map(int, input().split()))
    
    print(sum_at_least(numbers, K))    
    
    pass

if __name__ == "__main__":
    solve()
