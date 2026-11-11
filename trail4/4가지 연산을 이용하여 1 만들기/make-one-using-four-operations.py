import sys
from collections import deque

input = sys.stdin.readline

def solve():
    N = int(input())

    # 4가지 연산을 하여 1로 만들기
    # 1 더하기, 1 빼기
    # 2로 나누어 떨어지면 2로 나누기
    # 3으로 나누어 떨어지면 3으로 나누기

    visited = dict()

    def bfs(x):
        queue = deque()
        count = 0

        if x == 1:
            visited[1] = count
            return

        queue.append(x)
        visited[x] = count

        while queue:
            cur = queue.popleft()

            next_nums = [cur + 1, cur - 1]
            if cur % 2 == 0:
                next_nums.append(cur // 2)
            if cur % 3 == 0:
                next_nums.append(cur // 3)

            for next_num in next_nums:
                if 0 <= next_num and next_num not in visited:
                    visited[next_num] = visited[cur] + 1

                    if next_num == 1:
                        return

                    queue.append(next_num)

    bfs(N)

    answer = visited[1]

    print(answer)

    return

if __name__ == "__main__":
    solve()
