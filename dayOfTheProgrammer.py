y = int(input().strip())

# feb = 28

# if y == 1918:
#     feb = 15
# elif 1700 <= y <= 1917:
#     if y % 4 == 0:
#         feb = 29
#     else:
#         feb = 28
# elif y > 1918:
#     if y % 400 == 0:
#         feb = 29
#     elif y % 4 == 0 and y % 100 != 0:
#         feb = 29
#     else:
#         feb = 28

# totalDays = 31 + feb + 31 + 30 + 31 + 30 + 31 + 31
# day = 256 - totalDays

if y < 1918:
    print('12.09.' + str(y) if y % 4 == 0 else '13.09.' + str(y))
elif y > 1918:
    print('12.09.' + str(y) if y % 400 == 0 or (y % 4 == 0 and y % 100 != 0) else '13.09.' + str(y))
else:
    print('26.09.' + str(y))


# print(str(day) + ".09." + str(y))
