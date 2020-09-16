n = int(input().strip())
scores = list(map(int, input().rstrip().split()))

maximum = scores[0]
minimum = scores[0]
result = [0,0]

for i in scores:
    if i > maximum:
        maximum = i
        result[0] += 1
    if i < minimum:
        minimum = i
        result[1] += 1

print(result[0], result[1])