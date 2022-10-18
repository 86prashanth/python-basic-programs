def add_number(a,b):
    if not(isinstance(a,int)and isinstance(b,int)):
        raise TypeError('inputs must be integers')
    return a+b
print(add_number(10,20))