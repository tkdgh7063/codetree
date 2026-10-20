import sys

input = sys.stdin.readline
print = sys.stdout.write

def solve():
    N = int(input())
    nums = list(map(int, input().split()))

    counting = set()
    answer = 0
    j = 0
    for i in range(N):
        while j < N and nums[j] not in counting:
            counting.add(nums[j])
            j += 1
        answer = max(answer, j - i)
        counting.remove(nums[i])

    print(str(answer) + "\n")

if __name__ == "__main__":
    solve()
