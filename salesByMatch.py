n = int(input().strip())

socks = list(map(int, input().rstrip().split()))

freq = dict()

for sock in socks:
    if sock in freq:
        freq[sock] += 1
    else:
        freq[sock] = 1

pairs = 0

for key, value in freq.items():
    pairs += value // 2
    
print(pairs)