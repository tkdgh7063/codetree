import sys

input = sys.stdin.read
# print = sys.stdout.write

def solve():
    input_data = input().split()

    N, K = map(int, input_data[:2])
    coins = [int(x) for x in input_data[2:]]

    answer = 0
    idx = N - 1
    while K > 0:
        answer += K // coins[idx]
        K %= coins[idx]
        idx -= 1

    print(answer)
    return

if __name__ == "__main__":
    solve()
