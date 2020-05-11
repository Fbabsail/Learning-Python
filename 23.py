numbers = [3, 3, 4, 2, 5, 3, 4, 2]
uniqes = []
for number in numbers:
    if number not in uniqes:
        uniqes.append(number)
print(uniqes)
