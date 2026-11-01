import sys

input = sys.stdin.readline
print = sys.stdout.write

MOD = 10_007

def solve():
    N = int(input())
    nums = [1, 2, 5]

    dp = [0] * (N + 1)
    dp[0] = 1

    for i in range(1, N + 1):
        for num in nums:
            if i < num:
                continue

            candidate = dp[i - num]

            if dp[i] is None:
                dp[i] = candidate
            else:
                dp[i] += candidate

    answer = dp[N] % MOD
    print(str(answer) + "\n")

    return

if __name__ == "__main__":
    solve()
