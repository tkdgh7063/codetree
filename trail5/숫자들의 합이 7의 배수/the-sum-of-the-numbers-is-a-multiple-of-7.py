import sys

input = sys.stdin.readline
print = sys.stdout.write

def solve():
    N = int(input())
    nums = [int(input()) for _ in range(N)]

    remainder = [0] * N
    remainder[0] = nums[0] % 7
    for i in range(1, N):
        remainder[i] = (remainder[i - 1] + nums[i]) % 7

    R = dict()
    answer = 0
    for i in range(N):
        n = remainder[i]
        if n == 0:
            answer = max(answer, i + 1)
        else:
            if n in R:
                answer = max(answer, i - R[n])
            else:
                R[n] = i

    print(str(answer))

if __name__ == "__main__":
    solve()
