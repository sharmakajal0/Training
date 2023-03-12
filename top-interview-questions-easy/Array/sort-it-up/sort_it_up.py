'''
Question: You are given an array `arr`, consisting of only zeroes, ones and twos.
Sort the same array in-place and return it.
NOTE: Do not create a new array.
Input: 
    n: size of the array
    arr: array itself

Output:
    sorted array

Constraint:
    1 <= n <= 100
'''

def sortItUp(arr: list, n: int) -> list:
    left = 0
    right = n - 1
    pointer = 0

    while pointer <= right:
        if arr[pointer] == 2:
            arr[left], arr[right] = arr[right], arr[left]
            right -= 1
        elif arr[pointer] == 1:
            pointer += 1
        else:
            arr[pointer], arr[left] = arr[left], arr[pointer]
            left += 1
            pointer += 1

    return arr

n = 5
arr = [2, 0, 1, 0, 2]
print(sortItUp(arr, n))