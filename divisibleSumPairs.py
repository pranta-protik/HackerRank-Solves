nk = list(map(int, input().rstrip().split()))
n = nk[0]
k = nk[1]

ar = list(map(int, input().rstrip().split()))

result = 0

for i in range(n - 1):
    for j in range(i + 1, n):
        if (ar[i] + ar[j]) % k == 0:
            result += 1
print(result)