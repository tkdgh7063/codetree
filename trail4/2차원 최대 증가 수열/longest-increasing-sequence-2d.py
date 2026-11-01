import sys

input = sys.stdin.readline
print = sys.stdout.write

def solve():
    N, M = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(N)]

    # 이동은 항상 숫자가 더 큰 칸으로만 점프
    # 점프는 오른쪽 아래로만 가능
    # 칸을 최대한 많이 밟으면서 이동

    # 점프가 불가능한 칸은 None으로 초기화
    dp = [[None] * M for _ in range(N)]
    dp[0][0] = 1

    for i in range(1, N):
        for j in range(1, M):
            # 각 칸에 대해서
            for k in range(i):
                for l in range(j):
                    # 왼쪽 상단 칸들의 DP 계산
                    # 이동 불가 시 패스
                    if dp[k][l] is None:
                        continue

                    # 점프 가능
                    if grid[k][l] < grid[i][j]:
                        candidate = dp[k][l] + 1

                        if dp[i][j] is None or candidate > dp[i][j]:
                            dp[i][j] = candidate

    # 최대 이동 칸 출력
    answer = max((num for row in dp for num in row if num is not None), default=1)
    print(str(answer) + "\n")

    return

if __name__ == "__main__":
    solve()
