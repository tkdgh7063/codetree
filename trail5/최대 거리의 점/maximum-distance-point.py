import sys

input = sys.stdin.read
print = sys.stdout.write

def solve():
    input_data = input().split()
    if not input_data:
        return

    N = int(input_data[0])
    M = int(input_data[1])
    dots = [int(x) for x in input_data[2:]]

    dots.sort()

    def is_possible(dist):
        cnt = 1

        last_idx = 0
        for i in range(1, N):
            if dots[i] - dots[last_idx] >= dist:
                cnt += 1
                last_idx = i

        return cnt >= M

    left = 0
    right = max(dots)
    answer = 0
    while left <= right:
        mid = (left + right) // 2

        if is_possible(mid):
            answer = max(answer, mid)
            left = mid + 1
        else:
            right = mid - 1

    print(str(answer) + "\n")
    return

if __name__ == "__main__":
    solve()
