import sys

input = sys.stdin.readline
print = sys.stdout.write

def solve():
    N = int(input())

    answer = 0
    current_remainder = 0
    first_index = [-1] * 7
    for i in range(N):
        num = int(input())
        current_remainder = (current_remainder + num) % 7

        if current_remainder == 0:
            answer = max(answer, i + 1)
        else:
            if first_index[current_remainder] == -1:
                first_index[current_remainder] = i
            else:
                answer = max(answer, i - first_index[current_remainder])

    print(str(answer))

if __name__ == "__main__":
    solve()
