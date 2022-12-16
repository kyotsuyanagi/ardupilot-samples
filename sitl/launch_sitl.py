import subprocess
import time

print( "Starting SITL by process" )

sitl_frame          = 'copter'
sitl_home_latitude  = 35.879143
sitl_home_longitude = 140.339577
sitl_home_altitude  = '0.0'
sitl_home_direction = '0.0'

target_latitude = 35.879143
target_longitude = 140.339577 - 0.001800

total_instance = 4
connection_instance = []
processes = []

for i in range(total_instance):
    if i==total_instance-1:
        sitl_home_longitude = sitl_home_longitude + 0.001100
    else:
        sitl_home_longitude = sitl_home_longitude + 0.000100

    sitl_boot_list = [
        'sim_vehicle.py',
        '--vehicle=ArduCopter',
        #'--frame={0}'.format(sitl_frame),
        '--custom-location=%s,%s,%s,%s' % (str(sitl_home_latitude),str(sitl_home_longitude),sitl_home_altitude,sitl_home_direction),
        '--instance=%s'%(i)
    ]
    print("# sitl command:{0}".format(sitl_boot_list))
    subprocess.Popen(sitl_boot_list)
    time.sleep(15)

    master_port = str(5762 + int(i) * 10 )
    out_port1 = str(14762 + int(i) * 10 )
    out_port2 = str(15762 + int(i) * 10 )
    mavproxy = [
        'mavproxy.py',
        '--master','tcp:127.0.0.1:{0}'.format(master_port),
        '--out','127.0.0.1:{0}'.format(out_port1),
        '--out','127.0.0.1:{0}'.format(out_port2)
    ]
    print("# mavproxy command:{0}".format(mavproxy))
    subprocess.Popen(mavproxy)
    time.sleep(3)

