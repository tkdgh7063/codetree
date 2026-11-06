import sys
sys.setrecursionlimit(10 ** 9)

input = sys.stdin.readline

def solve():
    # 길이가 N인 식의 각 소문자 알파벳에 1~4 정수를 넣어 최대 결과
    exp = input().strip()

    char = set()  # 알파벳
    for ch in exp:
        if ord('a') <= ord(ch) <= ord('f'):
            char.add(ch)

    N = len(char)  # 알파벳 개수

    def calc(nums):
        # 현재 선택한 숫자들로 식 계산
        d = dict()

        for c, n in zip(char, nums):
            d[c] = n

        res = d[exp[0]]
        idx = 1
        while idx < len(exp):
            c = exp[idx]
            idx += 1
            if c == "+":
                res += d[exp[idx]]
            elif c == "-":
                res -= d[exp[idx]]
            elif c == "*":
                res *= d[exp[idx]]
            idx += 1

        return res

    nums = []
    answer = -float('inf')
    def choose(curr):
        # 현재 고른 숫자 개수가 curr개
        nonlocal answer

        if curr == N:
            # 모든 숫자 선택 완료
            res = calc(nums)
            answer = max(answer, res)
            return

        for i in range(1, 5):
            nums.append(i)
            choose(curr + 1)
            nums.pop()

    choose(0)

    print(answer)


if __name__ == "__main__":
    solve()
