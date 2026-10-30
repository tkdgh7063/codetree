import sys

input = sys.stdin.readline
print = sys.stdout.write

def solve():
    N = int(input())

    dp = [0] * 1001
    dp[1] = 1
    dp[2] = 2

    for i in range(3, N + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    print(str(dp[N] % 10007) + "\n")

    return

if __name__ == "__main__":
    solve()
