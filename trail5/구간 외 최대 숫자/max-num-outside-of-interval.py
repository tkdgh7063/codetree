import sys

input = sys.stdin.readline

def solve():
    N, Q = map(int, input().split())
    arr = list(map(int, input().split()))
    queries = [tuple(map(int, input().split())) for _ in range(Q)]

    L = [0] * N
    L[0] = arr[0]
    for i in range(1, N):
        L[i] = max(L[i - 1], arr[i])

    R = [0] * N
    R[-1] = arr[-1]
    for i in range(N - 2, -1, -1):
        R[i] = max(R[i + 1], arr[i])

    for a, b in queries:
        answer = -float('inf')
        a -= 1
        b -= 1
        if a > 0:
            answer = max(answer, L[a - 1])

        if b < N - 1:
            answer = max(answer, R[b + 1])

        print(answer)

if __name__ == '__main__':
    solve()
