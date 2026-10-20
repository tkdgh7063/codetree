import sys

input = sys.stdin.readline
print = sys.stdout.write

def solve():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    i = 0
    for j in range(M):
        while i < N and A[i] != B[j]:
            i += 1

        if i == N:
            print("No")
            return

        i += 1

    print("Yes")
    return

if __name__ == "__main__":
    solve()
