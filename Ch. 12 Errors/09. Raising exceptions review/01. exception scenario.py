# In the code sample, what will happen?
try:
    raise Exception('zero division')
except ZeroDivisionError as e:
    print("zero")

# Traceback (most recent call last):
#   File "c:\Users\mstamenov\GitHub\boot.dev\main.py", line 2, in <module>
#     raise Exception('zero division')
# Exception: zero division