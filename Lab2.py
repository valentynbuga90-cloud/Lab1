main_list = [12, 3, 7, 18, 25, 4, 9, 2, 30, 15,
             "banana", "apple", "pear", "kiwi", "mango",
             "grape", "cherry", "orange", "plum", "melon"]

print(main_list)

int_list = sorted([x for x in main_list if isinstance(x, int)])
str_list = sorted([x for x in main_list if isinstance(x, str)])

sorted_list = int_list + str_list

even_list = [x for x in int_list if x % 2 == 0]

caps_list = [x.upper() for x in str_list]

print(sorted_list)

print(even_list)

print(caps_list)
