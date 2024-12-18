# def number_sum(n):
#     pass



def number_sum(n):
    sum = 0
    for i in range(n+1):
        sum += i
    return sum

# ------------------
# def number_sum(n):
#     for i in range(n):
#         sum += i
#     return sum

# PythonError: Traceback (most recent call last):
#   File "<exec>", line 6, in <module>
#   File "<string>", line 51, in <module>
#   File "<string>", line 35, in main
#   File "<string>", line 22, in test
#   File "/home/pyodide/main.py", line 3, in number_sum
#     sum += i
#     ^^^
# UnboundLocalError: cannot access local variable 'sum' where it is not associated with a value