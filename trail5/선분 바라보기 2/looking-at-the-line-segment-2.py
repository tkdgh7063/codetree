import sys
import heapq

input = sys.stdin.readline
print = sys.stdout.write

def solve():
    N = int(input())
    intervals = [tuple(map(int, input().split())) for _ in range(N)]

    points = []
    for idx, (y, x1, x2) in enumerate(intervals):
        points.append((x1, +1, y, idx))
        points.append((x2, -1, y, idx))
    points.sort(key=lambda x: (x[0], x[2]))

    segments = []
    checked = set()
    answer = set()
    for x, v, y, idx in points:
        while segments and segments[0][1] in checked:
            heapq.heappop(segments)

        if segments:
            answer.add(segments[0][1])

        if v == +1:
            heapq.heappush(segments, (y, idx))
        else:
            checked.add(idx)

    print(str(len(answer)) + '\n')

if __name__ == "__main__":
    solve()
