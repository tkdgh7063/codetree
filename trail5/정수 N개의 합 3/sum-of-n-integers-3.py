import sys

input = sys.stdin.readline
print = sys.stdout.write

N, K = map(int, input().split())
square = [[0] + list(map(int, input().split())) for _ in range(N)]

grid = [[0] * (N + 1)]
prefix_sum = [[0] * (N + 1) for _ in range(N + 1)]

grid += square

for i in range(1, N + 1):
    for j in range(1, N + 1):
        prefix_sum[i][j] = prefix_sum[i - 1][j] + prefix_sum[i][j - 1] - prefix_sum[i - 1][j - 1] + grid[i][j]

answer = -float('inf')
for i in range(K, N + 1):
    for j in range(K, N + 1):
        square_sum = prefix_sum[i][j] - prefix_sum[i - K][j] - prefix_sum[i][j - K] + prefix_sum[i - K][j - K]
        answer = max(answer, square_sum)

print(str(answer))
