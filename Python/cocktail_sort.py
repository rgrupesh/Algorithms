def cocktailSort(arr):
    isSwapped = True
    First = 0
    Last = len(arr)-1
    while isSwapped is True:
        isSwapped = False
        for i in range(First, Last):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                isSwapped = True

        if isSwapped is False:
            break

        isSwapped = False
        Last = Last-1

        for i in range(Last-1, First-1, -1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                isSwapped = True
        First = First+1

n = int(input("Enter number of elements : "))
#keep white space between numbers while giving input
arr = list(map(int, input("\nEnter the numbers : ").strip().split()))[:n]
cocktailSort(arr)
print("Sorted array is: ")
print(arr)