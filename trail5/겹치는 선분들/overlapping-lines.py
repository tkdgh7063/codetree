import sys

input = sys.stdin.readline
print = sys.stdout.write

def solve():
    N, K = map(int, input().split())
    M = []
    dirs = []

    for _ in range(N):
        m, d = input().split()
        M.append(int(m))
        dirs.append(d)

    points = []
    cur = 0
    for m, dir in zip(M, dirs):
        if dir == "L":
            points.append((cur, -1))
            cur -= m
            points.append((cur, +1))
        else:
            points.append((cur, +1))
            cur += m
            points.append((cur, -1))

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
