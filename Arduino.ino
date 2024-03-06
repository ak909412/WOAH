#include <Servo.h> 
const int NumServos = 5; 
const int BaudRate = 9600; 
const char StartBit = '$'; 
Servo servos[NumServos]; // Thumb, Index, Middle, Ring, Pinky 
int servoPins[] = {8, 9, 10, 11, 12}; // Thumb, Index, Middle, Ring, Pinky 
const int servoPin = 9; 
void setup() { 
 for (int i = 0; i < NumServos; ++i) { 
 servos[i].aƩach(servoPins[i]);
 servos[i].write(0); 
 delay(1000); 
 } 
 Serial.begin(BaudRate); 
} 
char getChar() { 
 if (!Serial.available()) return '?'; 
 char cur = Serial.read(); 
 Serial.print("Char: " + cur); 
 return cur; 
} 
String readSerialData() { 
 String res = ""; 
 bool readStartBit = false; 
 while (Serial.available() && getChar() != StartBit) ; 
 while (res.length() != NumServos) { 
 char cur = getChar(); 
 if (cur == '0' || cur == '1') res += cur; 
 } 
 return res; 
} 
void loop() { 
 String cur = readSerialData(); 
 Serial.println("Current: " + cur); 
 for (int i = 0; i < NumServos; ++i) { 
 int value = int(cur[i]-'0')*180; 
 if (i % 2 == 1 || i==0) { 
 value = 180 - value; // Invert the value 
 } 
 servos[i].write(value); 
} 
} 


// Explanation:
// The code starts by including the "Servo.h" library, which is used to control the servos. 
// The code defines some constants, including the number of servos 
// (NumServos), the baud rate for serial communicaƟon (BaudRate), and a 
// start bit character for the serial communicaƟon (StartBit).
// The code then iniƟalizes an array of Servo objects (servos) with the 
// specified pins for each servo (servoPins), aƩaches each servo to its 
// corresponding pin, and sets the iniƟal posiƟon of each servo to 0 
// degrees. This is done in the setup() funcƟon, which is called once when 
// the Arduino is powered on or reset. 
// The code defines two helper funcƟons: getChar() and readSerialData(). 
// getChar() reads a single character from the serial input, if available, and 
// returns it. If there is no data available, it returns a quesƟon mark 
// character ('?'). readSerialData() reads the serial input unƟl it finds the 
// start bit character (StartBit), then reads NumServos binary digits ('0' or 
// '1') and returns them as a String. 
// The main loop() funcƟon repeatedly calls readSerialData() to get the 
// binary values for each servo, converts them to a servo angle (0 to 180 
// degrees), and writes the angle to the corresponding servo using the 
// Servo.write() method. The code inverts the angle for odd-indexed servos 
// (Index and Ring fingers) and the thumb servo (the first servo in the 
// array). 
// This code can be used to control a roboƟc hand or other mechanical 
// system with 5 degrees of freedom, using a serial connecƟon to send 
// commands to the Arduino. 
