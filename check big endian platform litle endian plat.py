import sys
print()
if sys.byteorder=='little':
    print("Littel-endian platform")
else:
    print("big-endian platform")