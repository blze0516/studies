import sys

input = sys.stdin.readline

def get_max_score(scores):
    max = scores[0]
    
    for i in range(1, len(scores)):
        if scores[i] > max:
            max = scores[i]
    return max

def solve() -> None:
    # 입력: 5
    #       70 92 81 92 64
    # 핵심 조건: N개의 점수가 주어진다.
    # 내장 max()를 사용하지 않고 get_max_score(scores) 함수를 작성해 최댓값을 반환하라.
    # 예상 시간복잡도: O(N)
    N = int(input())
    scores = list(map(int, input().split()))
    
    print(get_max_score(scores))
    pass


if __name__ == "__main__":
    solve()
