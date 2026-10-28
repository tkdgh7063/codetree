import sys

input = sys.stdin.read
print = sys.stdout.write

def solve():
    input_data = input().split()

    N, K = map(int, input_data[:2])
    coins = [int(x) for x in input_data[2:]]

    answer = 0
    idx = N - 1
    for coin in coins[::-1]:
        answer += K // coin
        K %= coin

        if K <= 0:
            break

    print(str(answer) + "\n")
    return

if __name__ == "__main__":
    solve()
