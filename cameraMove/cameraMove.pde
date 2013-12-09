// Original code taken from:
// Learning Processing
// Daniel Shiffman
// http://www.learningprocessing.com

// Example 16-11: Simple color tracking

// Modified by Eduardo Marisca @ MIT for AgNES
// A(u)gmented Narrative Experience Simulator
// SciFi2SciFab Project - Fall 2013

import processing.video.*;
import processing.serial.*;

// Variable for capture device
Capture video;
Serial myPort;
int counter = 0;
int launcher = 0;

// A variable for the color we are searching for.
color trackColor; 

void setup() {
  myPort = new Serial(this, Serial.list()[4], 9600);
  size(640,480);
  String[] cameras = Capture.list();
//  video = new Capture(this,width,height,15);
  video = new Capture(this,cameras[18]);
  video.start();
  // Start off tracking for red
  trackColor = color(255,0,0);
  smooth();
//  println(Serial.list());
}

void draw() {
  counter++;
  // Capture and display the video
  if (video.available()) {
    video.read();
  }
  video.loadPixels();
  image(video,0,0);

  // Before we begin searching, the "world record" for closest color is set to a high number that is easy for the first pixel to beat.
  float worldRecord = 500; 

  // XY coordinate of closest color
  int closestX = 0;
  int closestY = 0;

  // Begin loop to walk through every pixel
  for (int x = 0; x < video.width; x ++ ) {
    for (int y = 0; y < video.height; y ++ ) {
      int loc = x + y*video.width;
      // What is current color
      color currentColor = video.pixels[loc];
      float r1 = red(currentColor);
      float g1 = green(currentColor);
      float b1 = blue(currentColor);
      float r2 = red(trackColor);
      float g2 = green(trackColor);
      float b2 = blue(trackColor);

      // Using euclidean distance to compare colors
      float d = dist(r1,g1,b1,r2,g2,b2); // We are using the dist( ) function to compare the current color with the color we are tracking.

      // If current color is more similar to tracked color than
      // closest color, save current location and current difference
      if (d < worldRecord) {
        worldRecord = d;
        closestX = x;
        closestY = y;
      }
    }
  }

  // We only consider the color found if its color distance is less than 10. 
  // This threshold of 10 is arbitrary and you can adjust this number depending on how accurate you require the tracking to be.
  if (worldRecord < 10) { 
    // Draw a circle at the tracked pixel
    fill(trackColor);
    strokeWeight(4.0);
    if ((closestX < 270) || (closestX > 370)) {
      stroke(255, 0, 0);
    } else {
      stroke(0);
    }
    ellipse(closestX,closestY,64,64);
    textSize(24);
    fill(0, 0, 0);
    text(closestX, 0, 0);
  }
  
  if(counter == 15) {
      if (closestX < 270) {
        moveHead("right");
      } else if (closestX > 370) {
        moveHead("left");
      } else{
        moveHead("non");
      }
      counter = 0;
  }
  
  println(closestX);
}

void mousePressed() {
  // Modify this so camera only follows specific colour (bright pink)
  // int loc = mouseX + mouseY*video.width;
  trackColor = color(255, 0, 127); // video.pixels[loc];
}

// Send signal to Arduino board if color falls outside the tracking treshold

void moveHead(String direction) {
  if (direction == "right") {
    myPort.write(1);
    println("Printed right");
  } else if (direction == "left") {
    myPort.write(2);
    println("Printed left");
  } else {
    myPort.write(0);
    println("Printed none");
  }
}

