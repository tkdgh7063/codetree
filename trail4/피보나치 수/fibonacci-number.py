import sys

input = sys.stdin.readline
print = sys.stdout.write

def fibo(num):
    dp = [-1] * (45 + 1)
    dp[1] = 1
    dp[2] = 1

    for i in range(3, num + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[num]

def solve():
    N = int(input())

    answer = fibo(N)

    print(str(answer) + "\n")

    return

if __name__ == "__main__":
    solve()
