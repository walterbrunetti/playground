import serial #for Serial communication
import time   #for delay functions
 
arduino = serial.Serial('/dev/ttyACM0',9600) #Create Serial port object called arduinoSerialData
time.sleep(2) #wait for 2 secounds for the communication to get established

arduino.flushInput()

while True:
    try:
        ser_bytes = arduino.readline()
        decoded_bytes = float(ser_bytes[0:len(ser_bytes)-2].decode("utf-8"))
        print(decoded_bytes)
    except:
        print("Keyboard Interrupt")
        break
