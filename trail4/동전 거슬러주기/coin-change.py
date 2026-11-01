import sys

input = sys.stdin.readline
print = sys.stdout.write

def solve():
    N, M = map(int, input().split())
    coins = list(map(int, input().split()))

    # 최소 동전 수
    dp = [None] * (M + 1)
    dp[0] = 0

    for money in range(1, M + 1):
        for coin in coins:
            prev = money - coin
            if money >= coin:
                if dp[prev] is not None:
                    if dp[money] is None:
                        dp[money] = dp[prev] + 1
                    else:
                        dp[money] = min(dp[prev] + 1, dp[money])

    print(str(dp[M]) if dp[M] != None else "-1")

    return

if __name__ == "__main__":
    solve()
