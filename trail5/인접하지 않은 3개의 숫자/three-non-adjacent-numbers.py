import sys

input = sys.stdin.readline
print = sys.stdout.write

def solve():
    N = int(input())
    arr = list(map(int, input().split()))

    L = [0] * N
    L[0] = arr[0]
    for i in range(1, N):
        L[i] = max(L[i - 1], arr[i])

    R = [0] * N
    R[-1] = arr[-1]
    for i in range(N - 2, -1, -1):
        R[i] = max(R[i + 1], arr[i])

    answer = -float('inf')
    for i in range(2, N - 2):
        res = L[i - 2] + R[i + 2] + arr[i]
        answer = max(res, answer)

    print(str(answer) + '\n')

if __name__ == '__main__':
    solve()
