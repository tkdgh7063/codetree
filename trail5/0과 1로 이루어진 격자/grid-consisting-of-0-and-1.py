import sys

input = sys.stdin.readline
# print = sys.stdout.write

def solve():
    N = int(input())
    grid = [list(map(int, input().strip())) for _ in range(N)]

    # 선택한 칸을 기점으로 좌측 상단이 모두 반전
    # 우측 하단 칸부터 시작해 선택
    answer = 0
    for row_idx in range(N - 1, -1, -1):
        for col_idx in range(N - 1, -1, -1):
            if grid[row_idx][col_idx] == 1:
                # 좌측 상단을 반전
                answer += 1
                for i in range(row_idx + 1):
                    for j in range(col_idx + 1):
                        grid[i][j] ^= 1

    print(str(answer) + "\n")

    return

if __name__ == "__main__":
    solve()
