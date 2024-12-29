def bubble_sort(arr):
    for i in range(len(arr)-1):
        if_sorted = False
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                if_sorted = True
        if not if_sorted:
            return arr
    return arr


def selection_sort(arr):
    for i in range(len(arr)-1):
        temp_lowest_idx = i
        min_val = arr[i]
        for j in range(i, len(arr)):
            if arr[j] < min_val:
                temp_lowest_idx = j
        next_elem = arr.pop(temp_lowest_idx)
        arr.insert(i, next_elem)
    return arr


def selection_sort_2(arr):
    for i in range(len(arr)-1):
        temp_lowest_idx = i
        for j in range(i, len(arr)):
            if arr[j] < arr[temp_lowest_idx]:
                temp_lowest_idx = j
        arr[temp_lowest_idx], arr[i] = arr[i], arr[temp_lowest_idx]
    return arr


def insertion_sort_2(arr):
    for i in range(1, len(arr)):
        insert_index = i
        current_value = arr[i]
        for j in range(i-1, -1, -1):
            if arr[j] > current_value:
                insert_index = j
            else:
                break
        arr[insert_index+1:i+1] = arr[insert_index:i]
        arr[insert_index] = current_value
    return arr



if __name__ == "__main__":
    # new = bubble_sort([6,2,31,1,0])
    # new = selection_sort([6,2,31,1,0])
    # new = selection_sort_2([6,2,31,1,0])
    # new = insertion_sort([6,2,31,1,0])
    new = insertion_sort_2([6,2,31,1,0])
    print(new)