import sys

input = sys.stdin.readline
print = sys.stdout.write

def solve():
    N = int(input())
    K = int(input())

    def get_seq(num):
        seq = 0

        limit = min(N, num)
        for i in range(1, limit + 1):
            seq += min(N, num // i)

        return seq

    left = 1
    right = N * N

    answer = 0
    while left <= right:
        mid = (left + right) // 2
        seq = get_seq(mid)

        if seq >= K:
            answer = mid
            right = mid - 1
        else:
            left = mid + 1

    print(str(answer) + "\n")

if __name__ == "__main__":
    solve()
