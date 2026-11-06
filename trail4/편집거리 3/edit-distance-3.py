import sys

input = sys.stdin.readline

def solve():
    A = input().strip()
    B = input().strip()

    N = len(A)
    M = len(B)

    # 문자열 A를 문자열 B로 바꾸기 위해 필요한 최소 연산 횟수
    # 연산은 삽입, 삭제만 가능

    # dp[i][j] = A의 i번째, B의 j번째까지 고려한 최소 연산 횟수
    dp = [[0] * (M + 1) for _ in range(N + 1)]

    for i in range(N + 1):
        dp[i][0] = i

    for j in range(M + 1):
        dp[0][j] = j

    for i in range(1, N + 1):
        for j in range(1, M + 1):
            if A[i - 1] == B[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + 1

    answer = dp[N][M]
    sys.stdout.write(str(answer) + "\n")

if __name__ == "__main__":
    solve()
