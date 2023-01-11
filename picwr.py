import ctypes
import time

list = b""
png = open('a.png','ab+')
print(len(list))
png.write(list)
png.close()
print('写入完成')
