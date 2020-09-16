nm = list(map(int, input().rstrip().split()))
n = nm[0]
m = nm[1]

a = list(map(int, input().rstrip().split()))
b = list(map(int, input().rstrip().split()))

a.sort()
b.sort()

def betweenTwoSets(a, b):
    result = 0
    for i in range(a[-1], b[0] + 1, a[-1]):
        temp = True
        for j in a:
            if i % j != 0:
                temp = False
                break
        if temp:
            for j in b:
                if j % i != 0:
                    temp = False
                    break
        if temp:
            result += 1

    print(result)

def betweenTwoSetsUpdate(a, b):
    result = 0

    for i in range(a[-1], b[0] + 1, a[-1]):
        if all(i % x == 0 for x in a) and all(y % i == 0 for y in b):
            result += 1

    print(result)


betweenTwoSetsUpdate(a, b)
