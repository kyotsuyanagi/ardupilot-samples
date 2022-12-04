from subprocess import Popen
from signal import signal, SIGINT
from dronekit import connect, VehicleMode, LocationGlobalRelative
import time

print( "Starting SITL by process" )

# example: 'dronekit-sitl copter --home=35.079624,136.905453,50.0,3.0 --instance 0'
sitl_frame          = 'copter'
sitl_home_latitude  = 35.879143
sitl_home_longitude = 140.339577
sitl_home_altitude  = '20.0'
sitl_home_direction = '0.0'
sitl_instance_num   = 0

target_latitude = 35.879143
target_longitude = 140.339577 - 0.001800

total_instance = 4
connection_instance = []
processes = []

def set_attitude(vehicle,aTargetAltitude):

    """
    Arms vehicle and fly to aTargetAltitude.
    """

    print("Basic pre-arm checks")
    # Don't try to arm until autopilot is ready
    while not vehicle.is_armable:
        print(" Waiting for vehicle to initialise...")
        time.sleep(1)

    print("Arming motors")
    vehicle.armed = True
    
    # Confirm vehicle armed before attempting to take off
    while not vehicle.armed:
        print(" Waiting for arming...")
        time.sleep(1)

    # Copter should arm in GUIDED mode
    vehicle.mode = VehicleMode("GUIDED")

    print("Taking off!")
    vehicle.simple_takeoff(aTargetAltitude)  # Take off to target altitude

    # Wait until the vehicle reaches a safe height before processing the goto
    #  (otherwise the command after Vehicle.simple_takeoff will execute
    #   immediately).
    while True:
        print(" Altitude: ", vehicle.location.global_relative_frame.alt)
        # Break and return from function just below target altitude.
        if vehicle.location.global_relative_frame.alt >= aTargetAltitude * 0.95:
            print("Reached target altitude")
            break
        time.sleep(5)

def go_target_point(vehicle):
    print("Set default/target airspeed to 3")
    vehicle.airspeed = 3

    print("Going towards first point for 30 seconds ...")
    point1 = LocationGlobalRelative(target_latitude, target_longitude, 20)
    vehicle.simple_goto(point1)


for i in range(total_instance):
    if i==total_instance-1:
        sitl_home_longitude = sitl_home_longitude + 0.001000
    else:
        sitl_home_longitude = sitl_home_longitude + 0.000200

    '''
    sitl_boot_list = ['dronekit-sitl',sitl_frame,
                    '--home=%s,%s,%s,%s' % (str(sitl_home_latitude),str(sitl_home_longitude),sitl_home_altitude,sitl_home_direction),
                    '--instance=%s'%(i)]
    '''
    
    sitl_boot_list = ['sim_vehicle.py','--vehicle=ArduCopter','--frame=quad',
                    '--custom-location=%s,%s,%s,%s' % (str(sitl_home_latitude),str(sitl_home_longitude),sitl_home_altitude,sitl_home_direction),
                    '--instance=%s'%(i)]

    print("# sitl command:{0}".format(sitl_boot_list))
    p = Popen(sitl_boot_list)
    #processes.append(p)
    time.sleep(5)

'''
    connection_string = 'tcp:localhost:' + str(5760 + int(i) * 10 )
    print( "FC: %s" % (connection_string) )
    connection_instance.append(connect(connection_string, wait_ready=True))

##set attitude
for c in connection_instance:
    set_attitude(c,10)
    
##4th drone go target point
go_target_point(connection_instance[3])


try:

    while True:
        print("Looping")
        time.sleep(1)

        for i,c in enumerate(connection_instance):
            print("Instance-"+str(i))
            print("Mode:{0}".format(c.mode.name ))
            time.sleep(1)

except( KeyboardInterrupt, SystemExit):
    print( "SIGINT Detected" )


for i,c in enumerate(connection_instance):
    print("Closing instance {0}".format(i) )
    c.close()


for p in processes:
    p.send_signal(SIGINT)
    p.communicate()
    time.sleep(1)

print("All shutdown")
'''