import sys

input = sys.stdin.readline
print = sys.stdout.write

def solve():
    N, M = map(int, input().split())
    fires = list(map(int, input().split()))
    stations = list(map(int, input().split()))

    fires.sort()
    stations.sort()

    answer = -1
    station_index = 0
    for fire_index in range(N):
        while station_index + 1 < M and abs(stations[station_index + 1] - fires[fire_index]) <= abs(stations[station_index] - fires[fire_index]):
            station_index += 1

        answer = max(answer, abs(stations[station_index] - fires[fire_index]))

    print(str(answer) + "\n")

if __name__ == "__main__":
    solve()
