from subprocess import Popen
from signal import signal, SIGINT
from dronekit import connect
import time


print( "Starting SITL by process" )

# example: 'dronekit-sitl copter --home=35.079624,136.905453,50.0,3.0 --instance 0'
sitl_frame          = 'copter'          # rover, plane, copterなどのビークルタイプ
sitl_home_latitude  = 35.879143       # 緯度(度)
sitl_home_longitude = 140.339577      # 経度(度)
sitl_home_altitude  = '20.0'             # 高度(m)
sitl_home_direction = '0.0'             # 機首方位(度)
sitl_instance_num   = 0                 # 0〜


total_instance = 4
connection_instance = []
processes = []

for i in range(total_instance):
    if i==total_instance-1:
        sitl_home_longitude = sitl_home_longitude + 0.001000
    else:
        sitl_home_longitude = sitl_home_longitude + 0.000200

    sitl_boot_list = ['dronekit-sitl',sitl_frame,
                    '--home=%s,%s,%s,%s' % (str(sitl_home_latitude),str(sitl_home_longitude),sitl_home_altitude,sitl_home_direction),
                    '--instance=%s'%(i)]

    print("# sitl command:{0}".format(sitl_boot_list))
    p = Popen(sitl_boot_list)
    processes.append(p)
    time.sleep(1)

    '''
    connection_string = 'tcp:localhost:' + str(5760 + int(i) * 10 )
    print( "FC: %s" % (connection_string) )
    connection_instance.append(connect(connection_string, wait_ready=True))
    '''

try:

    while True:
        print("Looping")
        time.sleep(1)

        '''
        for i,c in enumerate(connection_instance):
            print("Instance-"+str(i))
            print("Mode:{0}".format(c.mode.name ))
            time.sleep(1)
        '''

except( KeyboardInterrupt, SystemExit):
    print( "SIGINT Detected" )

'''
for i,c in enumerate(connection_instance):
    print("Closing instance {0}".format(i) )
    c.close()
'''

for p in processes:
    p.send_signal(SIGINT)
    p.communicate()
    time.sleep(1)

print("All shutdown")