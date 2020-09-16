n = int(input().strip())
candles = list(map(int, input().rstrip().split()))
candles.sort()
print(len([i for i in candles if i == candles[-1]]))
