import tinytuya
import time
import os

## Get environ vars
device_id = os.getenv('DEVICE_ID')
device_ip = os.getenv('DEVICE_IP')
device_local_key = os.getenv('DEVICE_LOCAL_KEY')

## Connect and configure bulb
d = tinytuya.BulbDevice(device_id, device_ip, device_local_key)
d.set_version(3.3)
STATUS = d.status()
# print('Status', STATUS)

## Do cool shit
d.set_colour(255,0,0) 
time.sleep(5) 
d.set_mode(mode='white')

# d.turn_off()
# time.sleep(5)
# d.turn_on()
