name = 'Vahram'

for letter in name:
    print(letter)

print('_____________________')

num_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for num in num_list:
    if num % 2 == 0:
        print(num)

print('_____________________')

sum_of_num_list = 0

for num in num_list:
    sum_of_num_list += num

print("Sum of our numbers collection equals to {s}".format(s=sum_of_num_list))


print('_____________________')

tup = (1, 2, 3, 4, 5)

for num in tup:
    print(num)

# tuple unpacking


(tup_item_1, tup_item_2, tup_item_3, tup_item_4, tup_item_5) = tup

print("{} - {} - {}".format(tup_item_1, tup_item_2, tup_item_3))

# array unpacking
print('_____________________')


new_num_collection = [1, 2, 3, 4, 5]

a, b, c, d, e = new_num_collection

print(f'{a} - {b} - {c}')

# iterating over dictionaries

print('_____________________')

car = {'color': 'blue', 'manufacturer': 'Opel',
       'model': 'Zafira', 'year': 2003, 'engine': 1.8}

for prop in car:
    print(f'{prop} is {car[prop]}')
