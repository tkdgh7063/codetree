import sys

input = sys.stdin.readline
# print = sys.stdout.write


def solve():
    N, K = map(int, input().split())
    nums = list(map(int, input().split()))

    counter = dict()
    i = 0
    answer = 0
    for j in range(N):
        counter[nums[j]] = counter.get(nums[j], 0) + 1

        while i < N and counter[nums[j]] > K:
            counter[nums[i]] -= 1

            if counter[nums[i]] == 0:
                del counter[nums[i]]

            i += 1

        answer = max(answer, j - i + 1)

    print(answer)

if __name__ == "__main__":
    solve()
