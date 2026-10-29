import sys

input = sys.stdin.readline
# print = sys.stdout.write

def solve():
    N = int(input())
    meetings = [tuple(map(int, input().split())) for _ in range(N)]

    meetings.sort(key=lambda x: (x[1], x[0]))

    current_time = 0
    answer = 0
    for s, e in meetings:
        if current_time > s:
            answer += 1
            continue

        current_time = e

    print(answer)

    return

if __name__ == "__main__":
    solve()
