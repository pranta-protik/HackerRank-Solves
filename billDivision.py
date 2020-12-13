nk = list(map(int, input().rstrip().split()))
n = nk[0]
k = nk[1]

bills = list(map(int, input().rstrip().split()))

charge = int(input().strip())

actual = sum([bills[i] for i in range(len(bills)) if i != k]) // 2

if charge == actual:
    print('Bon Appetit')
else:
    print(charge - actual)
