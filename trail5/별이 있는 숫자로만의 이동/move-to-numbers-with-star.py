import sys

input = sys.stdin.readline
print = sys.stdout.write

N, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

prefix_sum = [[0] * (N + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    for j in range(1, N + 1):
        prefix_sum[i][j] = prefix_sum[i - 1][j] + prefix_sum[i][j - 1] - prefix_sum[i - 1][j - 1] + board[i - 1][j - 1]

answer = 0
for r in range(N):
    for c in range(N):
        total_sum = 0
        for i in range(r - K, r + K + 1):
            if i < 0 or i >= N:
                continue

            width = K - abs(i - r)
            col_start = c - width
            col_end = c + width

            if col_end < 0 or col_start >= N:
                continue

            col_start = max(0, col_start)
            col_end = min(N - 1, col_end)

            i += 1
            col_start += 1
            col_end += 1

            # i행에서 col_start부터 col_end까지의 합
            total_row = prefix_sum[i][col_end] - prefix_sum[i][col_start - 1] - prefix_sum[i - 1][col_end] + prefix_sum[i - 1][col_start - 1]
            total_sum += total_row
        answer = max(answer, total_sum)

print(str(answer) + '\n')
