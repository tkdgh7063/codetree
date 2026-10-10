import sys

input = sys.stdin.readline

N, K = map(int, input().split())
nums = list(map(int, input().split()))

INF = float('inf')
answer = -INF
s = sum(nums[:K])
for i in range(N - K):
    s = s - nums[i] + nums[i + K]
    answer = max(answer, s)

print(answer)
