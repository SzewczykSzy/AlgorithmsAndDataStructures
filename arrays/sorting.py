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


def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i+1

def quick_sort(arr, low=0, high=None):
    if high is None:
        high = len(arr) - 1
    if low < high:
        pivot_idx = partition(arr, low, high)
        quick_sort(arr, low, pivot_idx-1)
        quick_sort(arr, pivot_idx+1, high)


def counting_sort(arr):
    counter = [0 for i in range(max(arr)+1)]
    for el in arr:
        counter[el] += 1
    result = []
    for idx, el in enumerate(counter[:]):
        if el > 0:
            result.extend([idx]*el)
    return result


def radix_sort(arr):
    radix_arr = [[], [], [], [], [], [], [], [], [], []]
    for i in range(len(str(arr[0]))):
        for j in range(len(arr)):
            idx = int(str(arr[j])[-i-1])
            radix_arr[idx].append(arr[j])
        arr = []
        for el in radix_arr:
            for val in el:
                arr.append(val)
        radix_arr = [[], [], [], [], [], [], [], [], [], []]
    return arr


if __name__ == "__main__":
    # arr = [6,2,31,1,0]
    arr = [33, 45, 40, 25, 17, 24]
    # new = bubble_sort([6,2,31,1,0])
    # new = selection_sort([6,2,31,1,0])
    # new = selection_sort_2([6,2,31,1,0])
    # new = insertion_sort([6,2,31,1,0])
    # new = insertion_sort_2([6,2,31,1,0])
    # quick_sort(arr)
    # new = counting_sort(arr)
    new = radix_sort(arr)
    print(new)