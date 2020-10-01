def binarySearch(arr, l, r, x): 
    if r >= l: 
        mid = l + (r - l) // 2

        if arr[mid] == x: 
            return mid 
        elif arr[mid] > x: 
            return binarySearch(arr, l, mid-1, x) 
        else: 
            return binarySearch(arr, mid + 1, r, x) 

    else: 
        return -1

if __name__=='__main__':
    lst = []

    n = int(input("Enter numbers of elements:"))
    print("Enter numbers manually")
    for i in range(0,n):
        ele=int(input())
        lst.append(ele)

    num = int(input("Enter number to search:")) 

    result = binarySearch(lst, 0, len(lst)-1, num) 

    if result != -1: 
        print ("Element is present at index % d" % result) 
    else: 
        print ("Element is not present in array") 
        