BOOK_INSTRUCTIONS = """
Say you’re creating a medieval fantasy video game. 
The data structure to model the player’s inventory 
is a dictionary whose keys are strings describing the item 
in the inventory and whose values are integers detailing 
how many of that item the player has. 
For example, the dictionary value 
{'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12} 
means the player has one rope, six torches, 42 gold coins, and so on.

Write a function named display_inventory() that would take any 
possible “inventory” and display it like the following:

Inventory:
12 arrow
42 gold coin
1 rope
6 torch
1 dagger
Total number of items: 62
Hint: You can use a for loop to loop through all keys in a dictionary.

stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def display_inventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        # FILL THIS PART IN
    print("Total number of items: " + str(item_total))

display_inventory(stuff)
"""

stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def display_inventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        print(f"{v} {k}")
        item_total += v
        
    print(f"Total number of items: {item_total}")
    

def add_to_inventory(inventory:dict, added_items:list):
    # Your code goes here.
    
    # For each list item in the new added_items list
    for item in added_items:
        # Check if the item already exists as a key in the inventory
        if item in inventory.keys():
            # If it does, then add 1 to its value
            inventory[item] += 1
        # If it doesn't, add the item as a new key with a default count of 1.    
        else:
            inventory.setdefault(item, 1)
    return inventory

inv = {'gold coin': 42, 'rope': 1}
dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = add_to_inventory(inv, dragon_loot)

display_inventory(inv)
