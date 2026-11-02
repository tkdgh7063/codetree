import sys

input = sys.stdin.readline
print = sys.stdout.write

def solve():
    N, M = map(int, input().split())
    nums = list(map(int, input().split()))

    dp = [None] * (M + 1)
    dp[0] = True

    for num in nums[::-1]:
        for i in range(M, -1, -1):
            if i < num:
                continue

            prev = i - num

            if dp[prev] is None:
                continue

            if dp[i] is None:
                dp[i] = dp[prev]

    answer = "Yes" if dp[M] else "No"
    print(answer)

    return

if __name__ == "__main__":
    solve()
