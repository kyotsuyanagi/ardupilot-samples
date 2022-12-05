from dronekit import connect, VehicleMode, LocationGlobalRelative
import time

print( "Lauching drones" )

total_instance = 4
target_latitude = 35.879143
target_longitude = 140.339577 - 0.001800
home_latitude = 35.879143
home_longitude = 140.339577 + 0.001400

def set_attitude(vehicle,aTargetAltitude):

    print("Basic pre-arm checks")
    vehicle.mode = VehicleMode("GUIDED")
    while not vehicle.is_armable:
        print(" Waiting for vehicle to initialise...")
        time.sleep(1)

    print("Arming motors")
    vehicle.armed = True
    
    while not vehicle.armed:
        print(" Waiting for arming...")
        time.sleep(1)

    print("Taking off!")
    vehicle.simple_takeoff(aTargetAltitude)  # Take off to target altitude


    while True:
        print(" Altitude: ", vehicle.location.global_relative_frame.alt)

        if vehicle.location.global_relative_frame.alt >= aTargetAltitude * 0.95:
            print("Reached target altitude")
            break
        time.sleep(5)

def go_target_point(vehicle):

    print("Set default/target airspeed to 3")
    vehicle.airspeed = 3

    while True:
        print("Going towards target point")
        point1 = LocationGlobalRelative(target_latitude, target_longitude, 10)
        vehicle.simple_goto(point1)
        time.sleep(120)
        print("Going towards home location")
        point2 = LocationGlobalRelative(home_latitude,home_longitude, 10)
        vehicle.simple_goto(point2)
        time.sleep(120)

connection_instance = []
for i in range(total_instance):
    connection_string = 'udp:localhost:' + str(15762 + int(i) * 10 )
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