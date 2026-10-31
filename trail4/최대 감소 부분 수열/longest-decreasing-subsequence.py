import sys

input = sys.stdin.readline
print = sys.stdout.write

def solve():
    N = int(input())
    arr = list(map(int, input().split()))

    dp = [1] * N

    for i in range(1, N):
        for j in range(i):
            if arr[j] > arr[i]:
                dp[i] = max(dp[i], dp[j] + 1)

    print(str(max(dp)) + "\n")

    return

if __name__ == "__main__":
    solve()
