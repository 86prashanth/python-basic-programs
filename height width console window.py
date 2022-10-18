import fcntl,termios,struct
def terminal_size():
    th,tw,hp,wp=struct.unpack('HHHH',fcntl.ioctl(0,termios,TIOCGWINSZ,struct.pack('HHHH,0,0,0,0')))
    return tw,th
print('number of columns and rows',terminal_size())