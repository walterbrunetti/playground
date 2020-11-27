
//https://arduinogetstarted.com/tutorials/arduino-light-sensor
int limit = 2;
int led = 3;



void loop() {
  // reads the input on analog pin A0 (value between 0 and 1023)
  int analogValue = analogRead(A0);

  //Serial.print("Analog reading = ");
  Serial.println(analogValue);   // the raw analog reading

  //Serial.println(analogValue);
  delay(500);
}
