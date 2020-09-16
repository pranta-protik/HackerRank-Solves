import math

nh = input().split()
n = int(nh[0])
h = int(nh[1])
location = list(map(int, input().rstrip().split()))
updateLocation = []
diff = math.floor(math.sqrt(h))

