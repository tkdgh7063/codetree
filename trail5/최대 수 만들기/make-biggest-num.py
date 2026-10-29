import sys
from functools import cmp_to_key

input = sys.stdin.read
print = sys.stdout.write

def solve():
    input_data = input().split()
    if not input_data:
        return

    N = int(input_data[0])
    nums = input_data[1:]
    MAX_LENGTH = 9

    # nums 정렬
    nums.sort(key=lambda x: (x * MAX_LENGTH), reverse=True)

    print("".join(nums))

    return

if __name__ == "__main__":
    solve()
