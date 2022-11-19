import wiotp.sdk.device
import time
# Provide your IBM Watson Device Credentials
myConfig = {   "identity": {     "orgId": "ie9ki3",
                                     "typeId": "mydevice",
                                     "deviceId":"mydeviceid"},
                "auth": {     "token": "bW(_2O((aRG8E6fij6"}}

def myCommandCallback(cmd):
    print("Message received from IBM IoT Platform: %s" % cmd.data['command'])
    m = cmd.data['command']
client = wiotp.sdk.device.DeviceClient(config=myConfig, logHandlers=None)
client.connect()

def pub(data):
    client.publishEvent(eventId="status", msgFormat="json", data=myData, qos=0, onPublish=None)
    print("Published data Successfully: %s", myData)

while True:

    ######____TRAIN ROUTE FROM_____MUMBAI ----> CHENNAI____######

    myData = {'name': 'BALA', 'PASSWORD': 12234}
    pub(myData)
    time.sleep(3)
    myData = {'name': 'aravind', 'PASSWORD': 12234}
    pub(myData)
    time.sleep(3)
    myData = {'name': 'sanjay', 'PASSWORD': 12234}
    pub(myData)
    time.sleep(3)
    break
client.disconnect()