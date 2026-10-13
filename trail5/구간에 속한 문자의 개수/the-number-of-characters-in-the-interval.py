import sys

input = sys.stdin.readline

N, M, K = map(int, input().split())
strings = list(list(input().strip()) for _ in range(N))

prefix_a = [[0] * (M + 1) for _ in range(N + 1)]
prefix_b = [[0] * (M + 1) for _ in range(N + 1)]
prefix_c = [[0] * (M + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    for j in range(1, M + 1):
        ch = strings[i - 1][j - 1]

        prefix_a[i][j] = prefix_a[i][j - 1] + prefix_a[i - 1][j] - prefix_a[i - 1][j - 1]
        prefix_b[i][j] = prefix_b[i][j - 1] + prefix_b[i - 1][j] - prefix_b[i - 1][j - 1]
        prefix_c[i][j] = prefix_c[i][j - 1] + prefix_c[i - 1][j] - prefix_c[i - 1][j - 1]

        if ch == 'a':
            prefix_a[i][j] += 1
        elif ch == 'b':
            prefix_b[i][j] += 1
        else:
            prefix_c[i][j] += 1

for _ in range(K):
    r1, c1, r2, c2 = tuple(map(int, input().split()))
    r1, c1 = r1 - 1, c1 - 1

    result = prefix_a[r2][c2] - prefix_a[r1][c2] - prefix_a[r2][c1] + prefix_a[r1][c1]
    print(result, end=" ")

    result = prefix_b[r2][c2] - prefix_b[r1][c2] - prefix_b[r2][c1] + prefix_b[r1][c1]
    print(result, end=" ")

    result = prefix_c[r2][c2] - prefix_c[r1][c2] - prefix_c[r2][c1] + prefix_c[r1][c1]
    print(result)
