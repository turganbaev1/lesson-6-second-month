letters = []
numbers = []
data_tuple = ('h', 6.13, 'C', 'e', 'T', True, 'k', 'e', 3, 'e', 1, 'g')
for i in data_tuple:
    if type(i) == str or type(i) ==bool:
        letters.append(i)
    elif type(i) == int or type(i) == float:
        numbers.append(i)
del numbers[0]
numbers.insert(1, 2)
numbers.sort()
letters.append(letters.pop(letters.index(True)))
letters.reverse()
letters[1] = "G"
letters[-2] = "c"
letters1 = tuple(letters)
numbers1 = tuple(numbers)
print(letters1)
print(numbers1)