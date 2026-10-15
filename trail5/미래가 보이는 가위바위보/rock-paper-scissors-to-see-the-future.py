import sys

input = sys.stdin.readline
print = sys.stdout.write

def solve():
    N = int(input())
    B = [input().strip() for _ in range(N)]

    mapper = {"S": 0, "H": 1, "P": 2}

    L = [[0] * 3 for _ in range(N + 1)]
    R = [[0] * 3 for _ in range(N + 1)]

    for i in range(1, N + 1):
        for j in range(3):
            L[i][j] = L[i - 1][j]
        L[i][mapper[B[i - 1]]] += 1

    for i in range(N - 1, -1, -1):
        for j in range(3):
            R[i][j] = R[i + 1][j]
        R[i][mapper[B[i]]] += 1

    # answer = -1
    # for i in range(N + 1):
    #     res = max(L[i]) + max(R[i])
    #     answer = max(answer, res)
    answer = max(max(L[i]) + max(R[i]) for i in range(N + 1))

    print(str(answer) + '\n')

if __name__ == '__main__':
    solve()
