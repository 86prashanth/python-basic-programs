import os.path,time
print("last modified.%s" %time.ctime(os.path.getmtime("get size of file.py")))
print("created: %s" % time.ctime(os.path.getctime("histogram.py")))