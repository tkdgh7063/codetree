import sys

input = sys.stdin.readline
print = sys.stdout.write

MIN_INT = -sys.maxsize

def solve():
    N = int(input())
    arr = list(map(int, input().split()))
    dp = [0] * N

    for i in range(N):
        dp[i] = MIN_INT

    dp[0] = 0
    for i in range(1, N):
        for j in range(i):
            if arr[j] == MIN_INT:
                continue

            if arr[j] + j >= i:
                dp[i] = max(dp[i], dp[j] + 1)

    print(str(max(dp)) + "\n")

    return

if __name__ == "__main__":
    solve()
