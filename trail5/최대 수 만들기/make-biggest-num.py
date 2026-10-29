import sys
from functools import cmp_to_key

input = sys.stdin.read
print = sys.stdout.write

def compare(x, y):
    if x + y >= y + x:
        return -1
    else:
        return 1

def solve():
    input_data = input().split()
    if not input_data:
        return

    N = int(input_data[0])
    nums = input_data[1:]
    MAX_LENGTH = 10

    # nums 정렬
    # nums.sort(key=cmp_to_key(compare))
    nums.sort(key=lambda x: (x * MAX_LENGTH), reverse=True)

    answer = "".join(nums)
    print(answer)

    return

if __name__ == "__main__":
    solve()
