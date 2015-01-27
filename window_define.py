
from ctypes import *

UINT      = c_uint
WNDPROC   = c_void_p
INT       = c_int
HANDLE    = c_int
LPCTSTR   = POINTER(c_char)
BOOL      = c_bool
LONG      = c_long
DWORD     = c_ulong


WNDPROC = WINFUNCTYPE(c_long,c_int,c_uint,c_int,c_int )

class WNDCLASSEX(Structure):
    _fileds_=[
        ('cbSize',        UINT),
        ('style',         UINT),
        ('lpfnWndProc',   WNDPROC),
        ('cbClsExtra',    INT),
        ('cbWndExtra',    INT),
        ('hInstance',     HANDLE),
        ('hIcon',         HANDLE),
        ('hCursor',       HANDLE),
        ('hbrBackground', HANDLE),
        ('lpszMenuName',  LPCTSTR),
        ('lpszClassName', LPCTSTR),
        ('hIconSm',       HANDLE),
        ]

class RECT(Structure):
    _fileds_=[
        ("left",          LONG),
        ('top',           LONG),
        ('right',         LONG),
        ('bottom',        LONG),
        ]
    
class PAINTSTRUCT(Structure):
    _fileds_=[
        ('hDc',           HANDLE),
        ('fErase',        BOOL),
        ('rcPaint',       RECT),
        ('fRestore',      BOOL),
        ('fIncUpdate',    BOOL),
        ('rgbReserved[32]',c_char*32)
        ]


class POINT(Structure):
    _fileds_=[
        ('x',             LONG),
        ('y',             LONG),
        ]

class MSG(Structure):
    _fileds_=[
        ('hWnd',         HANDLE),
        ('message',      UINT),
        ('wParam',       INT),
        ('lParam',       INT),
        ('time',         DWORD),
        ('pt',           POINT),
        ]




