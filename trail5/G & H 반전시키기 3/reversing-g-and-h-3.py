import sys

input = sys.stdin.readline
print = sys.stdout.write

def solve():
    N = int(input())
    before = list(input().strip())
    target = list(input().strip())

    length = 0
    answer = 0
    for idx, (b, t) in enumerate(zip(before, target)):
        if b != t:
            length += 1
            if length == 4:
                answer += 1
                length = 0
        else:
            if length:
                answer += 1
                length = 0

    if length:
        answer += 1

    print(str(answer) + "\n")

    return

if __name__ == "__main__":
    solve()
