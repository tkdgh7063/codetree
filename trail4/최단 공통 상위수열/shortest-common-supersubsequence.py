import sys

input = sys.stdin.readline

def solve():
    S = input().strip()
    T = input().strip()

    N = len(S)
    M = len(T)

    # 최단 공통 supersequence 길이 구하기

    # dp[i][j] = S의 i번째, T의 j번째까지 고려했을 때 최단 공통 supersequence 길이
    dp = [[0] * (M + 1) for _ in range(N + 1)]

    for i in range(1, N + 1):
        if S[i - 1] == T[0]:
            dp[i][1] = 1
        else:
            dp[i][1] = 0

    for j in range(1, M + 1):
        if S[0] == T[j - 1]:
            dp[1][j] = 1
        else:
            dp[1][j] = 0

    for i in range(1, N + 1):
        for j in range(1, M + 1):
            if S[i - 1] == T[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    lcs = dp[N][M]
    answer = N + M - lcs
    sys.stdout.write(str(answer) + "\n")

if __name__ == "__main__":
    solve()
