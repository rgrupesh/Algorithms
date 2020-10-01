# Selection Sort

def selection_sort(numlist):        
    for i in range(len(numlist)):
        min = i
        
        for j in range(i + 1, len(numlist)):
            if numlist[j] < numlist[min]:
                min = j

        numlist[min], numlist[i] = numlist[i], numlist[min]
            
    return numlist
