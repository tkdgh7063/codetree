n = int(input())
intervals = [tuple(map(int, input().split())) for _ in range(n)]
s = [interval[0] for interval in intervals]
e = [interval[1] for interval in intervals]

# Please write your code here.
points = []
for a, b in intervals:
    points.append((a, +1))
    points.append((b, -1))
points.sort(key=lambda x: (x[0], -x[1]))

sum_val = 0
answer = 0
for x, v in points:
    sum_val += v
    answer = max(sum_val, answer)

print(answer)
