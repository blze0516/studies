import sys

input = sys.stdin.readline

def solve() -> None:
    # 입력: 6
    #      -3 0 4 8 -1 2
    # 핵심 조건: 정수 N개 중 양수만 더한 결과를 출력하라.
    #           0은 양수에 포함하지 않는다.
    # 1부터 N까지의 수 중 K의 배수 개수를 세는 count_multiples(n, k) 함수를 작성하라. 
    # 예상 시간복잡도: O(N)
    # 예상 공간복잡도: O(N)
    n = int(input())
    numbers = list(map(int, input().split()))
    positive_sum = 0

    for number in numbers:
        if number > 0:
            positive_sum += number
            
    print(positive_sum)

    pass


if __name__ == "__main__":
    solve()
