import sys

input = sys.stdin.readline
print = sys.stdout.write

def solve():
    N = int(input())
    nums = list(map(int, input().split()))

    total = sum(nums)

    if total % 2:
        print("No\n")
        return

    total //= 2

    dp = [False] * (total + 1)
    dp[0] = True

    for num in nums:
        for i in range(total, num - 1, -1):
            prev = i - num

            if dp[prev]:
                dp[i] = True

    answer = "Yes" if dp[total] else "No"
    print(answer)

    return

if __name__ == "__main__":
    solve()
