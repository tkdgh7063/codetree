import sys

input = sys.stdin.readline
print = sys.stdout.write

def solve():
    N, M = map(int, input().split())
    jewels = [tuple(map(int, input().split())) for _ in range(N)]  # 무게, 가치

    dp = [None] * (M + 1)
    dp[0] = 0

    for i in range(1, M + 1):
        for w, v in jewels:
            if i < w:
                continue

            prev = i - w

            if dp[prev] is None:
                continue

            candidate = dp[prev] + v

            if dp[i] is None or dp[i] < candidate:
                dp[i] = candidate

    answer = max((value for value in dp if value is not None), default=0)
    print(str(answer) + "\n")

    return

if __name__ == "__main__":
    solve()
