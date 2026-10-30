import sys

input = sys.stdin.readline
# print = sys.stdout.write

def solve():
    N = int(input())

    dp = [0] * 1001
    dp[2] = 1
    dp[3] = 1

    for i in range(4, N + 1):
        dp[i] = dp[i - 2] + dp[i - 3]

    if dp[N] != 0:
        print(dp[N] % 10007)
    else:
        print(0)

    return

if __name__ == "__main__":
    solve()
