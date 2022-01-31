from hypno import inject_py
import os
import sys
import signal
import time

DEBUGGER_CONNECTED_SIGNAL = signal.SIGUSR1

def inject_pudb_set_trace(pid, debugger="pudb", pause=True):
    assert(isinstance(pid, int))
    assert(pid>0)
    tty = os.ttyname(1)
    print(f"TTY={tty}")
    inject_py(pid, f'__import__("os").environ["PUDB_TTY"]="{tty}"')
    sig_num = DEBUGGER_CONNECTED_SIGNAL.value
    inject_py(pid, f'__import__("signal").signal({sig_num},lambda _,f:__import__("{debugger}").set_trace(f))')
    os.kill(pid, sig_num)

if __name__=="__main__":
     import sys
     if len(sys.argv)!=2:
        print("Expecting pid to attach to as argument")
        sys.exit(1)
     inject_pudb_set_trace(int(sys.argv[1]))
     while True:
        time.sleep(1.0)
