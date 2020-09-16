sTime = input()
mTime = list(sTime[:-2])
if 'AM' in sTime:
    if int(sTime[:2]) == 12:
        mTime[:2] = '00'
else:
    if int(sTime[:2]) in range(1, 12):
        mTime[:2] = str(int(sTime[:2]) + 12)

print(''.join(mTime))
