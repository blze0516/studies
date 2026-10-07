import sys

input = sys.stdin.readline

def solve() -> None:
    # 입력: 5
    #      3 8 4 6 9
    # 핵심 조건: 정수 N개가 주어진다. 마지막 숫자를 출력하라.
    # 메인 코드에서는 반환값에 따라 EVEN 또는 ODD를 출력한다.
    # 예상 시간복잡도: O(N)
    # 예상 공간복잡도: O(N)
    n = int(input())
    numbers = list(map(int, input().split()))
    
    print(numbers[n - 1])
    

    pass


if __name__ == "__main__":
    solve()
