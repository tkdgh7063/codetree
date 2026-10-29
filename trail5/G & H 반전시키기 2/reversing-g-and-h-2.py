import sys

input = sys.stdin.readline
# print = sys.stdout.write

def solve():
    n = int(input())
    before = list(input().strip())
    target = list(input().strip())

    answer = 0
    for i in range(n - 1, -1, -1):
        b = before[i]
        t = target[i]
        if b != t:
            answer += 1
            for j in range(i + 1):
                if before[j] == "G":
                    before[j] = "H"
                else:
                    before[j] = "G"

    print(answer)

    return

if __name__ == "__main__":
    solve()
