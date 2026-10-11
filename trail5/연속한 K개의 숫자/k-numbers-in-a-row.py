import sys

input = sys.stdin.readline

N, K, B = map(int, input().split())
missing_nums = {int(input()) for _ in range(B)}

all_nums = [1 if i not in missing_nums else 0 for i in range(1, N + 1)]

answer = -float('inf')

s = sum(all_nums[:K])
for i in range(1, N - K + 1):
    s = s - all_nums[i - 1] + all_nums[i + K - 1]
    answer = max(answer, s)

print(K - answer)
