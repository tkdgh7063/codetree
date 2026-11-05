import sys

input = sys.stdin.readline

def get_max(arr):
    m1, m1_idx = -float('inf'), -1
    m2 = -float('inf')
    for idx, num in enumerate(arr):
        if num > m1:
            m2 = m1
            m1 = num
            m1_idx = idx
        elif num > m2:
            m2 = num

    return (m1, m1_idx), m2

def solve():
    N, M = map(int, input().split())

    # 각 층에 M개의 방
    # 직전 층에서 선택한 번호의 방을 연속으로 선택하면 실패

    curr = list(map(int, input().split()))  # 이번 층의 보물 개수 초기화

    for i in range(1, N):
        prev = curr  # 이전 층으로 이동
        treasures = tuple(map(int, input().split()))

        (m1, m1_idx), m2 = get_max(prev)
        # for j in range(M):
        #     if m1 == m2:
        #         curr[j] = m1 + treasures[j]
        #     else:
        #         if j == m1_idx:
        #             curr[j] = m2 + treasures[j]
        #         else:
        #             curr[j] = m1 + treasures[j]
        curr = [
            (m2 if m1 != m2 and j == m1_idx else m1) + treasures[j]
            for j in range(M)
        ]

    answer = max(curr)
    sys.stdout.write(str(answer) + "\n")

if __name__ == "__main__":
    solve()
