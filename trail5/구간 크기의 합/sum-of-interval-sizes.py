import sys

input = sys.stdin.readline

def solve():
    n = int(input())
    intervals = [tuple(map(int, input().split())) for _ in range(n)]

    points = []
    for a, b in intervals:
        points.append((a, +1))
        points.append((b, -1))
    points.sort(key=lambda x: (x[0], -x[1]))

    answer = 0
    sum_val = 0
    prev_val = None
    for x, v in points:
        if sum_val == 0 and v == +1:
            prev_x = x
        elif sum_val == 1 and v == -1:
            answer += (x - prev_x)
            prev_x = x
        sum_val += v

    print(answer)

if __name__ == "__main__":
    solve()
