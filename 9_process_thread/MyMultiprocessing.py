from multiprocessing import Process
import os

def run_proc(name):
    print( "run chiled process %s (%s)" %(name, os.getpid()))
    
if __name__=="__main__":
    print("Parent Process %s " % os.getpid())
    p=Process(target=run_proc,args=("test",)) # args "test" is the argument of the function run_proc
    print("Child process will start")
    p.start()
    p.join()
    print("child process ends")