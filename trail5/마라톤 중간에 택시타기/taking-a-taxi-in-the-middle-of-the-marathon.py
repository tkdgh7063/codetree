import sys

input = sys.stdin.readline

def get_dist(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

N = int(input())
points = [tuple(map(int, input().split())) for _ in range(N)]

L_arr = [0] * N
R_arr = [0] * N

L_arr[0] = 0
for i in range(1, N):
    L_arr[i] = L_arr[i - 1] + get_dist(points[i], points[i - 1])

R_arr[N - 1] = 0
for i in range(N - 2, -1, -1):
    R_arr[i] = R_arr[i + 1] + get_dist(points[i], points[i + 1])

# 체크포인트 패스
answer = float('inf')
for i in range(1, N - 1):
    dist = L_arr[i - 1] + R_arr[i + 1] + get_dist(points[i - 1], points[i + 1])
    answer = min(dist, answer)

print(answer)
