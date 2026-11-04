import sys

input = sys.stdin.readline
# print = sys.stdout.write

def solve():
    N = int(input())
    treasures = [tuple(map(int, input().split())) for _ in range(N)]

    # dp[i][j][k] = 처음에 i번째 방을 선택하고 j층에서 k번째 방을 선택했을 때 보물 최대 개수
    dp = [[[0] * 3 for _ in range(N)] for _ in range(3)]

    for i in range(3):
        dp[i][0][i] = treasures[0][i]

    for i in range(3):
        for j in range(1, N - 1):
            dp[i][j][0] = max(dp[i][j - 1][1], dp[i][j - 1][2]) + treasures[j][0]

            dp[i][j][1] = max(dp[i][j - 1][0], dp[i][j - 1][2]) + treasures[j][1]

            dp[i][j][2] = max(dp[i][j - 1][0], dp[i][j - 1][1]) + treasures[j][2]

    # N층은 이전층의 선택과 1층의 선택이 겹치지 않도록
    for i in range(3):
        for j in range(3):
            for k in range(3):
                # i는 처음 선택, j는 이전 선택, k는 이번 선택
                if k == i or k == j:
                    continue

                dp[i][N - 1][k] = max(dp[i][N - 2][j] + treasures[N - 1][k], dp[i][N - 1][k])

    # dp[i][j][k] = 처음에 i번째 방을 선택하고 j층에서 k번째 방을 선택했을 때 보물 최대 개수
    answer = -1
    for i in range(3):
        for num in dp[i][N - 1]:
            answer = max(answer, num)

    print(answer)

    return

if __name__ == "__main__":
    solve()
