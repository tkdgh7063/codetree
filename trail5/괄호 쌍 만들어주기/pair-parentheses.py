import sys

input = sys.stdin.readline
print = sys.stdout.write

def solve():
    A = input().strip()

    R = [0] * len(A)
    num = 0
    for i in range(len(A) - 2, -1, -1):
        if A[i] == A[i + 1] and A[i] == ")":
            num += 1
        R[i] = num

    answer = 0
    for i in range(len(A) - 1):
        if A[i] == A[i + 1] and A[i] == "(":
            answer += R[i]

    print(str(answer) + '\n')

if __name__ == "__main__":
    solve()
