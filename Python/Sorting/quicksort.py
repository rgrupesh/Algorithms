def partition(arr, low, high):
  pivot = arr[high]
  lower = low - 1

  for i in range(low, high):
    if arr[i] < pivot:
      arr[i], arr[lower] = arr[lower], arr[i]
      lower += 1
    
  arr[high], arr[lower + 1] = arr[lower + 1], arr[high]
  return lower + 1

def quicksort(arr, low, high):
  if low < high:
    pi = partition(arr, low, high)
    quicksort(arr, low, pi - 1)
    quicksort(arr, pi + 1, low)

def main():
  my_arr = [10, 2, 5, 8, 1]
  quicksort(my_arr, 0, len(my_arr)-1)
  print(my_arr)
  print("Hello World!")

if __name__ == "__main__":
  main()