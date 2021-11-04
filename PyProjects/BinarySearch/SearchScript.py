def binarySearch(arr, low, high, x):
    #   Check base case
    if high >= low:
        mid = (high + low) // 2

        #   Checks if x is mid itself
        if arr[mid] == x:
            return mid
        
        #   If x is less than mid, then it can only be on the left side
        elif arr[mid] > x:
            return binarySearch(arr, low, mid - 1, x)
 
        #   Else x can only be on the right side
        else:
            return binarySearch(arr, mid + 1, high, x)

    else:
        #Element is not present in the array
        return -1

#   Test data
theArr = [1, 3, 4, 5, 13, 20, 25, 40, 42, 44, 53]
x = 25

#   Function call
result = binarySearch(theArr, 0, len(theArr) - 1, x)

if result != -1:
    print(f"{x} is present at index: ", str(result))
else:
    print(f"{x} is not present in array")