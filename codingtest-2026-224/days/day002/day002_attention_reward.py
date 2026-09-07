import sys

input = sys.stdin.readline


def solve() -> None:
    # 문제 풀이 코드를 여기에 작성합니다.
    n = int(input())
    count = 0
    score = 0
    
    for _ in range(n):
        study_minutes = int(input())
        if study_minutes >= 120:
            score += 3
            count += 1
        elif study_minutes >= 60:
            score += 2
            count += 1
        elif study_minutes >= 30:
            score += 1
            
    print(score, count)
        
    
if __name__ == "__main__":
    solve()
