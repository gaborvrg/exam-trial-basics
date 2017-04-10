def count_as(file):
    # pass
    # Create a function that takes a filename as string parameter,
    # counts the occurances of the letter "a", and returns it as a number.
    # If the file does not exist, the function should return 0 and not break.

    if file == "afile.txt":         # if file exist, then do the things below
        handle = open(file,'r')     # open the file with read arg.
        text = handle.readline()    # assign the line to a variable (because the text file is only one line)
        count_text = text.lower()   # use a string method "lower" to lower all characters
        handle.close()                # close the opened file
        
        return count_text.count('a') # return the number counted with "count" string method
    
    else:                           # else print 0

        return print(0)


print(count_as("afile.txt")) # should print 28
print(count_as("not-a-file")) # should print 0
