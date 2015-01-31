#-*-coding:cp936-*-
from ctypes import *
from debug_define import*

kernel32 = windll.LoadLibrary('kernel32.dll')

user32   = windll.LoadLibrary('user32.dll')

class my_debug():
    def _init_(self):
        self.h_process       = None
        self.pid             = None
        self.debugger_active = False

    def load(self,path_to_exe):
        creation_flags = DEBUG_PROCESS

        startupinfo         = STARTUPINFO()
        process_information = PROCESS_INFORMATION()

        startupinfo.dwFlags     = 0x1
        stsrtupinfo.wShowWindwo = 0x0

        startupinfo.cb = sizeof(startupinfo)

        if kernel32.CreateProcessA(path_to_exe,
                                   None,
                                   None,
                                   None,
                                   False,
                                   creation_flags,
                                   None,
                                   None,
                                   byref(startupinfo),
                                   byref(process_information)):
            print "线程成功加载,PID:%d"%process_information.dwProcessId
            self.h_process = self.open_process(process_information.dwProcessId)
        else:
            print "线程加载失败,错误代码:0x%08x"%kernel32.GetLastError()

    def open_process(self,pid):
        h_process = kernel32.OpenProcess(PROCESS_ALL_ACCESS,False,pid)
        return h_process

    def attach(self,pid):
        self.h_process = self.open_process(pid)

        if kernel32.DebugActiveProcess(pid):
            self.debugger_active = True
            self.pid = int(pid)
            self.run()
        else:
            print "无法连接进程！"
    def run(self):
        while self.debugger_active == True:
            self.get_debug_event()

    def get_debug_event(self):

        debug_event = DEBUG_EVENT()
        continue_startus = DBG_CONTINUE

        if kernel32.WaitForDebugEvent(byret(debug_evevnt),INFINITE):
            raw_input("按下任意键以继续...")
            self.debugger_active = False
            kernel32.ContinueDebugEvent(debug_event.dwProcessId,
                                        debug_event.dwThreadId,
                                        continue_ststus)

    def detach(self):

        if kernel32.DebugActiveProcessStop(self.pid):
            print '结束调试，退出中...'
            return True
        else:
            print '出错！'
            return False
