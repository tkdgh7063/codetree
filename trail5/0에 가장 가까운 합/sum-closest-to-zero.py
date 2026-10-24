import sys

input = sys.stdin.readline
print = sys.stdout.write

def solve():
    N = int(input())
    nums = list(map(int, input().split()))
    nums.sort()

    left = 0
    right = N - 1
    M = abs(nums[left] + nums[right])
    while left < right:
        current_sum = nums[left] + nums[right]

        if abs(current_sum) <= M:
            M = abs(current_sum)

        if current_sum < 0:
            left += 1
        else:
            right -= 1

    print(str(M) + "\n")


if __name__ == "__main__":
    solve()
