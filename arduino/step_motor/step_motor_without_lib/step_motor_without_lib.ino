/*
 https://create.arduino.cc/projecthub/debanshudas23/getting-started-with-stepper-motor-28byj-48-3de8c9
 https://www.web-robotica.com/arduino/motor-de-pasos-28byj-48-con-driver-uln2003-y-arduino-uno  <-- libreria para manejar el motor
 https://create.arduino.cc/projecthub/rafa/3-wheels-autonomous-vehicle-b8ab84  <-- ejemplo de estrucura


*/

#define A 2
#define B 3
#define C 4
#define D 5
 
#define NUMBER_OF_STEPS_PER_REV 512

void setup(){
  pinMode(A,OUTPUT);
  pinMode(B,OUTPUT);
  pinMode(C,OUTPUT);
  pinMode(D,OUTPUT);
}

void write(int a,int b,int c,int d){
  digitalWrite(A,a);
  digitalWrite(B,b);
  digitalWrite(C,c);
  digitalWrite(D,d);
}

void onestep(){
  write(1,0,0,0);
  delay(5);
  write(1,1,0,0);
  delay(5);
  write(0,1,0,0);
  delay(5);
  write(0,1,1,0);
  delay(5);
  write(0,0,1,0);
  delay(5);
  write(0,0,1,1);
  delay(5);
  write(0,0,0,1);
  delay(5);
  write(1,0,0,1);
  delay(5);
}

void loop(){
  int i;
  i=0;
  while(i<NUMBER_OF_STEPS_PER_REV){
    onestep();
    i++;
  }
}
