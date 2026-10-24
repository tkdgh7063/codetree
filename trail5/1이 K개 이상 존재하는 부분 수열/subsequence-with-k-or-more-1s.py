import sys

input = sys.stdin.readline
# print = sys.stdout.write

def solve():
    N, K = map(int, input().split())
    nums = list(map(int, input().split()))

    answer = float('inf')
    j = 0
    count = 0
    for i in range(N):
        while j < N and count < K:
            if nums[j] == 1:
                count += 1
            j += 1

        if count == K:
            answer = min(answer, j - i)

        if nums[i] == 1:
            count -= 1

    print(answer if answer != float('inf') else -1)

if __name__ == "__main__":
    solve()
