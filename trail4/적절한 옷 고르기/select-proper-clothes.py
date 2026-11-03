import sys

input = sys.stdin.readline
print = sys.stdout.write

def solve():
    N, M = map(int, input().split())
    clothes = [tuple(map(int, input().split())) for _ in range(N)]  # 시작 날짜, 마지막 날짜, 옷의 화려함

    # 옷을 적절히 입어 최대 만족도
    # 만족도는 입은 옷 사이의 화려함의 차이의 합
    # 만족도가 높으려면 같은 옷을 2일 연속으로 입으면 안 됨
    dp = [[-1] * N for _ in range(M)]
    for i in range(N):
        s, e, v = clothes[i]
        if s <= 1 <= e:
            dp[0][i] = 0

    # dp[i][j] = i번째 날에 j번 옷을 입었을 때 최대 만족도
    for i in range(1, M):
        for j in range(N):
            for k in range(N):
                if dp[i - 1][k] == -1:
                    continue

                s1, e1, v1 = clothes[j]  # 이번에 고른 옷
                s2, e2, v2 = clothes[k]  # 전날에 고른 옷

                if s1 <= i + 1 <= e1 and s2 <= i <= e2:
                    # 해당 옷들을 고를 수 있음
                    score = abs(v1 - v2)
                    dp[i][j] = max(dp[i][j], dp[i - 1][k] + score)

    answer = max(a for row in dp for a in row)
    print(str(answer) + "\n")

    return

if __name__ == "__main__":
    solve()
