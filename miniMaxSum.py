ar = list(map(int, input().rstrip().split()))
ar.sort()

print(sum(ar[:-1]), sum(ar[1:]))
