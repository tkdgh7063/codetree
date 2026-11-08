import sys

input = sys.stdin.readline

def solve():
    A = input().strip()
    N = len(A)

    answer = 0
    for i in range(N):
        for j in range(i, N):
            if A[i] == "(" and A[j] == ")":
                answer += 1

    sys.stdout.write(str(answer))

    return

if __name__ == "__main__":
    solve()
