import glob
import os
files=glob.glob("*.py")
files.sort(key=os.path.getatime)
print("\n".join(files))