import sys

input = sys.stdin.readline
# print = sys.stdout.write

def solve():
    s = input().strip()

    p = ""
    j = 0
    answer = 0
    for i in range(len(s)):
        while j < len(s) and s[j] not in p:
            p += s[j]
            j += 1

        p = p[1:]

        answer = max(answer, j - i)

    print(answer)

if __name__ == "__main__":
    solve()
