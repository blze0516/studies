import sys

input = sys.stdin.readline


def solve() -> None:
    # 입력: -7
    # 핵심 조건: 정수 N이 주어진다. get_absolute(n) 함수를 만들어 N의 절댓값을 반환하고 출력하라.
    # 예상 시간복잡도: O(1)
    n = int(input())
    total = 0
    
    if usage > 200:
        total += (usage - 200) * 5
        usage -= (usage - 200)
    
    if usage > 100:
        total += (usage - 100) * 3
        usage -= (usage - 100)
        
    total += usage *2

    print(total)    
    pass


if __name__ == "__main__":
    solve()
