import sys

input = sys.stdin.readline
# print = sys.stdout.write

def solve():
    N = int(input())
    info = [tuple(map(int, input().split())) for _ in range(N)]  # 시작, 끝, 금액

    info.sort(key=lambda x: x[1])

    dp = [x[2] for x in info]

    for i in range(1, N):
        for j in range(i):
            if info[j][1] < info[i][0]:
                dp[i] = max(dp[i], dp[j] + info[i][2])

    print(max(dp))

    return

if __name__ == "__main__":
    solve()
