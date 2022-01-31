
import os
import time

def loopy():
   print(f"PID={os.getpid()}")
   while True:
      print(os.environ.get("PUDB_TTY", "NADA"))
      time.sleep(1)

loopy() 