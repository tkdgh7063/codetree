import sys

input = sys.stdin.readline
# print = sys.stdout.write

def solve():
    N = int(input())
    arr = list(map(int, input().split()))

    answer = 0
    dxs = [-1, 0, 1]
    for i in range(1, N):
        if arr[i - 1] == 0:
            answer += 1
            for dx in dxs:
                idx = i + dx
                if idx < N:
                    arr[idx] = abs(arr[idx] - 1)

    if arr[-1] != 1:
        print("-1")
    else:
        print(str(answer) + "\n")

    return

if __name__ == "__main__":
    solve()
