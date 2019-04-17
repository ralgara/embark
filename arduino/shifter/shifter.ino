short SER = 2;
short RCLK = 3;
short SRCLK = 4;

void setup() {
  Serial.begin(9600);
  Serial.println("Set up");
  pinMode(SER, OUTPUT);
  pinMode(RCLK, OUTPUT);
  pinMode(SRCLK, OUTPUT);
}

bool b = LOW;
short delay_ms = 200;
void loop() {
  //count up routine
  for (int j = 0; j < 256; j++) {
    //ground latchPin and hold low for as long as you are transmitting
    digitalWrite(RCLK, LOW);
    shiftOut(SER, SRCLK, MSBFIRST, j);
    //return the latch pin high to signal chip that it
    //no longer needs to listen for information
    digitalWrite(RCLK, HIGH);
    Serial.println(j);
    delay(delay_ms);
    digitalWrite(LED_BUILTIN, j & 0x1);
    delay(delay_ms);
  }
}
