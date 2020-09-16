x1, v1, x2, v2 = map(int, input().rstrip().split())

if x1 == x2 and v1 == v2:
    print('YES')

elif x1 > x2 and v1 < v2:
    pos1 = x1
    pos2 = x2
    while True:
        pos1 += v1
        pos2 += v2

        if pos1 == pos2:
            print('YES')
            break
        elif pos2 > pos1:
            print('NO')
            break

elif x2 > x1 and v2 < v1:
    pos1 = x1
    pos2 = x2
    while True:
        pos1 += v1
        pos2 += v2

        if pos1 == pos2:
            print('YES')
            break
        elif pos1 > pos2:
            print('NO')
            break

else:
    print('NO')
