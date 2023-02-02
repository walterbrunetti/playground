import RPi.GPIO as GPIO


"""
Par = PIN # / 2 = positon starting from right to left
Impar = PIN # / 2 = UpRound() = position starting from right to left

From left to right just substract 20 (as we got 20 PINs on each row)

"""

# Motor 1
in2 = 23  # orange  - PIN 16
in1 = 24  # yelow  - PIN 18
en = 25  # black  - PIN 22

# Motor 2
in1_2 = 17  # blue  - PIN 11
en_2 = 27  # purple - PIN 13
in2_2 = 26  # green - PIN 37

# PIN 34 Ground - brown wire


GPIO.setmode(GPIO.BCM)
#GPIO.setwarnings(False)


motor_1 = None
motor_2 = None



class DCMotor():
    """A class to control one side of an L298N dual H bridge motor driver."""
    def __init__(self, en, in1, in2):
        self.in1 = in1
        self.in2 = in2
        all_pins = [self.in1, self.in2]
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(all_pins, GPIO.OUT)
        GPIO.setup(en, GPIO.OUT)
        #GPIO.setwarnings(False)

        GPIO.output(in1, GPIO.LOW)
        GPIO.output(in2, GPIO.LOW)

        try:
            p = GPIO.PWM(en, 1000)  # Pulse Width Modulation for the motor
            p.start(75)  # 75% of the velocity
            self.p = p
        except RuntimeError:
            # A PWM object already exists for this GPIO channel
            pass
        

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
    global motor_1
    global motor_2

    motor_1 = DCMotor(en, in1, in2)
    motor_2 = DCMotor(en_2, in1_2, in2_2)


def move_forward():
    motor_1.forwards()
    motor_2.forwards()


def move_backward():
    motor_1.backwards()
    motor_2.backwards()


def stop():
    motor_1.stop()
    motor_2.stop()


def move_left():
    motor_1.stop()
    motor_2.forwards()


def move_right():
    motor_1.forwards()
    motor_2.stop()


def set_high_valocity():
    motor_1.set_high_valocity()
    motor_2.set_high_valocity()


def set_medium_valocity():
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
