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

if __name__ == "__main__":
    new = bubble_sort([6,2,31,1,0])
    print(new)