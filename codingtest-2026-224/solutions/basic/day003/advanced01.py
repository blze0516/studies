import sys

input = sys.stdin.readline


def solve() -> None:
    # 입력: 250
    # 핵심 조건: 전기 사용량 usage가 주어진다. 사용량에 따라 아래 요금을 계산한다.
    # 처음 100 단위까지: 단위당 2원
    # 101부터 200 단위까지: 단위당 3원
    # 201 단위부터: 단위당 5원
    # 총 요금을 출력하라.
    # 예상 시간복잡도: O(1)
    usage = int(input())
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
