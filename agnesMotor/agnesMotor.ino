// Sweep
// by BARRAGAN <http://barraganstudio.com> 
// This example code is in the public domain.


#include <Servo.h> 
 
Servo myservo;  // create servo object to control a servo 
                // a maximum of eight servo objects can be created 
 
int pos = 0;    // variable to store the servo position 
int incomingByte = 0;
 
void setup() 
{ 
  myservo.attach(9);  // attaches the servo on pin 9 to the servo object 
  Serial.begin(9600);
  pos = 90;
  myservo.write(pos);
  delay(100);
} 
 
 
void loop() 
{ 
//  for(pos = 0; pos < 180; pos += 1)  // goes from 0 degrees to 180 degrees 
//  {                                  // in steps of 1 degree 
//    myservo.write(pos);              // tell servo to go to position in variable 'pos' 
//    delay(5);                       // waits 15ms for the servo to reach the position 
//  } 
//  for(pos = 180; pos>=1; pos-=1)     // goes from 180 degrees to 0 degrees 
//  {                                
//    myservo.write(pos);              // tell servo to go to position in variable 'pos' 
//    delay(5);                       // waits 15ms for the servo to reach the position 
//  } 
  
  
  if (Serial.available() > 0) {
      // read the incoming byte:
      incomingByte = Serial.read();
      
      if(incomingByte == 2){
        stepLeft();
//        Serial.print("Got a 2");
      }else if(incomingByte == 1){
        stepRight();
//        Serial.print("Got a 1");
      }else{
//        Serial.print("Got a 0");
      }
      Serial.flush();
  }

}

void stepLeft(){
 int newVal = pos-5;
 
 if(newVal >= 0){
  pos = newVal;
  myservo.write(pos); 
  delay(100);
 }
}

void stepRight(){
 int newVal = pos+5;
 
 if(newVal < 181){
  pos = newVal;
  myservo.write(pos);
  delay(100); 
 }
}
