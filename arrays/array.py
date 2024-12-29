
def lowest_el(arr:list):
    result = arr[0]
    for el in arr:
        if el < result:
            result = el
    return result


if __name__ == "__main__":
    arr = [6,4,6,8,4,2,3,45,6]
    print(lowest_el(arr))