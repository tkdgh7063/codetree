import sys

input = sys.stdin.readline
print = sys.stdout.write

def solve():
    N, M = map(int, input().split())
    nums = list(map(int, input().split()))

    j = 0
    sum_val = 0
    answer = 0
    for i in range(N):
        while j < N and sum_val < M:
            sum_val += nums[j]
            j += 1

        if sum_val == M:
            answer += 1

        sum_val -= nums[i]

    print(str(answer))

if __name__ == "__main__":
    solve()
