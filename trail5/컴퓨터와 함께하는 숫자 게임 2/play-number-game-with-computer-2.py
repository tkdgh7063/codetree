import sys

input = sys.stdin.readline
# print = sys.stdout.write

def get_count(arr, target):
    N = len(arr)

    left = 0
    right = N - 1
    count = 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return count

        count += 1
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

def solve():
    M = int(input())
    A, B = map(int, input().split())

    arr = range(1, M + 1)

    min_cnt = float('inf')
    max_cnt = -float('inf')
    for target in range(A, B + 1):
        count = get_count(arr, target)
        min_cnt = min(count, min_cnt)
        max_cnt = max(count, max_cnt)

    print(min_cnt, max_cnt)


if __name__ == "__main__":
    solve()
