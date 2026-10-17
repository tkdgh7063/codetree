import sys

input = sys.stdin.readline
print = sys.stdout.write

def solve():
    n = int(input())
    intervals = [tuple(map(int, input().split())) for _ in range(n)]

    points = []
    for a, b in intervals:
        points.append((a, +1))
        points.append((b, -1))
    points.sort(key=lambda x: (x[0], -x[1]))

    sum_val = 0
    answer = 0
    for x, v in points:
        sum_val += v
        answer = max(sum_val, answer)

    print(str(answer) + "\n")

if __name__ == "__main__":
    solve()
