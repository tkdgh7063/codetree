import sys

input = sys.stdin.readline
print = sys.stdout.write

def binary_search(nums, target):
    N = len(nums)

    left = 0
    right = N - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid + 1
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1

def solve():
    N, M = map(int, input().split())
    nums = list(map(int, input().split()))
    queries = [int(input()) for _ in range(M)]

    for query in queries:
        idx = binary_search(nums, query)
        print(f"{idx}\n")

    return

if __name__ == "__main__":
    solve()
