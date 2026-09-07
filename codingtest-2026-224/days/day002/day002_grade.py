import sys

input = sys.stdin.readline


def solve() -> None:
    # 문제 풀이 코드를 여기에 작성합니다.
    score = int(input())
    
    if score >= 90:
        print("A")
    elif score >= 80:
        print("B")
    elif score >= 60:
        print("C")
    else:
        print("F")
    
if __name__ == "__main__":
    solve()
