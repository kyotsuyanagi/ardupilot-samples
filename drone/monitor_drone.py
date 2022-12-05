from dronekit import connect, VehicleMode, LocationGlobalRelative
import time
import math

print( "Monitoring drones" )

total_instance = 4

def get_distance_metres(aLocation1, aLocation2):
    dlat = aLocation2.lat - aLocation1.lat
    dlong = aLocation2.lon - aLocation1.lon
    return math.sqrt((dlat*dlat) + (dlong*dlong)) * 1.113195e5

connection_instance = []
for i in range(total_instance):
    connection_string = 'tcp:localhost:' + str(5764 + int(i) * 10 )
    print( "FC: %s" % (connection_string) )
    connection_instance.append(connect(connection_string, wait_ready=True))

@connection_instance[3].on_attribute('location.global_frame')
def listener(self, attr_name, value):
    print("Global: {0}".format(value))
    for i,c in enumerate(connection_instance):
        if i in [0,1,2]:
            location = c[i].location.global_frame
            target_location = value
            metres = get_distance_metres(location,target_location)
            if metres > 7:
                print("Instance:{0} - distance:{1}".format(i,metres))