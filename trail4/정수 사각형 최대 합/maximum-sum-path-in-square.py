import sys

input = sys.stdin.readline
print = sys.stdout.write

def solve():
    N = int(input())
    grid = [list(map(int, input().split())) for _ in range(N)]

    dp = [[None] * N for _ in range(N)]
    dp[0][0] = grid[0][0]

    for i in range(1, N):
        dp[0][i] = dp[0][i - 1] + grid[0][i]
        dp[i][0] = dp[i - 1][0] + grid[i][0]

    # 밑, 오른쪽으로 이동가능
    for x in range(1, N):
        for y in range(1, N):
            dp[x][y] = max(dp[x - 1][y], dp[x][y - 1]) + grid[x][y]

    print(str(dp[-1][-1]) + "\n")

    return

if __name__ == "__main__":
    solve()
