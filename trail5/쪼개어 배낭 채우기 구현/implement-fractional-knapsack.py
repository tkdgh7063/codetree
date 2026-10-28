import sys

input = sys.stdin.readline
# print = sys.stdout.write


def solve():
    N, M = map(int, input().split())
    jewels = [tuple(map(int, input().split())) for _ in range(N)]

    # 무게 당 가격이 높은 순서대로 정렬
    jewels.sort(key=lambda x: (x[1] / x[0]), reverse=True)

    weight = 0
    answer = 0
    for w, v in jewels:
        if M - weight >= w:
            answer += v
            weight += w
        else:
            answer += (v / w) * (M - weight)
            weight = M

    print(f"{answer:.3f}")

    return


if __name__ == "__main__":
    solve()
