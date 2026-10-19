import sys

input = sys.stdin.readline

def solve():
    N, K = map(int, input().split())
    bombs = [int(input()) for _ in range(N)]

    R = [0] * N
    dists = dict()
    for i in range(N - 1, -1, -1):
        num = bombs[i]

        if num in dists.keys():
            R[i] = abs(dists[num] - i)
        dists[num] = i

    answer = -float('inf')
    for idx, val in enumerate(R):
        if 0 < val <= K:
            answer = max(answer, bombs[idx])

    print(answer if answer != -float('inf') else -1)

if __name__ == "__main__":
    solve()
