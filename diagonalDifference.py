def diagonalDifference(ar):
    primary = 0
    secondary = 0
    for i in range(len(ar)):
        for j in range(len(ar)):
            if i == j:
                primary += ar[i][j]
        secondary += ar[i][(len(ar)-1) - i]

    return abs(primary - secondary)


def diagonalDifferenceUpdate(ar):
    primary = 0
    secondary = 0
    for i in range(len(ar)):
        primary += ar[i][i]
        secondary += ar[i][-i-1]

    return abs(primary - secondary)


n = int(input().strip())
ar = []

for i in range(n):
    ar.append(list(map(int, input().rstrip().split())))

result = diagonalDifferenceUpdate(ar)
print(result)