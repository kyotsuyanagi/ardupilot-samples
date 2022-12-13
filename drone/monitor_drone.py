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
    connection_string = 'tcp:localhost:' + str(5763 + int(i) * 10 )
    print( "FC: %s" % (connection_string) )
    connection_instance.append(connect(connection_string, wait_ready=True))

def location_callback(self, attr_name, value):
    #print("Global: {0}".format(value))
    for i,c in enumerate(connection_instance):
        if i in [0,1,2]:
            location = connection_instance[i].location.global_frame
            target_location = value
            metres = get_distance_metres(location,target_location)
            if metres < 50:
                print("near")
                '''
                mode = "GUIDED"
                print("Instance:{0} - distance:{1}".format(i,metres))
                if connection_instance[i].mode != mode:
                    connection_instance[i].mode = VehicleMode(mode)
                '''
            else:
                print("away")
                '''
                mode = "GUIDED"
                if connection_instance[i].mode != mode:
                    connection_instance[i].mode = VehicleMode(mode)
                '''



connection_instance[3].add_attribute_listener('location.global_frame', location_callback)

while True:
    print("Monitoring")
    time.sleep(1)