def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


def binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    while left <= right-1:
        mid = (left+right)//2
        if arr[mid] == target:
            return mid
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


if __name__ == "__main__":
    # arr = [3,5,7,8,4,1,9,20]
    sort_arr = [1,2,3,4,5,6,7,8,10,11,12,13]
    # new = linear_search(arr, 1)
    new = binary_search(sort_arr, 9)
    print(new)