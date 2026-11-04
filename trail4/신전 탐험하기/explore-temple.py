import sys

input = sys.stdin.readline
print = sys.stdout.write

def solve():
    N = int(input())
    treasures = [tuple(map(int, input().split())) for _ in range(N)]  # 왼쪽, 가운데, 오른쪽 방의 보물 개수

    # 각 층에서 하나의 방에서 보물을 획득 가능
    # 같은 방향의 방을 연속해서 선택 불가
    dp = [[-1] * 3 for _ in range(N + 1)]

    # 1층은 보물 개수 그대로
    for i in range(3):
        dp[1][i] = treasures[0][i]

    # 2층부터 N층까지
    for i in range(2, N + 1):
        for j in range(3):
            for k in range(3):
                # j는 지금 선택한 방향
                # k는 이전에 선택한 방향
                if dp[i - 1][k] == -1:
                    continue

                if j != k:
                    dp[i][j] = max(dp[i][j], dp[i - 1][k] + treasures[i - 1][j])

    answer = max(dp[N])
    print(str(answer) + "\n")

    return

if __name__ == "__main__":
    solve()
