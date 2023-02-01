from flask import Flask, render_template, request

app = Flask(__name__)

import serial #for Serial communication
import time   #for delay functions
 
arduino = serial.Serial('/dev/ttyACM0',9600) #Create Serial port object called arduinoSerialData
time.sleep(2) #wait for 2 secounds for the communication to get established

print(arduino.readline()) #read the serial data and print it as line
print("Enter 1 to get LED ON & 0 to get OFF")


@app.route('/turn_on', methods=['POST'])
def turn_on():
    arduino.write(b'1') #send 1
    time.sleep(1)
    return 'Led is ON'

@app.route('/turn_off', methods=['POST'])
def turn_off():
    arduino.write(b'0') #send 1
    time.sleep(1)
    return 'Led is OFF'


@app.route('/')
def index():
    return render_template('led.html')
    

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)
