# This is the algorithm for bubble sort in Python

"""
The main idea behind this:

input parameter= list of numbers(presumably integers, floating point etc)
procedure= 

        1. We iterate through the list of numbers element wise
        2. If the current element is larger( or smaller, depends upon your desired order) compared to the next element.
                1. We swap their positions
        3. else, we go forward
        4. This goes on the till the end of the list.  
"""


def bubblesort(numlist):       # parameter as list of numbers

    for i in range(len(numlist)-1):
        for j in range(0, len(numlist)-i-1):
            if numlist[j]> numlist[j+1]:
                temp = numlist[j]
                numlist[j]= numlist[j+1]
                numlist[j+1]= temp
    return (numlist)
                