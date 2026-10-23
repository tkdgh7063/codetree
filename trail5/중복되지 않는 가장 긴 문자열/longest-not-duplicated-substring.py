import sys

input = sys.stdin.readline
print = sys.stdout.write

def solve():
    s = input().strip()

    p = set()
    j = 0
    answer = 0
    for i in range(len(s)):
        while j < len(s) and s[j] not in p:
            p.add(s[j])
            j += 1

        p.remove(s[i])
        answer = max(answer, j - i)

    print(str(answer) + "\n")

if __name__ == "__main__":
    solve()
