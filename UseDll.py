from ctypes import *
user32 = windll.LoadLibrary("user32.dll")
caption = c_char_p("hello")
text = c_char_p("by biopunk")
user32.MessageBoxA(0,text,caption,0)
