import sys

input = sys.stdin.readline

def get_positive_info(numbers):
    sum = 0
    count = 0
    for num in numbers:
        if num > 0:
            sum += num
            count += 1
    return sum, count

def solve() -> None:
    # 입력: 5
    #      -2 4 0 7 -1
    # 핵심 조건: 정수 N과 N개의 정수가 주어진다.
    # 양수들의 합과 양수의 개수를 구하는 get_positive_info(numbers) 함수를 작성하라.
    # 함수는 두 값을 반환해야 한다.
    # 출력은 합 개수 순서로 한다.
    # 예상 시간복잡도: O(N)
    N = int(input())
    numbers = list(map(int, input().split()))
    
    sum, count = get_positive_info(numbers)
        
    print(sum, count)

    pass


if __name__ == "__main__":
    solve()
