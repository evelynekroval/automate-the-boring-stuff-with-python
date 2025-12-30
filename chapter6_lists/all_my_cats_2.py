cat_names: list[str] = [] #type ignore
while True:
    print('Enter the name of cat ' + str(len(cat_names) + 1) +
      ' (Or enter nothing to stop.):')
    name = input().title()
    if name == '':
        break
    cat_names.append(name)  # List concatenation
print('The cat names are:')
for name in cat_names:
    print('  ' + name)