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

        i, j = 0, 1
        while i < N:
            while j < N and dots[j] - dots[i] < dist:
                j += 1

            if j != N:
                cnt += 1
            i = j

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
