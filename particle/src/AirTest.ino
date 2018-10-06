#include <math.h>
#include <application.h>

int pin = D1;
unsigned long duration;
unsigned long starttime;
unsigned long sampletime_ms = 15000;//sampe 30s ;
unsigned long lowpulseoccupancy = 0;
float ratio = 0;
float concentration = 0;
unsigned long pulse_start;
unsigned long pulse_count;
bool sensorTriggered;
int sensorVal;

void setup()
{
    Serial.begin(9600);
    pinMode(pin,INPUT);
    pinMode(D7, OUTPUT);

    starttime = millis();//get the current time;
}

void loop() {
  sensorVal = digitalRead(pin);
  if (sensorVal == LOW && sensorTriggered == false) {
    pulse_start = millis();
    sensorTriggered = true;
    while(digitalRead(pin) == LOW) {}
    lowpulseoccupancy += (millis() - pulse_start);
    sensorTriggered = false;
  }

  if ((millis()-starttime) > sampletime_ms)//if the sampel time == 30s
  {
      ratio = lowpulseoccupancy/(sampletime_ms*10.0);  // Integer percentage 0=>100
      // concentration = 1.1*pow(ratio,3)-3.8*pow(ratio,2)+520*ratio+0.62; // using spec sheet curve
      concentration = ratio * ratio * 0.1809 + 3.8987 * ratio;

      Serial.print(lowpulseoccupancy);
      Serial.print(",");
      Serial.print(ratio);
      Serial.print(",");
      Serial.println(concentration);
      //Particle.publish("airQ", String::format("{\"ratio\": %d, \"concentration\": %f}", ratio, concentration));
      lowpulseoccupancy = 0;
      starttime = millis();
  }
}


#if 0
void loopOld()
{
    digitalWrite(D7, LOW);
    pulse_count = 0;
    // wait for signal to go low
    while(digitalRead(pin) == HIGH && pulse_count++ < 1000) {}

    if (pulse_count != 1000) {
      pulse_count = 0;
      pulse_start = millis();
      while(digitalRead(pin) == LOW) { pulse_count++; }
      lowpulseoccupancy += (millis() - pulse_start);
      Serial.print(pulse_count);
      Serial.print("\r\nP");
    }

    /*

    duration = pulseIn(pin, LOW);
    digitalWrite(D7, LOW);
    lowpulseoccupancy = lowpulseoccupancy+duration;

    */

    if ((millis()-starttime) > sampletime_ms)//if the sampel time == 30s
    {
        ratio = lowpulseoccupancy/(sampletime_ms*10.0);  // Integer percentage 0=>100
        concentration = 1.1*pow(ratio,3)-3.8*pow(ratio,2)+520*ratio+0.62; // using spec sheet curve
        Serial.print(lowpulseoccupancy);
        Serial.print(",");
        Serial.print(ratio);
        Serial.print(",");
        Serial.println(concentration);
        Particle.publish("airQ", String::format("{\"ratio\": %d, \"concentration\": %f}", ratio, concentration));
        lowpulseoccupancy = 0;
        starttime = millis();
    }
}
#endif


unsigned long pulseIn2(uint16_t pin, uint8_t state) {

    GPIO_TypeDef* portMask = (PIN_MAP[pin].gpio_peripheral); // Cache the target's peripheral mask to speed up the loops.
    uint16_t pinMask = (PIN_MAP[pin].gpio_pin); // Cache the target's GPIO pin mask to speed up the loops.
    unsigned long pulseCount = 0; // Initialize the pulseCount variable now to save time.
    unsigned long loopCount = 0; // Initialize the loopCount variable now to save time.
    unsigned long loopMax = 20000000; // Roughly just under 10 seconds timeout to maintain the Spark Cloud connection.

    // Wait for the pin to enter target state while keeping track of the timeout.
    while (GPIO_ReadInputDataBit(portMask, pinMask) != state) {
        if (loopCount++ == loopMax) {
            return 0;
        }
    }

    // Iterate the pulseCount variable each time through the loop to measure the pulse length; we also still keep track of the timeout.
    while (GPIO_ReadInputDataBit(portMask, pinMask) == state) {
        if (loopCount++ == loopMax) {
            return 0;
        }
        pulseCount++;
    }

    // Return the pulse time in microseconds by multiplying the pulseCount variable with the time it takes to run once through the loop.
    return pulseCount * 0.405; // Calculated the pulseCount++ loop to be about 0.405uS in length.
}
