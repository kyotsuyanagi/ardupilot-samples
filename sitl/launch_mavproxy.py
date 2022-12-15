from subprocess import Popen
import time

print( "Starting mavproxy by process" )

   
mavproxy = ['mavproxy.py','--master','tcp:127.0.0.1:5762','--out','127.0.0.1:14762','--out','127.0.0.1:15762']
print("#command:{0}".format(mavproxy))
p = Popen(mavproxy)
time.sleep(5)

mavproxy = ['mavproxy.py','--master','tcp:127.0.0.1:5772','--out','127.0.0.1:14772','--out','127.0.0.1:15772']
print("#command:{0}".format(mavproxy))
p = Popen(mavproxy)
time.sleep(5)

mavproxy = ['mavproxy.py','--master','tcp:127.0.0.1:5782','--out','127.0.0.1:14782','--out','127.0.0.1:15782']
print("#command:{0}".format(mavproxy))
p = Popen(mavproxy)
time.sleep(5)

mavproxy = ['mavproxy.py','--master','tcp:127.0.0.1:5792','--out','127.0.0.1:14792','--out','127.0.0.1:15792']
print("#command:{0}".format(mavproxy))
p = Popen(mavproxy)
time.sleep(5)

