from bisect import bisect_left, bisect_right
import sys

input = sys.stdin.readline
print = sys.stdout.write

def solve():
    N, M = map(int, input().split())
    dots = list(map(int, input().split()))
    lines = list(tuple(map(int, input().split())) for _ in range(M))

    dots.sort()

    for x, y in lines:
        upper = bisect_right(dots, y)
        lower = bisect_left(dots, x)

        print(f"{upper-lower}\n")

    return


if __name__ == "__main__":
    solve()
