tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]


def print_table(tableData:list) -> None: # Because we're printing, not storing.
    """Function which:
    - takes in a list of strings (equal number of items in inner lists), 
    - finds the longest item in each inner list,
    - takes that as the column width, and 
    - outputs a nice table where everything is appropriately spaced."""
    
    # Create a colWidths variable to store for now the column, 
    # even though all items are 0 for now.
    # In this exercise, that's gonna be colWidths = [0, 0, 0]
    colWidths = [0] * len(tableData)
    
    # Accessing all 3 sub_lists & their indexes in tableData
    for index, sub_list in enumerate(tableData):
        # Create the item_length variable to store a list of int lengths
        item_length = []
        # Loop to get to the items of the sub_list
        for item in sub_list:
            # Add to item_length the length of each str item.
            item_length.append(len(item))
        
        # After inner loop complete, ask the outer loop that for each index
        # It replace the colWidths list with the various lengths
        colWidths[index] = max(item_length) # produces [8, 5, 5]
     
    for index, colWidth in enumerate(colWidths):
        for i in range(len(tableData[index])):
            print(tableData[index][i].rjust(colWidth))

    x = 0
    for i in range(len(tableData[0])):
        print(tableData[0][x].rjust(colWidths[0]),
        tableData[1][x].rjust(colWidths[1]),
        tableData[2][x].rjust(colWidths[2]))
        x += 1
        

print_table(tableData)
    
