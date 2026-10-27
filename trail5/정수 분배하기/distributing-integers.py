import sys

input = sys.stdin.readline
# print = sys.stdout.write

def is_possible(arr, K, M):
    if K == 0:
        return False

    cnt = 0
    for num in arr:
        cnt += num // K

    return cnt >= M

def solve():
    N, M = map(int, input().split())
    nums = list(int(input()) for _ in range(N))

    # 특정 수 K를 정하여 각 수를 K로 나눈 몫의 총합이 M 이상인지 체크
    left = 0
    right = max(nums)
    K = 0
    while left <= right:
        mid = (left + right) // 2

        if is_possible(nums, mid, M):
            left = mid + 1
            K = max(K, mid)
        else:
            right = mid - 1

    return K

if __name__ == "__main__":
    answer = solve()
    print(answer)
