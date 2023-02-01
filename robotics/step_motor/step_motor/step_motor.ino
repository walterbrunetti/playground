

/*
 https://create.arduino.cc/projecthub/debanshudas23/getting-started-with-stepper-motor-28byj-48-3de8c9
 https://www.web-robotica.com/arduino/motor-de-pasos-28byj-48-con-driver-uln2003-y-arduino-uno  <-- libreria para manejar el motor
 https://create.arduino.cc/projecthub/rafa/3-wheels-autonomous-vehicle-b8ab84  <-- ejemplo de estrucura
 https://lastminuteengineers.com/28byj48-stepper-motor-arduino-tutorial/
 https://leap.tardate.com/kinetics/steppermotors/28byj48/  <-- detalles de como funciona el motor con buenas fotos

*/

#include <AccelStepper.h>
#define HALFSTEP 8

// Motor pin definitions
#define motorPin1  2     // IN1 on the ULN2003 driver 1
#define motorPin2  3     // IN2 on the ULN2003 driver 1
#define motorPin3  4     // IN3 on the ULN2003 driver 1
#define motorPin4  5     // IN4 on the ULN2003 driver 1

// Initialize with pin sequence IN1-IN3-IN2-IN4 for using the AccelStepper with 28BYJ-48
AccelStepper stepper1(HALFSTEP, motorPin1, motorPin3, motorPin2, motorPin4);
int data;
int stpper1_position = 0;
int move_length = 100;
int moving = false;

void setup() {
  stepper1.setMaxSpeed(1000.0);
  stepper1.setAcceleration(100.0);
  stepper1.setSpeed(1000);
  //stepper1.moveTo(20000);

  Serial.begin(9600);

  Serial.println("This is my First Example.");

}//--(end setup )---

void loop() {
  
  if (Serial.available() > 0){
       data = Serial.read();
       Serial.write(data);


    if (data == 'w'){
      Serial.println("Start.");
      stepper1.setCurrentPosition(0);
      stepper1.moveTo(20000);
    }
    else if (data == 'x'){
      stepper1.setCurrentPosition(0);
      stepper1.moveTo(-20000);
    }
    else if (data == 's'){
      Serial.println("Stop.");
      stepper1.stop();
    }
  }

  stepper1.run();

  
  /*if (stepper1.distanceToGo() == 0) {
    stepper1.moveTo(-stepper1.currentPosition());
  }
  stepper1.run();
  */
}
