import sys

input = sys.stdin.readline

def solve() -> None:
    # 입력: 5
    #      10 20 30 40 50
    # 핵심 조건: 정수 N개가 주어진다.
    #           전체 합계를 N으로 나눈 평균 이상인 원소의 개수를 출력하라.
    #           평균은 실수 나눗셈을 사용한다.
    # 예상 시간복잡도: O(N)
    # 예상 공간복잡도: O(N)
    N = int(input())
    numbers = list(map(int, input().split()))
    total = 0
    count = 0
    
    for number in numbers:
        total += number
        
    average = total / N
    
    for number in numbers:
        if number >= average:
            count += 1
    print(count)
    
    pass


if __name__ == "__main__":
    solve()
