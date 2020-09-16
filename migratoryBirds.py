n = int(input().strip())
sightings = list(map(int, input().rstrip().split()))

numOfAppearance = list()
for i in range(6):
    numOfAppearance.append(sightings.count(i))

print(numOfAppearance.index(max(numOfAppearance)))