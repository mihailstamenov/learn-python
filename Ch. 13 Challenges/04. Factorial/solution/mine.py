def factorial(num):
    if num == 0:
        return 1
    res = num
    for i in range(num, 1, -1):
        res = res*(i-1)
    return res