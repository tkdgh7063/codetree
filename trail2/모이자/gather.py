import sys

input = sys.stdin.readline

def solve():
    N = int(input())
    A = list(map(int, input().split()))

    def get_dist(idx):
        dist = 0
        for i, n in enumerate(A):
            dist += abs(idx - i) * n

        return dist

    answer = float('inf')
    for i in range(N):
        dist = get_dist(i)
        answer = min(dist, answer)

    print(answer)

if __name__ == "__main__":
    solve()
