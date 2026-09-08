import sys

input = sys.stdin.readline


def solve() -> None:
    # 입력: 5 12 4
    # 핵심 조건: 지원자의 age, score, training이 주어진다.
    # 아래 순서대로 정확히 하나의 결과를 출력한다.
    # age가 18 미만이면 AGE_FAIL
    # 그렇지 않고 score가 80 이상이며 training이 100 이상이면 VIP
    # 그렇지 않고 score가 60 이상이며 training이 50 이상이면 PASS
    # 그 외에는 FAIL
    # 예상 시간복잡도: O(1)
    age, score, training = map(int, input().split())
    
    if age < 18:
        print("AGE_FAIL")
    else:
        if score >= 80 and training >= 100:
            print("VIP")
        elif score >= 60 and training >= 50:
            print("PASS")
        else:
            print("FAIL")
    
    pass

if __name__ == "__main__":
    solve()
