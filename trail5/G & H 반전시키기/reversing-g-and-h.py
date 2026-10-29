import sys

input = sys.stdin.readline
print = sys.stdout.write

def solve():
    N = int(input())
    before = input().strip()
    target = input().strip()

    start = False
    answer = 0
    # 서로 다른 칸을 찾으면 구간 시작
    # 같은 칸을 찾으면 구간 종료
    for b, t in zip(before, target):
        if b != t and not start:
            start = True
            answer += 1

        if b == t:
            start = False

    print(str(answer) + "\n")

    return

if __name__ == "__main__":
    solve()
