import sys

input = sys.stdin.readline
print = sys.stdout.write

def solve():
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    dp = [None] * (M + 1)
    dp[0] = 0

    for num in arr[::-1]:
        for m in range(M, -1, -1):
            prev = m - num
            if prev >= 0:
                if dp[prev] is None:
                    continue

                if dp[m] is None:
                    dp[m] = dp[prev] + 1
                else:
                    dp[m] = min(dp[prev] + 1, dp[m])

    print(str(dp[M]) if dp[M] is not None else "-1")

    return

if __name__ == "__main__":
    solve()
