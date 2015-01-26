from ctypes import *

UINT      = c_uint
WNDPROC   = c_void_p
INT       = c_int
HINSTANCE = c_void_p
HINCON    = c_void_p
LPCTSTR   = POINTER(c_char)



class WNDCLASSEX(Structure):
    _fileds_=[
        ('cbSize',        UINT),
        ('style',         UINT),
        ('cbClsExtra',    INT),
        ('cbWndExtra',    INT),
        ('hInstance',     HINSTANCE),
        ('hIcon',         HINSTANCE),
        ('hCursor',       HINSTANCE),
        ('hbrBackground', HINSTANCE),
        ('lpszMenuName',  LPCTSTR),
        ('lpszClassName', LPCTSTR),
        ('hIconSm',       HINSTANCE),
        ]
        
