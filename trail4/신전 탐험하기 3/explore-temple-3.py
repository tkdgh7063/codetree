import sys

input = sys.stdin.readline
print = sys.stdout.write

def solve():
    N, M = map(int, input().split())
    treasures = [tuple(map(int, input().split())) for _ in range(N)]

    # 각 층에 M개의 방
    # 직전 층에서 선택한 번호의 방을 연속으로 선택하면 실패
    # dp[i][j] = i층에서 j번째 방을 선택했을 때 보물 최대 개수
    dp = [[0] * M for _ in range(N)]

    for i in range(M):
        dp[0][i] = treasures[0][i]

    for i in range(1, N):
        for j in range(M):
            for k in range(M):
                # j는 이번 층에서 고른 방
                # k는 이전 층에서 고른 방
                if j != k:
                    dp[i][j] = max(dp[i - 1][k] + treasures[i][j], dp[i][j])

    answer = max(dp[N - 1])
    print(str(answer) + "\n")

    return

if __name__ == "__main__":
    solve()
