int input = 2;
int val = 0;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(input, INPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  val = digitalRead(input);
  Serial.println(val);
  delay(1);
}
