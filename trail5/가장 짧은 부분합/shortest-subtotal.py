import sys

input = sys.stdin.readline
print = sys.stdout.write

def solve():
    N, S = map(int, input().split())
    nums = list(map(int, input().split()))

    answer = float('inf')
    j = 0
    sum_val = 0
    for i in range(N):
        while j < N and sum_val < S:
            sum_val += nums[j]
            j += 1
        if sum_val >= S:
            answer = min(answer, j - i)

        sum_val -= nums[i]

    print(str(answer) if answer != float('inf') else '-1')

if __name__ == "__main__":
    solve()
