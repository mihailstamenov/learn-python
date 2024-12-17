# Creation

# key: value aka literal
{'jack': 4098, 'sjoerd': 4127} #{'jack': 4098, 'sjoerd': 4127}

{4098: 'jack', 4127: 'sjoerd'} #{4098: 'jack', 4127: 'sjoerd'}


# comprehension
{x: x ** 2 for x in range(10)} #{0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}
{x: x**2 for x in (2, 4, 6)} #{2: 4, 4: 16, 6: 36}


# type constructor
dict() #{}

dict([('foo', 100), ('bar', 200)]) #{'foo': 100, 'bar': 200}

dict([('foo', 100), ('bar', 200), ('foo', 90)]) #{'foo': 90, 'bar': 200}

dict = dict(foo=100, bar=200) #{'foo': 100, 'bar': 200}

dict(foo=100, bar=200, foo=90) #SyntaxError: keyword argument repeated: foo


#create a list of all the keys in order of insertion
list(dict) #['foo', 'bar']


# Check for existence
'foo' in dict #True

'bar' not in dict #False


# Assign a new value to a key or create an unexisting key with a value
dict['bar'] = 1

# Access
dict['bar']