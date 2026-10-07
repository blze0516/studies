import sys

input = sys.stdin.readline

def solve() -> None:
    # 입력: 6
    #      5 12 3 12 7 1
    # 핵심 조건: 정수 N개가 주어진다.
    #           가장 큰 값과 그 값이 처음 등장한 인덱스를 출력하라.
    #           인덱스는 0부터 시작한다.
    # 예상 시간복잡도: O(N)
    # 예상 공간복잡도: O(N)
    N = int(input())    
    numbers = list(map(int, input().split()))
    max_number = numbers[0]
    max_number_idx = 0
    
    for i in range(1, N):
        if numbers[i] > max_number:
            max_number = numbers[i]
            max_number_idx = i

    print(max_number, max_number_idx)
    
    pass


if __name__ == "__main__":
    solve()
