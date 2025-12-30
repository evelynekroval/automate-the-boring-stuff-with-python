supplies = ['pens', 'staplers', 'flamethrowers', 'binders']

print("Let's try printing with `range(len(supplies)`")
for i in range(len(supplies)):
    print(f'Index {i} in supplies is: {supplies[i]}.')

print("Let's try printing directly with `for item in supplies`...")
for item in supplies:
    print(f'Ihe current item in supplies is {item}.')
    
# YESSS it's necessary!
# Because `for i in supplies` leads to item names and therefore strs
# Whereas `for i in range(len(supplies))` leads to item indexes and therefore ints

print("Yet we can use `enumerate()` for less code...")
for index, item in enumerate(supplies):
    print(f"Index {index} in supplies is: {item}")