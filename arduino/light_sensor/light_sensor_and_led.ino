
//https://arduinogetstarted.com/tutorials/arduino-light-sensor
int limit = 2;
int led = 3;


void setup() {
  // initialize serial communication at 9600 bits per second:
  Serial.begin(9600);
}

void loop() {
  // reads the input on analog pin A0 (value between 0 and 1023)
  int analogValue = analogRead(A0);

  Serial.print("Analog reading = ");
  Serial.print(analogValue);   // the raw analog reading


  if (analogValue < limit) {
    Serial.println(" - Dark");
    analogWrite(led, 100);
  } else {
    analogWrite(led, 0);
  }

  delay(500);
}
