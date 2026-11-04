import sys

input = sys.stdin.readline
print = sys.stdout.write

MOD = 10 ** 9 + 7

def solve():
    N = int(input())

    # dp[i][j] = 길이가 i이고 j가 마지막으로 선택한 숫자
    dp = [[0] * 10 for _ in range(N + 1)]

    # 길이가 1이고 1~9로 시작하는 방법
    for i in range(1, 10):
        dp[1][i] = 1

    # 길이가 2~N이고 j가 마지막으로 선택한 숫자인 문자열의 개수
    for i in range(2, N + 1):
        for j in range(10):
            if j > 0:
                dp[i][j] += dp[i - 1][j - 1]
            if j < 9:
                dp[i][j] += dp[i - 1][j + 1]

            dp[i][j] %= MOD

    answer = sum(dp[N]) % MOD
    print(str(answer) + "\n")

    return

if __name__ == "__main__":
    solve()
