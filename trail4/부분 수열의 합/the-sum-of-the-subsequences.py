import sys

input = sys.stdin.readline
print = sys.stdout.write

def solve():
    N, M = map(int, input().split())
    nums = list(map(int, input().split()))

    dp = [False] * (M + 1)
    dp[0] = True

    for num in nums:
        for i in range(M, num - 1, -1):
            if dp[i - num]:
                dp[i] = True

    answer = "Yes" if dp[M] else "No"
    print(answer)

    return

if __name__ == "__main__":
    solve()
