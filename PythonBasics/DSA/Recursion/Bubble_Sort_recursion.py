

arr = [5, 4, 3, 2, 1]

# Set default n to None so it doesn't look for 'arr' during definition
def bubble_sort(arr, n=None, index=0):
    # Initialize n on the very first call
    if n is None:
        n = len(arr)

    # base-case:1 
    if n == 1:
        return

    # base-case:2
    if index == n - 1:
        return bubble_sort(arr, n - 1, 0)

    # if this swap.
    if arr[index] > arr[index + 1]:
        arr[index], arr[index + 1] = arr[index + 1], arr[index]

    # this thing is for all .
    return bubble_sort(arr, n, index + 1)

bubble_sort(arr)
print(arr)  # Output: [1, 2, 3, 4, 5]
  

