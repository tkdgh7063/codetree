import sys

input = sys.stdin.readline
print = sys.stdout.write

def solve():
    N, M = map(int, input().split())
    coins = list(map(int, input().split()))

    # 최소 동전 수
    dp = [None] * (M + 1)
    dp[0] = 0

    for money in range(1, M + 1):
        for coin in coins:
            # 현재 돈보다 동전이 크면 패스
            if money < coin:
                continue

            prev = money - coin

            # 이전 금액을 만들 수 없으면 패스
            if dp[prev] is None:
                continue

            candidate = dp[prev] + 1

            if dp[money] is None or candidate < dp[money]:
                dp[money] = candidate


    answer = dp[M] if dp[M] is not None else -1
    print(str(answer) + "\n")

    return

if __name__ == "__main__":
    solve()
