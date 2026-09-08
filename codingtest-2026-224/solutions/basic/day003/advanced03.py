import sys

input = sys.stdin.readline


def solve() -> None:
    # 입력: 6
    # 핵심 조건: 1부터 N까지 각 정수를 확인한다.
    # 2의 배수이면 1점 추가
    # 3의 배수이면 2점 추가
    # 5의 배수이면 3점 추가
    # 한 숫자가 여러 조건을 만족하면 점수를 모두 더한다.
    # 1부터 N까지의 총점을 출력하라.
    # 예상 시간복잡도: O(1)
    N = int(input())
    score = 0
    
    for i in range(1, N + 1):
        if i % 2 == 0:
            score += 1

        if i % 3 == 0:
            score += 2
            
        if i % 5 == 0:
            score += 3
        
    print(score)    
    pass


if __name__ == "__main__":
    solve()
