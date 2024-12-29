
def fibonacci_loop(n):
    result = 0
    prev_1 = 1
    prev_2 = 0

    if n == 0:
        return 0
    for i in range(n):
        prev_2 = prev_1
        prev_1 = result
        result = prev_1 + prev_2
    return result


def fibonacci_recur(n):
    if n <= 1:
        return n
    else:
        return fibonacci_recur(n-1) + fibonacci_recur(n-2)
    


if __name__ == "__main__":
    x = fibonacci_loop(7)
    y = fibonacci_recur(7)
    print(x)
    print(y)