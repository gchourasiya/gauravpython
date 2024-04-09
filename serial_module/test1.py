import serial


serialPort = serial.Serial()


#Open Port :
serialPort.open()

#Close port:
serialPort.close()

#write to serial
message = 'Serial data'
message.encode('utf-8')
serialPort.write(message)

#read from serial
serialPort.read(1)

