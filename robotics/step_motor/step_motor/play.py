import serial #for Serial communication
import time   #for delay functions
 
arduino = serial.Serial('/dev/ttyACM0',9600) #Create Serial port object called arduinoSerialData
time.sleep(2) #wait for 2 secounds for the communication to get established

print(arduino.readline()) #read the serial data and print it as line
print("Drive Robot")

 
while 1:      #Do this in loop

    var = input() #get input from user
 
    if var == 'w':
        print("fordward py")
        arduino.write(b'w') #send 1
        
        time.sleep(1)
    
    if var == 's':
        arduino.write(b's') #send 0
        print("stop py")
        time.sleep(1)

    if var == 'x':
        arduino.write(b'x')
        time.sleep(1)
