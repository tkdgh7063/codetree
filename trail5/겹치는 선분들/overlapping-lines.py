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

    points.sort(key=lambda x: (x[0], x[1]))

    sum_val = 0
    s = set()
    answer = 0
    for x, v in points:
        sum_val += v
        if sum_val >= K:
            if v == +1 and not s:
                s.add(x)
        else:
            if v == -1 and s:
                answer += abs(s.pop() - x)

    print(str(answer))

if __name__ == "__main__":
    solve()
