import sys

input = sys.stdin.readline
# print = sys.stdout.write

def solve():
    N = int(input())
    meetings = [tuple(map(int, input().split())) for _ in range(N)]

    meetings.sort(key=lambda x: x[1])

    current_time = 0
    answer = 0
    for s, e in meetings:
        if s < current_time:
            continue

        answer += 1
        current_time = e

    print(answer)

if __name__ == "__main__":
    solve()
