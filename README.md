# Arduino Voice Control 

I was in my free time, waiting for a bug to be solved in another project. So, something came to my mind! What if ... we could control our electronics with our voices? 

So I decided to make it happen. This is a very simple form of the project, but effective. What it does is just sending some data through a serial connection to an arduino board, and in the micro-controller side of the project, we make something happen. In this case, I used a single LED. 

## The Circuit

### Schematics 

![Schematics](schematics.jpg)

### Parts

1. Arduino (I used Uno, but as long as you can have a proper serial connection, the model doesn't matter)
2. LED 
3. Resistor (For most of applications, and most of boards 220 or 330 ohms is okay. But if you have a weaker model of the board that does not have a 5+ volts logic, 100 ohms is a choice.)

### Arduino code

As the arduino code was not that complicated, I put it here: 

```c++

#define LED 8

void setup(){
    pinMode(LED, OUTPUT);
    Serial.begin(9600);
}

void loop(){
    String input_string = Serial.readString(); 
    if(Serial.available()){
        if(input_text == "on\n"){
            digitalWrite(LED, HIGH);
        }
        if(input_text == "off\n"){
            digitalWrite(LED, LOW);
        }
    }
}
``` 

__NOTE__ : It is important for commands to include `\n`. Without that, it's not working. 