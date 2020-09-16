st = input().rstrip().split()
s = int(st[0])
t = int(st[1])
ab = input().rstrip().split()
a = int(ab[0])
b = int(ab[1])
mn = input().rstrip().split()
m = int(mn[0])
n = int(mn[1])
apples = list(map(int, input().rstrip().split()))
oranges = list(map(int, input().rstrip().split()))

appleDistance = list()
for apple in apples:
    appleDistance.append(apple + a)
orangeDistance = list()
for orange in oranges:
    orangeDistance.append(orange + b)

result = [len([i for i in appleDistance if i in range(s, t+1)]),
          len([i for i in orangeDistance if i in range(s, t+1)])]

for r in result:
    print(r)


