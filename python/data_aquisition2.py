import serial 
from datetime import datetime
from serial import Serial 
ser = serial.Serial ( port = '/dev/ttyUSB0',baudrate=9600)
while ser.isOpen():
 datastring = ser.read(size=8)
 print datetime.utcnow().isoformat(),datastring
ser.close()
type(datastring)
