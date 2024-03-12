#include <SoftwareSerial.h>
const int led1 = 13;
const int led2 = 12;
void setup() {
  Serial.begin(9600);
  pinMode(led1, OUTPUT);
  pinMode(led2, OUTPUT);
  digitalWrite(led1, LOW);
  digitalWrite(led2, LOW);
  delay(1000);
  Serial.println("command");
}

// the loop function runs over and over again forever
void loop() {
  if (Serial.available() > 0)
    switch (Serial.read()) {
      case '1':
        door();
        break;
    }
}
void door() {
  Serial.println("RUN");
  digitalWrite(led1, HIGH);
  delay(1000);
  digitalWrite(led1, LOW);  // turn the LED on (HIGH is the voltage level)
  delay(1000);
  digitalWrite(led2, HIGH);

  delay(1000); // changed by naman from 1000->2000
  digitalWrite(led2, LOW);
  delay(3000);               // wait for a second
  digitalWrite(led2, HIGH);  // turn the LED off by making the voltage LOW
  delay(1000);
  digitalWrite(led2, LOW);
  delay(1000);


  digitalWrite(led1, HIGH);
  delay(2000);
  digitalWrite(led1, LOW);  // turn the LED on (HIGH is the voltage level)
  delay(1000);
  digitalWrite(led2, HIGH);

  delay(2000);
  digitalWrite(led2, LOW);
  delay(2000);               // wait for a second
  digitalWrite(led2, HIGH);  // turn the LED off by making the voltage LOW
  delay(2000);
  digitalWrite(led2, LOW);
  delay(2000);
}
