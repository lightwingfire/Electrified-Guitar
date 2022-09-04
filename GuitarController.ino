String x;
int duration;
const int triggerPin = 3;
const int buttonPin = 5;
int triggerState = 0;

void setup() {
    Serial.begin(115200);
    Serial.setTimeout(1);
    pinMode(triggerPin,OUTPUT);
    pinMode(buttonPin,INPUT);
}
void loop() {
    //while (!Serial.available());
    x = Serial.readString();

    triggerState = digitalRead(buttonPin);
    if (triggerState == HIGH) {
        Serial.println("restart");
        delay(5);
        Serial.println();
    }
    if (x.startsWith("s")) {
        Serial.println("shocking");
        duration = x.substring(1).toInt();
        if (duration > 500){
            duration = 500;
        }
        digitalWrite(triggerPin,HIGH);
        delay(duration);
        digitalWrite(triggerPin,LOW);
    }
    else {
        Serial.print(x);
    }

}