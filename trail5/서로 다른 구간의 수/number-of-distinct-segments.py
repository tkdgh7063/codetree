import sys

input = sys.stdin.readline
print = sys.stdout.write

def solve():
    N = int(input())
    intervals = [tuple(map(int, input().split())) for _ in range(N)]

    points = []
    for idx, (a, b) in enumerate(intervals):
        points.append((a, +1, idx))
        points.append((b, -1, idx))

    points.sort()

    segs = set()
    cnt = 0
    for x, v, idx in points:
        if v == +1:
            if not segs:
                cnt += 1
            segs.add(idx)

        else:
            segs.remove(idx)
    print(str(cnt))

if __name__ == "__main__":
    solve()
