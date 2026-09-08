import sys

input = sys.stdin.readline


def solve() -> None:
    # 입력: 5 12 4
    # 핵심 조건: 정수 value, 목표 target, 최대 횟수 K가 주어진다.
    # 한 번의 작업에서:
    # value가 짝수면 3을 더한다.
    # value가 홀수면 2를 더한다.
    # 최대 K번 작업하면서 처음 value >= target이 되는 작업 횟수를 출력하라. K번 안에 도달하지 못하면 -1을 출력한다.
    # 처음부터 목표 이상이면 0을 출력한다.
    # 예상 시간복잡도: O(1)
    value, target, K = map(int, input().split())
    count = 0
    
    if value >= target:
        print(0)
        return 0
    
    while value < target and count < K:
        if value % 2 == 0:
            value += 3
        else:
            value += 2
        count += 1
    
    if value >= target:
        print(count)
    else:
        print(-1)    
    
    pass

if __name__ == "__main__":
    solve()
