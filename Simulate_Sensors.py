#!/usr/bin/env python
# coding: utf-8

# In[16]:


import uuid 
import random
import json

from azure.iot.device import IoTHubDeviceClient, Message
import threading

random.seed(42)

def check_uid_exists(uid, device_id):
    if uid in device_id:
        return True
    else:
        return False

def generate_device_ids(num_devices=4):
    device_id=[]
    while len(device_id)<num_devices:
        uid=random.randint(1000,9999)
        if check_uid_exists(uid,device_id): 
            continue
        else:
            device_id.append(uid)
    return device_id


# In[6]:


devices = generate_device_ids(4)

# In[7]:


def generate_temperature_humidity(min_temp=25, max_temp = 30, min_humidity =80, max_humidity=85):
    mean_temp=random.uniform(min_temp, max_temp)
    temp = round(random.normalvariate(mean_temp, 2),1)
    mean_humidity = random.uniform(min_humidity, max_humidity)
    humidity = round(random.normalvariate(mean_humidity, 4),1)
    return temp,humidity


# In[8]:


def generate_gps_location(gps, alpha=0.01):
    direction = gps['direction']
    if direction=='W-E':
        slope = (gps['final']['long']-gps['initial']['long'])/(gps['final']['lat']-gps['initial']['lat'])
        lat_new = gps['current']['lat']-alpha
        long_new = gps['initial']['long']+slope*(lat_new-gps['initial']['lat'])
    else:
        slope = (gps['final']['long']-gps['initial']['long'])/(gps['final']['lat']-gps['initial']['lat'])
        lat_new = gps['current']['lat']+alpha
        long_new = gps['initial']['long']+slope*(lat_new-gps['initial']['lat'])
    
    if abs(lat_new-gps['final']['lat'])<0.01:
        gps['current']['lat'] = gps['initial']['lat']
        gps['current']['long']= gps['current']['long']
    else:
        gps['current']['lat']=lat_new
        gps['current']['long']=long_new
    return gps


# In[9]:


# From west to east

gps_1 ={'device': devices[0],
    'initial':{
        'lat':-33.816559,
        'long': 152.111733
    },
    'final':{
        'lat':-36.983220,
        'long':174.133296
    },
    'current':{
        'lat':-33.816559,
        'long': 152.111733
    },
    'direction':'W-E'
    
}

# From west to east

gps_2 ={
    'device':devices[1],
    'initial':{
        'lat':-33.816559,
        'long': 152.111733
    },
    'final':{
        'lat':-44.447275,
        'long':167.609779
    },
    'current':{
        'lat':-33.816559,
        'long': 152.111733
    },
    'direction':'W-E'
    
}


# From east to west

gps_3 ={
    'device':devices[2],
    'initial':{
        'lat':-32.239542,
        'long': 113.938671
    },
    'final':{
        'lat':6.538896,
        'long':81.915375
    },
    'current':{
        'lat':-32.239542,
        'long': 113.938671
    },
    'direction':'E-W'
    
}

# From east to west


gps_4 ={
    'device':devices[3],
    'initial':{
        'lat':-32.239542,
        'long': 113.938671
    },
    'final':{
        'lat':-7.768057,
        'long':106.306864
    },
    'current':{
        'lat':-32.239542,
        'long': 113.938671
    },
    'direction':'E-W'
    
}


# In[10]:




CONNECTION_STRING = 'HostName=Food-Supply-Chain.azure-devices.net;DeviceId=myRaspberryPi;SharedAccessKey=PZeS9YfawPmtEDzGXbH8CEHz64z8XYqvw2nPFGD7FSY='
def iothub_client_init():
    # Create an IoT Hub client
    client = IoTHubDeviceClient.create_from_connection_string(CONNECTION_STRING)
    return client

client = iothub_client_init()

TEMPERATURE = 200.0
HUMIDITY = 600

#MSG_TXT = '{{temperature": {temperature},"humidity": {humidity}, "initlat":{initlat}, "initlong":{initlong}, "finallat":{finallat}, "finallong":{finallong}, "currentlat":{currentlat}, "currentlong":{currentlong}}}'

#MSG_TXT = '{{"deviceID": {deviceID},"temperature": {temperature},"humidity": {humidity},"init_lat": {init_lat},"init_long": {init_long},"final_lat": {final_lat},"final_long": {final_long},"current_lat": {current_lat},"current_long": {current_long}}}'

MSG_TXT = '{{"hashid": {hashid},"temperature": {temperature},"humidity": {humidity}, "initlat":{initlat}, "initlong":{initlong}, "finallat":{finallat}, "finallong":{finallong}, "currentlat":{currentlat}, "currentlong":{currentlong}}}'





def send_data(device, temp, humidity, gps, client):
    #msg_txt_formatted = MSG_TXT.format(deviceID=device,temperature=temp, humidity=humidity, init_lat=gps['initial']['lat'], init_long=gps['initial']['long'], final_lat=gps['final']['lat'], final_long=gps['final']['long'], current_lat=gps['current']['lat'], current_long=gps['current']['long'])
    
    #msg_txt_formatted = MSG_TXT.format(temperature=temp, humidity=humidity, initlat=gps['initial']['lat'], initlong=gps['initial']['long'], finallat=gps['final']['lat'], finallong=gps['final']['long'], currentlat=gps['current']['lat'], currentlong=gps['current']['long'])

    msg_txt_formatted = MSG_TXT.format(hashid=device,temperature=temp, humidity=humidity, initlat=gps['initial']['lat'], initlong=gps['initial']['long'],finallat=gps['final']['lat'], finallong=gps['final']['long'], currentlat=gps['current']['lat'], currentlong=gps['current']['long'])

    message = Message(msg_txt_formatted)

    print( "Sending message: {}".format(message) )

    

    sample = {"deviceID": device,"temperature": temp,"humidity": humidity, "init_lat": gps['initial']['lat'], "init_long":gps['initial']['long'], "final_lat": gps['final']['lat'],"final_long":gps['final']['long'], "current_lat":gps['current']['lat'], "current_long": gps['current']['long']}

    
    #client.send_message(json.dumps(sample, ensure_ascii=False).encode('utf8'))
    client.send_message(message)
    print ( "Message successfully sent" )
    


# In[ ]:





# In[12]:


def generate_send_data(device_id,gps_1, gps_2, gps_3, gps_4):

    for index,device in enumerate(device_id):
        if index==0:
            temp, humidity = generate_temperature_humidity()
            gps_1 = generate_gps_location(gps_1)
            gps= gps_1
        elif index==2:
            temp,humidity = generate_temperature_humidity(10,15, 70,75)
            gps_2 = generate_gps_location(gps_2)
            gps=gps_2
        elif index==3:
            temp,humidity = generate_temperature_humidity(30,35,85,90)
            gps_3 = generate_gps_location(gps_3)
            gps = gps_3
        else:
            temp,humidity = generate_temperature_humidity(30,35,85,90)
            gps_4 = generate_gps_location(gps_4)
            gps=gps_4
        send_data(device, temp, humidity, gps, client)


# In[17]:



def broadcast_data():
    t = threading.Timer(5.0, broadcast_data).start()
    generate_send_data(devices, gps_1, gps_2, gps_3, gps_4)

broadcast_data()
#send_data(devices[0], 600, 47, gps_1, client)


# In[ ]:




