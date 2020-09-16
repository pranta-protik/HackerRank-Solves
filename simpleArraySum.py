def simpleArraySum(ar):
    return sum(i for i in ar)


ar_count = int(input())
ar = list(map(int, input().rstrip().split()))
result = simpleArraySum(ar)
print(result)
