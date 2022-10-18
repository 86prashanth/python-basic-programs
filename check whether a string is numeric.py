str='a124'
try:
    i=float(str)
except(ValueError,TypeError):
    print('\nNot numeric')
print()