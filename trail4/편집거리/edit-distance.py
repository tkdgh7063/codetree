import sys

input = sys.stdin.readline

def solve():
    A = input().strip()
    B = input().strip()

    N = len(A)
    M = len(B)

    # dp[i][j] = A의 i개 문자를 B의 j개 문자로 바꾸는 데 필요한 최소 편집 수
    dp = [[0] * (M + 1) for _ in range(N + 1)]

    for i in range(N + 1):
        dp[i][0] = i

    for i in range(M + 1):
        dp[0][i] = i

    for i in range(1, N + 1):
        for j in range(1, M + 1):
            if A[i - 1] == B[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1

    answer = dp[N][M]
    sys.stdout.write(str(answer) + "\n")

if __name__ == "__main__":
    solve()
