import sys

input = sys.stdin.readline
# print = sys.stdout.write

def get_sum(N):
    return N * (N + 1) // 2

def solve():
    S = int(input())

    answer = -1

    left = 0
    right = S
    while left <= right:
        mid = (left + right) // 2
        target = get_sum(mid)

        if target == S:
            answer = max(mid, answer)
            right = mid - 1
        elif target < S:
            answer = max(mid, answer)
            left = mid + 1
        else:
            right = mid - 1

    print(answer)

if __name__ == "__main__":
    solve()
