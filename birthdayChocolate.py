n = int(input().strip())
squares = list(map(int, input().rstrip().split()))
dm = list(map(int, input().rstrip().split()))
d = dm[0]
m = dm[1]
result = 0

for i in range(len(squares) - m + 1):
    if sum(squares[i: i+m]) == d:
        result += 1

print(result)