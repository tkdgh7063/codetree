import sys

input = sys.stdin.readline

def solve():
    N, S = map(int, input().split())
    arr = list(map(int, input().split()))

    min_length = float('inf')
    current_sum = 0
    right = 0

    # left를 하나씩 옮겨가며 투 포인터 진행
    for left in range(N):
        # 현재 부분합이 S보다 작고, right가 끝에 도달하지 않았다면 오른쪽으로 확장
        while current_sum < S and right < N:
            current_sum += arr[right]
            right += 1

        # 만약 합이 S 이상을 만족했다면, 길이 측정 및 갱신
        if current_sum >= S:
            min_length = min(min_length, right - left)

        # left를 한 칸 오른쪽으로 밀기 전에, 현재 left 위치의 값을 합에서 제외
        current_sum -= arr[left]

    # 만약 조건을 만족하는 구간이 없었다면 -1 출력
    if min_length == float('inf'):
        print(-1)
    else:
        print(min_length)

if __name__ == "__main__":
    solve()
