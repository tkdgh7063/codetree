import sys

input = sys.stdin.readline
# print = sys.stdout.write

def solve():
    N = int(input())
    nums = list(map(int, input().split()))

    dp = [-float('inf')] * N
    dp[0] = nums[0]

    for i in range(1, N):
        dp[i] = max(dp[i - 1] + nums[i], nums[i])

    print(max(dp))

    return

if __name__ == "__main__": solve()
