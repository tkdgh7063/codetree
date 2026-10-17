import sys
import heapq

input = sys.stdin.readline
# print = sys.stdout.write

def solve():
    N = int(input())
    intervals = [tuple(map(int, input().split())) for _ in range(N)]

    points = []
    for idx, (a, b) in enumerate(intervals):
        points.append((a, +1, idx))
        points.append((b, -1, idx))
    points.sort(key=lambda x: x[0])

    answer = [None] * N
    computer_map = dict()
    computer_num = []
    next_num = 1
    for x, v, idx in points:
        if v == +1:
            if not computer_num:
                heapq.heappush(computer_num, next_num)
                next_num += 1

            num = heapq.heappop(computer_num)
            computer_map[idx] = num  # 사용자 번호: 컴퓨터 번호
        else:
            num = computer_map.pop(idx)
            answer[idx] = num
            heapq.heappush(computer_num, num)

    print(*(answer), sep=' ')

if __name__ == "__main__":
    solve()
