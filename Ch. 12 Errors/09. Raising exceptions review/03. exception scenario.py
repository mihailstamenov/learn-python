# In the code sample, what will happen?
try:
    raise Exception('zero division')
except ZeroDivisionError as e:
    print("zero")
except Exception as e:
    print("other")

# other    