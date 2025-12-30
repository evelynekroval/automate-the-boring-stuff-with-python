import random

my_list = ["a", "A", "B", "b", "C", "D", "E", "F", "b", "c", "d", "e", "f"]

random.shuffle(my_list)

for i in my_list:
    print(f"{i} is at index {my_list.index(i)}.")

print(my_list)

my_list.sort(key=str.lower)
print("And now the sorted list")
print(my_list)