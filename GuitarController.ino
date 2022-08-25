String x;
int duration;
void setup() {
    Serial.begin(115200);
    Serial.setTimeout(1);
}
void loop() {
    while (!Serial.available());
    x = Serial.readString();
    if (x.startsWith("s")) {
        Serial.print("shocking");
        duration = int(x.substring(1))
        if (duration > 500){
            duration = 500;
        }
        digitalWrite(3,HIGH);
        delay(duration);
        digitalWrite(3,LOW);
    }
    else {
        Serial.print(x);
    }

}