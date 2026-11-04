import sys

input = sys.stdin.readline
print = sys.stdout.write

def solve():
    N = int(input())
    treasures = [tuple(map(int, input().split())) for _ in range(N)]  # 왼쪽, 가운데, 오른쪽 방의 보물 개수

    # 각 층에서 하나의 방에서 보물을 획득 가능
    # 같은 방향의 방을 연속해서 선택 불가

    # dp[i][j] = i번째 층에서 j번 방을 골랐을 때의 최대 보물 개수
    dp = [[0] * 3 for _ in range(N)]

    # 1층은 보물 개수 그대로
    for i in range(3):
        dp[0][i] = treasures[0][i]

    # 2층부터 N층까지
    for i in range(1, N):
        dp[i][0] = treasures[i][0] + max(dp[i - 1][1], dp[i - 1][2])

        dp[i][1] = treasures[i][1] + max(dp[i - 1][0], dp[i - 1][2])

        dp[i][2] = treasures[i][2] + max(dp[i - 1][0], dp[i - 1][1])

    answer = max(dp[N - 1])
    print(str(answer) + "\n")

    return

if __name__ == "__main__":
    solve()
