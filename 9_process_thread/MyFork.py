import os
print( "Process %s start" % os.getpid())
pid=os.fork()
if pid==0:
    print("I am a child process %s and my parent is %s" % (os.getpid(),os.getppid()))
else:
    print("I %s just created a child process %s" %(os.getpid(), pid))
    

''' output
Process 60 start
I 60 just created a child process 61 # returned from the parent process
I am a child process 61 and my parent is 60 # returned from the child process
''' and None
