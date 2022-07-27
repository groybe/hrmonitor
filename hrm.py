# -*- coding:UTF-8 -*-

#Linux環境でのみ動作します
#Only works in Linux environment
#動作確認端末:POLAR Verity Sense
#Confirmed working with:POLAR Verity Sense

from bluepy import btle
import time
import sys
import datetime

# Mac Adress of heart rate device.
hrm = "a0:9e:1a:b2:15:7e"
target = "120"

params = ""

try:
    while True:

        class MyDelegate(btle.DefaultDelegate):

            def __init__(self,params):
                print(params)

                btle.DefaultDelegate.__init__(self)

            def handleNotification(self, cHandle, data):
                #print(cHandle)
                #print(data)

                heartrate = int.from_bytes(data, byteorder='big')
                print(chr(27) + "[2J") # clear screen using escape sequences
                print(chr(27) + "[H")  # return to home using escape sequences
                print("Heart Rate:", heartrate,"   Target:",target)

        p = btle.Peripheral(hrm)
        p.withDelegate(MyDelegate(params))

        handle = 40
        p.writeCharacteristic(handle+1, b'\x01\x00', True)

        TIMEOUT = 1.0
        while True:
            if p.waitForNotifications(TIMEOUT):
                continue
            print('wait...')

except KeyboardInterrupt:
    print('initialize')

    p.writeCharacteristic(handle+1, b'\x00\x00', True)
    p.disconnect()

    sys.exit()
