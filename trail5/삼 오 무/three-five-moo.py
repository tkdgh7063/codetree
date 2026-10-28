import sys

input = sys.stdin.readline
print = sys.stdout.write

def get_seq(N):
    # N이 적히는 순서
    seq = N - N // 3 - N // 5 + N // 15

    return seq

def solve():
    N = int(input())

    # 숫자 X를 골랐을 때 해당 X가 몇번째인가?
    left = 1
    right = 10 ** 10
    answer = 0
    while left <= right:
        mid = (left + right) // 2

        seq = get_seq(mid)
        if seq >= N:
            answer = mid
            right = mid - 1
        else:
            left = mid + 1

    return answer

if __name__ == "__main__":
    answer = solve()
    print(str(answer) + '\n')
