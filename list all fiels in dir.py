from os import listdir
from os.path import isfile,join
files_list=[f for f in listdir('/python/')if isfile(join('/python/'.f))]
print(files_list)