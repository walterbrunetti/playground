import RPi.GPIO as GPIO


in1 = 24  # yelow
in2 = 23  # orange
en = 25  # black

in1_2 = 17  # blue
in2_2 = 26  # green
en_2 = 27  # purple

p = None
p_2 = None


temp1=1

GPIO.setmode(GPIO.BCM)
GPIO.setup(in1,GPIO.OUT)
GPIO.setup(in2,GPIO.OUT)
GPIO.setup(en,GPIO.OUT)
GPIO.output(in1,GPIO.LOW)
GPIO.output(in2,GPIO.LOW)


GPIO.setup(in1_2,GPIO.OUT)
GPIO.setup(in2_2,GPIO.OUT)
GPIO.setup(en_2,GPIO.OUT)
GPIO.output(in1_2,GPIO.LOW)
GPIO.output(in2_2,GPIO.LOW)

p=GPIO.PWM(en,1000)
#p.start(75)

p_2=GPIO.PWM(en_2,1000)
#p_2.start(75)

motor_1 = None
motor_2 = None





class DCMotor():
    """A class to control one side of an L298N dual H bridge motor driver."""
    def __init__(self, en, in1, in2):
        self.in1 = in1
        self.in2 = in2
    #    all_pins = [self.in1, self.in2]
    #    GPIO.setmode(GPIO.BCM)
    #    #GPIO.setup(all_pins, GPIO.OUT)
    #    GPIO.setup(in1, GPIO.OUT)
    #    GPIO.setup(in2, GPIO.OUT)
    #    GPIO.setup(en, GPIO.OUT)
    #    #GPIO.setwarnings(False)

    #    GPIO.output(in1,GPIO.LOW)
    #    GPIO.output(in2,GPIO.LOW)
    #    p = GPIO.PWM(en,1000)
    #    p.start(75)

    #    print "Done setting up"


    def forwards(self):
        GPIO.output(self.in1, GPIO.HIGH)
        GPIO.output(self.in2, GPIO.LOW)

    def backwards(self):
        GPIO.output(self.in1, GPIO.LOW)
        GPIO.output(self.in2, GPIO.HIGH)

    def stop(self):
        GPIO.output(self.in1, GPIO.LOW)
        GPIO.output(self.in2, GPIO.LOW)



def initialize():
    global p
    global p_2
    global motor_1
    global motor_2

    #p=GPIO.PWM(en,1000)
    p.start(75)

    #p_2=GPIO.PWM(en_2,1000)
    p_2.start(75)

    motor_1 = DCMotor(en, in1, in2)
    motor_2 = DCMotor(en_2, in1_2, in2_2)




def go_fordward():
    motor_1.forwards()
    motor_2.forwards()

def stop():
    motor_1.stop()
    motor_2.stop()






def run_robot():


    

    while(1):
        print "Input command: "
        x = raw_input()
        
        if x == "f":
            print "forward"
            go_fordward()
        elif x == "b":
            # backwards
            pass
        elif x == "s":
            print "stop"
            stop()
            x='z'
        elif x == "l":
            # left
            pass
        elif x == "r":
            # right
            pass
        elif x == "e":
            # exit
            GPIO.cleanup()
            #GPIO.setmode(GPIO.BCM)
            break
        else:
            print "Wrond command"




if __name__ == "__main__":
    initialize()
    run_robot()
