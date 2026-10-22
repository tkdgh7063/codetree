import sys

input = sys.stdin.readline
print = sys.stdout.write

def solve():
    N, K = map(int, input().split())
    nums = [int(input()) for _ in range(N)]
    nums.sort()

    left = 0
    right = N - 1
    answer = 0

    while left < right:
        current_sum = nums[left] + nums[right]

        if current_sum <= K:
            answer += right - left
            left += 1
        else:
            right -= 1

    print(str(answer) + '\n')

if __name__ == "__main__":
    solve()
