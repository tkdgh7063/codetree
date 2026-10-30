import sys

input = sys.stdin.readline
print = sys.stdout.write

def solve():
    N = int(input())

    dp = [0] * 1001
    dp[0] = 1
    dp[1] = 2

    # 1칸을 채울 때는 2가지
    # 2칸을 채울 때는 7가지
    # k칸을 채울 때 1칸을 채우는 방법 + 2칸을 채우는 방법
    for i in range(2, N + 1):
        dp[i] = 3 * dp[i - 1] + dp[i - 2] - dp[i - 3]

    print(str(dp[N] % 1000000007) + "\n")

    return

if __name__ == "__main__":
    solve()
