def count_as(file):
    """Function for opennig file and return the number counted 'a' character in the file """
    try:

        handle = open(file,'r')     # open the file with read arg.
        text = handle.readline()    # assign the line to a variable (because the whole text file is only one line)
        count_text = text.lower()   # use a string method "lower" to lower all characters
        handle.close()                # close the opened file
        
        return count_text.count('a') # return the number counted with "count" string method
    
    except:

        return print(0)


print(count_as("afile.txt")) # should print 28
print(count_as("not-a-file")) # should print 0