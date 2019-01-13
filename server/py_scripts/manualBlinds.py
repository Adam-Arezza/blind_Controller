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
radio.setPALevel(NRF24.PA_MIN)
radio.enableDynamicPayloads()
radio.openReadingPipe(1, nodes[1])
radio.openWritingPipe(nodes[0])

#initialized as reader, listening on pipe
radio.startListening()

message = sys.argv
command = json.loads(message[1])

def radioAction(direction):
        #While the script is running, the message from the ndoe is read
        #The incoming message is stored in "message"	
        if radio.available:
                # radio.read(message, radio.getDynamicPayloadSize())
                radio.stopListening()
                radio.write(direction)
                radio.startListening()
                return print("Blinds opening")
        if not radio.available:
            return print('Blinds could not be reached...')

if command['control'] == 'open':
    radioAction(1)

elif command['control'] == 'closed':
    radioAction(2)
