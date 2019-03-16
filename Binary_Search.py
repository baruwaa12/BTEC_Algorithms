import math

# Binary search
# Check if the element your looking for is greater than or less than the element in the middle
# If greater than - all elements behind the middle number are discarded
# If less than - all elements in front of the middle number are discarded


def binary_search(Array, ItemWanted):
    left = 1
    right = len(Array)
    Middle_number = 0
    ItemFound = False
    while (left <= right) and (ItemFound == False):
        Middle_number = math.floor((left + right)/2)
        if Array[Middle_number] == ItemWanted:
            ItemFound = True
        if Array[Middle_number] > ItemWanted:
            right = Middle_number - 1
        if Array[Middle_number] < ItemWanted:
            left = Middle_number + 1
    return ItemFound

result = binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 8)
print(result)