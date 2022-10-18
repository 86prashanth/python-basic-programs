import os
path='abc.txt'
if os.path.isdir(path):
    print("\nit is a directory")
elif os.path.isfile(path):
    print("\n it is a normal file")
else:
    print("It is a special file (socket,fifo,device file")
print()
