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
            if m < num:
                continue

            prev = m - num

            if dp[prev] is None:
                continue

            candidate = dp[prev] + 1

            if dp[m] is None or dp[m] > candidate:
                dp[m] = candidate

    answer = dp[M] if dp[M] is not None else -1
    print(str(answer) + "\n")

    return

if __name__ == "__main__":
    solve()
