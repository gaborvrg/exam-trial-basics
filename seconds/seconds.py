def seconds(elements):
    # pass
    # Create a function that takes a list as a parameter,
    # and returns a new list with every second element from the orignal list
    # example: [1, 2, 3, 4, 5] should produce [2, 4]

    return elements[1::2]   # It counts the elements from after the 1st and step to the end. Last nmumber is teh step vaule.

print(seconds([1, 2, 3, 4, 5])) # should print [2, 4]
