# Using built-in method list() and adding items later or using append(), insert()

items = list()
print("Empty list:", items)

items.append('fruits')
items.append(1707)
items.append(12.5)
items.insert(1, 2+3j)

print(items)


# Using List Notation: []
fruit_list = ['apples', 'grapes', 'bananas']
print(fruit_list)


# Using List Comprehension
custom_list = [elements for elements in input('enter list: ').split(' ')]
print(custom_list)


# Using For Loop
string1 = input('enter any string: ').strip(' ')
char_list = []
for ch in string1:
    char_list.append(ch)
print(char_list)
