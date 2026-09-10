import sys

input = sys.stdin.readline

def triple(n):
    return 3 * n

def solve() -> None:
    # 입력: 4
    # 핵심 조건: 정수 N을 받아 세 배 값을 반환하는 triple(n) 함수를 작성하고 결과를 출력하라.
    # 예상 시간복잡도: O(1)
    n = int(input())
    
    print(triple(n))

    pass


if __name__ == "__main__":
    solve()
