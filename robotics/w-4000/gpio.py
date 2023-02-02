import RPi.GPIO as GPIO


"""
Par = PIN # / 2 = positon starting from right to left
Impar = PIN # / 2 = UpRound() = position starting from right to left

"""

in2 = 23  # orange  - PIN 16
in1 = 24  # yelow  - PIN 18
en = 25  # black  - PIN 22

in1_2 = 17  # blue  - PIN 11
en_2 = 27  # purple - PIN 13
in2_2 = 26  # green - PIN 37

# PIN 34 Ground - brown wire

p = None
p_2 = None

GPIO.setmode(GPIO.BCM)

# Motor 1
GPIO.setup(in1, GPIO.OUT)
GPIO.setup(in2, GPIO.OUT)
GPIO.setup(en, GPIO.OUT)
GPIO.output(in1, GPIO.LOW)
GPIO.output(in2, GPIO.LOW)

# Motor 2
GPIO.setup(in1_2, GPIO.OUT)
GPIO.setup(in2_2, GPIO.OUT)
GPIO.setup(en_2, GPIO.OUT)
GPIO.output(in1_2, GPIO.LOW)
GPIO.output(in2_2, GPIO.LOW)

#GPIO.setwarnings(False)


p = None
p_2= None

motor_1 = None
motor_2 = None


# Test
"""
1- Uncoment the init part (just the GPIO) and re-try
2- Try moving 'p' under the class

"""

class DCMotor():
    """A class to control one side of an L298N dual H bridge motor driver."""
    def __init__(self, en, in1, in2):
        self.in1 = in1
        self.in2 = in2
    #    all_pins = [self.in1, self.in2]
    #    GPIO.setmode(GPIO.BCM)
    #    GPIO.setup(all_pins, GPIO.OUT)
    #    GPIO.setup(en, GPIO.OUT)
    #    #GPIO.setwarnings(False)

    #    GPIO.output(in1, GPIO.LOW)
    #    GPIO.output(in2, GPIO.LOW)


        #global p
    #    p = GPIO.PWM(en, 1000)
    #    p.start(75)
        #self.p = p


    def forwards(self):
        GPIO.output(self.in1, GPIO.HIGH)
        GPIO.output(self.in2, GPIO.LOW)

    def backwards(self):
        GPIO.output(self.in1, GPIO.LOW)
        GPIO.output(self.in2, GPIO.HIGH)

    def stop(self):
        GPIO.output(self.in1, GPIO.LOW)
        GPIO.output(self.in2, GPIO.LOW)

    def set_high_valocity():
        self.p.ChangeDutyCycle(75)

    def set_medium_valocity():
        self.p.ChangeDutyCycle(50)






def initialize():
    global p
    global p_2
    global motor_1
    global motor_2


    motor_1 = DCMotor(en, in1, in2)
    motor_2 = DCMotor(en_2, in1_2, in2_2)

    p = GPIO.PWM(en, 1000)  # Pulse Width Modulation for motor 1
    p.start(75)

    p_2 = GPIO.PWM(en_2, 1000)
    p_2.start(75)





def move_forward():
    global motor_1
    global motor_2

    motor_1.forwards()
    motor_2.forwards()


def move_backward():
    global motor_1
    global motor_2

    motor_1.backwards()
    motor_2.backwards()


def stop():
    global motor_1
    global motor_2

    motor_1.stop()
    motor_2.stop()


def move_left():
    global motor_1
    global motor_2

    motor_1.stop()
    motor_2.forwards()


def move_right():
    global motor_1
    global motor_2

    motor_1.forwards()
    motor_2.stop()


def set_high_valocity():
    global motor_1
    global motor_2

    motor_1.set_high_valocity()
    motor_2.set_high_valocity()


def set_medium_valocity():
    global motor_1
    global motor_2

    motor_1.set_medium_valocity()
    motor_2.set_medium_valocity()


def exit_program():
    GPIO.cleanup()
    GPIO.setmode(GPIO.BCM)




def run_robot():

    print("\n")
    print("The default speed & direction of motor is LOW & Forward.....")
    print("s-stop f-forward b-backward l-left r-right e-exit")
    print("\n")
    print("Velocity: m-medium h-high")
    print("\n")



    while(1):
        print("Input command: ")
        x = input()
        
        if x == "f":
            print("forward")
            move_forward()
        elif x == "b":
            move_backward()
        elif x == "s":
            stop()
            #x='z'
        elif x == "l":
            move_left()
        elif x == "r":
            move_right()
        elif x == "m":
            set_medium_valocity()
        elif x == "h":
            set_high_valocity()
        elif x == "e":
            exit_program()
            break
        else:
            print("Wrond command")




if __name__ == "__main__":
    initialize()
    run_robot()
