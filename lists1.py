wizard_list = ['spider legs', 'toe of frog', 'eye of newt',
'bat wing', 'slug butter', 'snake dandruff']
print(wizard_list)
print(wizard_list[2])
wizard_list[2] = 'snail tongue'
print(wizard_list[2], " and ",wizard_list[0])
print(wizard_list[2:5])
some_numbers = [42, 69, 1, 0, 99]
print(some_numbers)
numbers_and_strings = ['hello', 42, 'smeg', 999, 'awright', 69]
print(numbers_and_strings)
print(numbers_and_strings[1] * 8)
print(numbers_and_strings[2] * 8 )
array_of_array = [some_numbers,numbers_and_strings]
print(array_of_array)
numbers_and_strings.append('queef')
print(numbers_and_strings)
del array_of_array[0]
print(array_of_array)