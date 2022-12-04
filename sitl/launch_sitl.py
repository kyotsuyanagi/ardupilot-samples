from subprocess import Popen
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
        sitl_home_longitude = sitl_home_longitude + 0.001000
    else:
        sitl_home_longitude = sitl_home_longitude + 0.000200

    sitl_boot_list = ['sim_vehicle.py','--vehicle=ArduCopter','--frame=quad',
                    '--custom-location=%s,%s,%s,%s' % (str(sitl_home_latitude),str(sitl_home_longitude),sitl_home_altitude,sitl_home_direction),
                    '--instance=%s'%(i)]

    print("# sitl command:{0}".format(sitl_boot_list))
    p = Popen(sitl_boot_list)
    time.sleep(5)

