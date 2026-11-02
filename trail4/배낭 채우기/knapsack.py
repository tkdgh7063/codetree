import sys

input = sys.stdin.readline
print = sys.stdout.write

def solve():
    N, M = map(int, input().split())
    jewels = [tuple(map(int, input().split())) for _ in range(N)]  # 무게, 가치

    # 각 보석을 최대 한 번씩만 선택
    # 무게 M, 가치는 최대로
    dp = [None] * (M + 1)
    dp[0] = 0

    for w, v in jewels:
        for m in range(M, w - 1, -1):
            prev = m - w

            if dp[prev] is None:
                continue

            candidate = dp[prev] + v

            if dp[m] is None or dp[m] < candidate:
                dp[m] = candidate

    answer = max([value for value in dp if value is not None])
    print(str(answer) + "\n")

    return

if __name__ == "__main__":
    solve()
