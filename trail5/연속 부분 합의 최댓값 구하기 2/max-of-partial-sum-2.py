import sys

input = sys.stdin.readline
# print = sys.stdout.write

def solve():
    N = int(input())
    nums = list(map(int, input().split()))

    answer = -float('inf')
    sum_val = 0
    for i in range(N):
        sum_val += nums[i]
        answer = max(answer, sum_val)

        if sum_val < 0:
            sum_val = 0

    print(answer)
    return

if __name__ == "__main__":
    solve()
