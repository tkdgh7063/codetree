import sys

input = sys.stdin.readline
print = sys.stdout.write

def solve():
    N = int(input())
    strings = list(input().strip())

    L = [0] * N
    L[0] = 1 if strings[0] == "C" else 0
    for i in range(1, N):
        L[i] = L[i - 1]
        if strings[i] == 'C':
            L[i] += 1

    R = [0] * N
    R[-1] = 1 if strings[-1] == 'W' else 0
    for i in range(N - 2, -1, -1):
        R[i] = R[i + 1]
        if strings[i] == 'W':
            R[i] += 1

    answer = 0
    for i, s in enumerate(strings):
        if i == 0 or i == N - 1:
            continue
        if s == 'O':
            answer += L[i - 1] * R[i + 1]

    print(str(answer) + '\n')

if __name__ == '__main__':
    solve()
