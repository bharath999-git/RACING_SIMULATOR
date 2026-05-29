const int potPin = A0;
const int gasPin = 8;
const int brakePin = 7;

void setup() {
  Serial.begin(9600);
  pinMode(gasPin, INPUT_PULLUP);
  pinMode(brakePin, INPUT_PULLUP);
}

void loop() {
  int steering = analogRead(potPin);      // 0-1023
  int gas   = !digitalRead(gasPin);       // 1 when pressed
  int brake = !digitalRead(brakePin);     // 1 when pressed

  Serial.print(steering);
  Serial.print(",");
  Serial.print(gas);
  Serial.print(",");
  Serial.println(brake);

  delay(50);
}