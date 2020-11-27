int data;
int led = 13; 

void setup() 
{ 
  Serial.begin(9600); 
  pinMode(led, OUTPUT) // Declare the LED as an output
  Serial.println("This is my First Example.");
}
 
void loop() {
    while (Serial.available())
      {
        data = Serial.read();
      }

      if (data == '1')
      digitalWrite(led, HIGH); // Turn the LED on

      else if (data == '0')
      digitalWrite(led, LOW); // Turn the LED off

}
