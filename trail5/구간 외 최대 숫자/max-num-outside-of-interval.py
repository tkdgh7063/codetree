import sys

input = sys.stdin.readline
print = sys.stdout.write

def solve():
    N, Q = map(int, input().split())
    arr = list(map(int, input().split()))
    section = [tuple(map(int, input().split())) for _ in range(Q)]

    L = [0] * N
    L[0] = arr[0]
    for i in range(1, N):
        L[i] = max(L[i - 1], arr[i])

    R = [0] * N
    R[-1] = arr[-1]
    for i in range(N - 2, -1, -1):
        R[i] = max(R[i + 1], arr[i])

    for a, b in section:
        answer = -float('inf')
        a, b = a - 1, b - 1
        answer = max(L[a - 1], R[b + 1])
        print(str(answer) + '\n')


if __name__ == '__main__':
    solve()
