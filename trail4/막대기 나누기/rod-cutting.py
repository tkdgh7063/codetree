import sys

input = sys.stdin.readline
print = sys.stdout.write

def solve():
    N = int(input())
    profit = list(map(int, input().split()))  # (인덱스+1) 길이의 막대기 수익

    dp = [None] * (N + 1)
    dp[0] = 0

    for i in range(1, N + 1):
        for l, p in enumerate(profit):
            length = l + 1

            if length > i:
                continue

            prev = i - length

            if dp[prev] is None:
                continue

            candidate = dp[prev] + p

            if dp[i] is None or dp[i] < candidate:
                dp[i] = candidate

    print(str(dp[N]) + "\n")

    return

if __name__ == "__main__": solve()
