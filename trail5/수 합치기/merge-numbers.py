import sys
import heapq

input = sys.stdin.readline
print = sys.stdout.write

def solve():
    N = int(input())
    nums = list(map(int, input().split()))

    heapq.heapify(nums)

    answer = 0
    while len(nums) > 1:
        m1 = heapq.heappop(nums)
        m2 = heapq.heappop(nums)

        cost = m1 + m2

        answer += cost
        heapq.heappush(nums, cost)

    print(str(answer))

if __name__ == "__main__":
    solve()
