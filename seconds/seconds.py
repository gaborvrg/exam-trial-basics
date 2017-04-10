def seconds(elements):
    # pass
    # Create a function that takes a list as a parameter,
    # and returns a new list with every second element from the orignal list
    # example: [1, 2, 3, 4, 5] should produce [2, 4]


    # This is an extended slice method. 
    # It works on every second elements on the list from 0 index to end index.

    return elements[::2] 

print(seconds([1, 2, 3, 4, 5])) # should print [2, 4]
