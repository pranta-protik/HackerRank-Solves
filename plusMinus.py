def plusMinus(ar):
    pos = 0
    neg = 0
    zero = 0
    length = len(ar)

    for i in ar:
        if i > 0:
            pos += 1
        elif i < 0:
            neg += 1
        else:
            zero += 1
    print(round(pos / length, 6), round(neg / length, 6), round(zero / length, 6), sep='\n')


def plusMinusUpdate(ar):
    print(round(len([i for i in ar if i > 0]) / len(ar), 6))
    print(round(len([i for i in ar if i < 0]) / len(ar), 6))
    print(round(len([i for i in ar if i == 0]) / len(ar), 6))


n = int(input().strip())
ar = list(map(int, input().rstrip().split()))
plusMinusUpdate(ar)
