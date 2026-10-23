import sys

input = sys.stdin.readline
print = sys.stdout.write

def solve():
    word, K = input().split()
    K = int(K)

    counter = dict()
    start, end = 0, 0
    answer = 0
    for end in range(len(word)):
        ch = word[end]
        counter[ch] = counter.get(ch, 0) + 1

        while len(counter) > K:
            ch = word[start]
            counter[ch] -= 1

            if counter.get(ch) == 0:
                del counter[ch]
            start += 1

        answer = max(answer, end - start + 1)

    print(str(answer) + '\n')

if __name__ == "__main__":
    solve()
