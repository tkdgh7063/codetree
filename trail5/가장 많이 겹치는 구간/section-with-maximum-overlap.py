import sys

input = sys.stdin.readline
print = sys.stdout.write

def solve():
    N = int(input())
    intervals = [tuple(map(int, input().split())) for _ in range(N)]

    points = []
    M = -1
    for x1, x2 in intervals:
        points.append((x1, 1))
        points.append((x2, -1))
        M = max(M, x2)
    points.sort()

    answer = -1
    sum_val = 0
    for x, v in points:
        sum_val += v

        answer = max(sum_val, answer)

    print(str(answer))

if __name__ == "__main__":
    solve()
