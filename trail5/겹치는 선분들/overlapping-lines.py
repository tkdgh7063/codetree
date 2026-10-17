import sys

input = sys.stdin.readline
print = sys.stdout.write

def solve():
    N, K = map(int, input().split())

    cur = 0
    points = []
    for _ in range(N):
        m, d = input().split()
        m = int(m)
        if d == "L":
            nxt = cur - m
            points.append((nxt, +1))
            points.append((cur, -1))

        else:
            nxt = cur + m
            points.append((cur, +1))
            points.append((nxt, -1))

        cur = nxt

    points.sort(key=lambda x: x[0])

    sum_val = 0
    prev_x = points[0][0]
    answer = 0
    for x, v in points:
        if sum_val >= K:
            answer += (x - prev_x)
        sum_val += v
        prev_x = x

    print(str(answer))

if __name__ == "__main__":
    solve()
