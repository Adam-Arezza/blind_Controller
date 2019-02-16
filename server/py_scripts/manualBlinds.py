# This script is called by the express server to control the blinds through the 
# NRF24 module

import sys
import json
import RPi.GPIO as GPIO
from lib_nrf24 import NRF24
import spidev

GPIO.setmode(GPIO.BCM)

nodes = [[0x01, 0x01, 0x01, 0x01, 0xE0],[0x01, 0x01, 0x01, 0x01, 0xE1]]
radio = NRF24(GPIO, spidev.SpiDev())
radio.begin(0, 22)

#setting communications channel
radio.setChannel(0x20)

#Setting data rate
#Setting power level of signal
#allowing Dynamic payloads
#open a reading pipe to read from the arduino NRF module
#open a writing pipe to write to the arduino NRF module
radio.setDataRate(NRF24.BR_1MBPS)
radio.setPALevel(NRF24.PA_MAX)
radio.enableDynamicPayloads()
radio.openReadingPipe(1, nodes[0])
radio.openWritingPipe(nodes[1])

message = sys.argv
command = json.loads(message[1])

# function used for sending the commands to the arduino nrf24
def radioAction(direction, message):	
        if radio.available:
                radio.stopListening()
                radio.write([direction])
                return print("Blinds " + message)

if command['control'] == 'open':
    radioAction(1, 'opening')

elif command['control'] == 'close':
    radioAction(2, 'closing')
