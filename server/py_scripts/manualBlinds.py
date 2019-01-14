import sys
import json
import RPi.GPIO as GPIO
from lib_nrf24 import NRF24
import spidev

# command = sys.argv
# response = json.loads(command[1])
# print(response)

GPIO.setmode(GPIO.BCM)

nodes = [[0x01, 0x01, 0x01, 0x01, 0xE0],[0x01, 0x01, 0x01, 0x01, 0xE1]]
radio = NRF24(GPIO, spidev.SpiDev())
radio.begin(0, 22)
#radio.setPayloadSize(32)
#setting communications channel
radio.setChannel(0x20)

#Setting data rate
#Setting power level of signal
#allowing Dynamic payloads
#open a reading pipe to read from the blinds node
#open a writing pipe to write to the blinds node
radio.setDataRate(NRF24.BR_1MBPS)
radio.setPALevel(NRF24.PA_MAX)
radio.enableDynamicPayloads()
radio.openReadingPipe(1, nodes[0])
radio.openWritingPipe(nodes[1])

#initialized as reader, listening on pipe

message = sys.argv
command = json.loads(message[1])

def radioAction(direction, message):
        #While the script is running, the message from the ndoe is read
        #The incoming message is stored in "message"	
        if radio.available:
                # radio.read(message, radio.getDynamicPayloadSize())
                radio.stopListening()
                radio.write(direction)
                return print("Blinds " + message)

if command['control'] == 'open':
    radioAction(1, 'opening')

elif command['control'] == 'close':
    radioAction(2, 'closing')
