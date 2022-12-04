from subprocess import Popen
from signal import signal, SIGINT
from dronekit import connect, VehicleMode, LocationGlobalRelative
import time

print( "Lauching drones" )

total_instance = 4

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


connection_instance = []
for i in range(total_instance):
    connection_string = 'tcp:localhost:' + str(5763 + int(i) * 10 )
    print( "FC: %s" % (connection_string) )
    connection_instance.append(connect(connection_string, wait_ready=True))

##set attitude
for c in connection_instance:
    set_attitude(c,10)
    
##4th drone go target point
go_target_point(connection_instance[3])

for i,c in enumerate(connection_instance):
    print("Closing instance {0}".format(i) )
    c.close()

print("located successfully")