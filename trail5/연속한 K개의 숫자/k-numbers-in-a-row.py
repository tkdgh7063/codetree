import sys

input = sys.stdin.readline
print = sys.stdout.write

N, K, B = map(int, input().split())
missing_nums = {int(input()) for _ in range(B)}

all_nums = [1 if i not in missing_nums else 0 for i in range(1, N + 1)]

s = sum(all_nums[:K])
answer = s
for i in range(1, N - K + 1):
    s = s - all_nums[i - 1] + all_nums[i + K - 1]
    answer = max(answer, s)

print(str(K - answer) + '\n')
