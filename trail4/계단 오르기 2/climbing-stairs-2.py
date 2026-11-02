import sys

input = sys.stdin.readline
print = sys.stdout.write

def solve():
    N = int(input())
    coins = list(map(int, input().split()))

    # 계단은 1계단, 2계단 이동 가능
    # 1계단은 최대 3번 이동
    # dp[i][j] = i번째 계단까지 이동했을 때 1계단을 j번 이동했을 때 최대 동전 개수
    dp = [[-1] * 4 for _ in range(N + 1)]
    dp[0][0] = 0

    for i in range(1, N + 1):
        # 1계단 이동
        for j in range(1, 4):
            if dp[i - 1][j - 1] != -1:
                dp[i][j] = max(dp[i - 1][j - 1] + coins[i - 1], dp[i][j])

        # 2계단 이동
        if i >= 2:
            for j in range(4):
                if dp[i - 2][j] != -1:
                    dp[i][j] = max(dp[i - 2][j] + coins[i - 1], dp[i][j])

    answer = max(dp[-1])
    print(str(answer) + "\n")

    return

if __name__ == "__main__": solve()
