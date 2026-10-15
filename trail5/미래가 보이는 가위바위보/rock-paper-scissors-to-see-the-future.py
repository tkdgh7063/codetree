import sys

input = sys.stdin.readline
print = sys.stdout.write

def solve():
    N = int(input())
    B = [input().strip() for _ in range(N)]

    L = [[0] * 3 for _ in range(N + 1)]
    R = [[0] * 3 for _ in range(N + 1)]

    for i in range(1, N + 1):
        L[i] = L[i - 1][:]

        if B[i - 1] == "S":
            L[i][0] += 1
        elif B[i - 1] == "H":
            L[i][1] += 1
        else:
            L[i][2] += 1

    for i in range(N - 1, -1, -1):
        R[i] = R[i + 1][:]

        if B[i] == "S":
            R[i][0] += 1
        elif B[i] == "H":
            R[i][1] += 1
        else:
            R[i][2] += 1

    answer = -1
    for i in range(N + 1):
        res = max(L[i]) + max(R[i])
        answer = max(answer, res)

    print(str(answer) + '\n')

if __name__ == '__main__':
    solve()
