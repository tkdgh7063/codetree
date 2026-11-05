import sys

input = sys.stdin.readline
# print = sys.stdout.write

def solve():
    A = input().strip()
    B = input().strip()

    N = len(A)
    M = len(B)

    # dp[i][j]는 A의 처음부터 i개 문자, B의 처음부터 j개 문자를 고려했을 때 LSC의 길이
    dp = [[0] * (M + 1) for _ in range(N + 1)]

    for i in range(1, N + 1):
        for j in range(1, M + 1):
            if A[i - 1] == B[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])

    answer = dp[N][M]
    sys.stdout.write(str(answer) + "\n")

    return

if __name__ == "__main__":
    solve()
