import sys

input = sys.stdin.readline
# print = sys.stdout.write

def solve():
    N = int(input())
    before = input()
    target = input()

    start = False
    answer = 0
    # 서로 다른 칸을 찾으면 구간 시작
    # 같은 칸을 찾으면 구간 종료
    for i in range(N):
        if before[i] != target[i] and not start:
            start = True
            answer += 1

        if before[i] == target[i]:
            start = False

    print(answer)

    return


if __name__ == "__main__":
    solve()
