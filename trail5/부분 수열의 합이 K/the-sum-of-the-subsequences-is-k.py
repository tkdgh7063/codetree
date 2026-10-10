import sys

input = sys.stdin.readline
print = sys.stdout.write

N, K = map(int, input().split())
nums = list(map(int, input().split()))

prefix_sum = [0] * (N + 1)
for i in range(1, N + 1):
    prefix_sum[i] = prefix_sum[i - 1] + nums[i - 1]

answer = 0
for length in range(1, N):
    for start in range(N - length + 1):
        s = prefix_sum[start + length] - prefix_sum[start]
        if s == K:
            answer += 1
print(str(answer))
