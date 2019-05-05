void setup() {
  for (int pin=2; pin <= 9; pin++) {
    pinMode(pin, OUTPUT);
  }
  pinMode(LED_BUILTIN, OUTPUT);
  Serial.begin(9600);
}

void pause(int pause_ms) {
    digitalWrite(LED_BUILTIN, HIGH);
    delay(pause_ms);
    digitalWrite(LED_BUILTIN, LOW);
    delay(pause_ms);
}

char msgBuffer[50];

bool randomState() {
  return random(100) > 50 ? HIGH : LOW; 
}

bool loopState(int t, int pin) {
  return pin == (t % 8) + 2;
}

int DELAY = 3;

void loop() {
  for (int t = 0; t < 255; t++) {
    //pause(DELAY);
    for (int pin=2; pin <= 9; pin++) {
      //int state = randomState();
      int state = loopState(t, pin);
      sprintf(msgBuffer, "pin: %d, state: %d", pin, state);
      Serial.println(msgBuffer);
      digitalWrite(pin,  state);
      pause(DELAY / 2);
    }
    Serial.println(t);
    pause(DELAY / 3);
  }
}
