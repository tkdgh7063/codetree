import sys

input = sys.stdin.readline
print = sys.stdout.write

def solve():
    N, K = map(int, input().split())
    info = []  # 좌표, 사탕 개수
    for i in range(N):
        c, b = map(int, input().split())
        info.append((b, c))

    candy = [0] * (1_000_000 + 1)
    for b, c in info:
        candy[b] += c

    start = 0
    end = 2 * K
    sum_val = sum(candy[:end + 1])
    answer = sum_val
    while end < len(candy) - 1:
        answer = max(answer, sum_val)

        end += 1
        sum_val = sum_val + candy[end] - candy[start]
        start += 1

    print(str(answer) + '\n')

if __name__ == "__main__":
    solve()
