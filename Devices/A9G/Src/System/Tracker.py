import gps
import machine
import time
import math
import uos
import ujson as json
import cellular
import uzlib

 

led = machine. Pin(27, machine.Pin.OUT, 0)
value =1
test=0

log_path = "/t/log.json"
# Path to your systemdata JSON file
systemdata_path = "/t/systemdata.json"




def start():
    print("Starting Program")
    gpsconfig(1)
    #time.sleep(300)
    # Read JSON file
    with open(systemdata_path, 'r') as file:
        systemdata = file.read()
        data = json.loads(systemdata)

    is_active = data["isactive"]
    live_tracking = data["livetracking"]
    custom_locations = data["customlocations"]
#   print("is_active:", is_active)
#   print("live_tracking:", live_tracking)
    
    
    if is_active == 1:
        print("gps active")
        #time.sleep(5)
        
        if live_tracking == 1:
            ping(1)
            
        else:
            away(custom_locations)
        
    else:
        log("Start","Not_Active")
        

    
    

    
def setup():
    print("System Setup")
    
    
def ping(mode):
    print("System Pinging")
    
    if mode == 0:
        print("Ping Mode Defualt")
    
    elif mode == 1:
        print("Ping Mode LiveTracking")
    
    
    
    
    
    
    
    
    
def away(custom_locations):
    print("System is in Awaymode")
    cur_latitude, cur_longitude = gps.get_location()
    print("Latitude",cur_latitude,"Longitude",cur_longitude)
    isincustomlocation = 0
    
    # Iterate through custom locations and extract coordinates
    for location_name, location_data in custom_locations.items():
        x = location_data["x"]
        y = location_data["y"]
        r = location_data["r"]
        if on_location_changed(location_name, x,  y, cur_latitude, cur_longitude, r) == 1:
            isincustomlocation= isincustomlocation+1
            print(isincustomlocation)
    if isincustomlocation < 1:
        print("is not in  range of custom locations")
        ping(0)
    else:
        print("is in range of custom locations")
        log("Away","Normal")
        
             
     
        



def format_time(local_time):
    return "{:04d}-{:02d}-{:02d} {:02d}:{:02d}:{:02d}".format(
        local_time[0], local_time[1], local_time[2], local_time[3], local_time[4], local_time[5])


def log(what, Type):
    currentlocation = gps.get_location()
    From = what
    level = Type
    local_time_str = "N/A"
    charge = machine.get_input_voltage()
    
    try:
        local_time = time.localtime(gps.time())
    except OverflowError:
        print("OverflowError occurred while getting time.")
        print("Local Time:", local_time_str)
    else:
        local_time_str = format_time(local_time)
        print("Local Time:", local_time_str)
        
    logger = {
        "Time"                  :    local_time_str,
        "From"                  :    From,
        "Level"                 :    level,
        "Current Location"      :    currentlocation,
        "Charge"				:    charge,
    }    
    
    # Append the new log entry to the file
    json_filename = "/t/logger.json"  # Adjust the path accordingly

    # Write the updated log entry to the JSON file
    with open(json_filename, "a") as file:
        json.dump(logger, file)
        file.write('\n')  # Add a newline after each entry
    
#     print("System logging")    
#     print("From:", From)
#     print("Level:", level)
#     print("Current Location:", currentlocation)
    
    
    
## Config for the gps
def gpsconfig(val):
    
    
    if val == 1:
        gps.on()
        print("Gps on")
    else:
        gps.off()
        print("Gps off")
        
        
def end():
    print("System Ending")







