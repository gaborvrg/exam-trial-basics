def seconds(elements):
    """Function for returns a new list with every second element from the orignal list"""
    
    # first few commit went to the base directory(exam-trial-basics)

    return elements[1::2]   # It counts the elements from after the 1st and step to the end. Last nmumber is the step vaule.

print(seconds([1, 2, 3, 4, 5])) # should print [2, 4]
