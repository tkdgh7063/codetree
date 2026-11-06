n = int(input())

# Please write your code here.
def count_beautiful(length):
    if length > n:
        return 0

    if length == n:
        return 1

    cnt = 0
    for i in range(1, 5):
        cnt += count_beautiful(length + i)

    return cnt

answer = count_beautiful(0)
print(answer)
