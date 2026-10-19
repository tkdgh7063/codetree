import sys

input = sys.stdin.readline
print = sys.stdout.write

def solve():
    N = int(input())
    energy = list(map(int, input().split()))  # 장소 사이 이동 시 드는 에너지
    costs = list(map(int, input().split()))  # 장소에서 에너지 1을 채우는데 드는 비용

    INF = float('inf')
    R = [INF] * N  # 현재까지의 에너지 충전 효율
    R[0] = costs[0]
    for i in range(1, N):
        R[i] = min(costs[i], R[i - 1])

    answer = 0
    for i in range(N - 1):
        answer += energy[i] * R[i]
    print(str(answer))

if __name__ == "__main__":
    solve()
