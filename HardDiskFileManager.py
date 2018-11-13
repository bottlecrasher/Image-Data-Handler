import subprocess
import time
import argparse
import signal

"""
Hard-disk waiter on Heavy File manipulation.
If your 
"""

parser = argparse.ArgumentParser(description='File movement helper')
parser.add_argument('--subprocess', default = "test_process.py",type=str, metavar='Subprocess', help='Subprocess python code you want to execute')
parser.add_argument("--process", type=float, default = 1, metavar="TIME", help="The minutes that process will run before halt")
parser.add_argument("--wait", type=float, default = 1, metavar="TIME", help="The seconds that process will run before halt")
args = parser.parse_args()

Total_time = time.time()
process_time = time.time()
#sub = subprocess.call(["python", args.subprocess])
sub = subprocess.Popen(["python", args.subprocess])
print("subprocess object successfully worked!")

while True:
    if (time.time() - process_time) > args.process:
        print("# Pause {} seconds to down HDD heat".format(args.wait))
        sub.send_signal(signal.SIGSTOP)
        time.sleep(args.wait)
        process_time = time.time()
        sub.send_signal(signal.SIGCONT)
        if sub.poll() != None:
            sub.terminate()
            Total_time = time.time() - Total_time
            print("# All of the process is end. Total Processing Time : {} seconds".format(Total_time))
            break

