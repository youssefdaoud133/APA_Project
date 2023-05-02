#include <SoftwareSerial.h>
#include <Wire.h>
#include <LiquidCrystal_I2C.h>

// Set the LCD address to 0x27 for a 16 chars and 2 line display
LiquidCrystal_I2C lcd(0x27, 16, 2);

String home = "APA AI Assistant";

SoftwareSerial BTSerial(12, 11); // RX, TX

// remove first character
String removeFirstChar(String inputString) {
  inputString = inputString.substring(1);
  return inputString;
}

// return home 
    void returnhome(void)
    {
      lcd.clear();
      for (int i = 0; i<16; i++)
      {
        lcd.setCursor(i,0);
        lcd.write(home.charAt(i));
        delay(250);
      }
    };
// by one 
void byone(String x, int n)
  {
    for (int i = 0; i < x.length(); i++)
    {
      lcd.setCursor(i+n,1);
      lcd.write(x.charAt(i));
      delay(250);
    }
  }


  // dail 
  void Dial (String x)
  {
    lcd.blink();
    byone(x,3);
    delay(1000);
    byone("Dialing...",3);
    lcd.print("  ");
    delay(16000)    ;
    returnhome();
  }



void setup() {
  Serial.begin(9600);
  BTSerial.begin(9600);



  // initialize the LCD
  lcd.begin();
  




  // Turn on the blacklight and print a message.
  lcd.backlight();
  returnhome();
}









void loop() {
  if (BTSerial.available()) {
    String message = BTSerial.readStringUntil('\n');
    
    if(message.charAt(0) == '0'){
      
      byone("Power Off", 3);
    lcd.noDisplay();
    }
    if(message.charAt(0) == '1'){
      
      Dial(removeFirstChar(message));
    }
    if(message.charAt(0) == '2'){
     
      Dial(removeFirstChar(message));
    }
    if(message.charAt(0) == '3'){
      
      Dial(removeFirstChar(message));
    }
    
    if(message.charAt(0) == '4'){
      
  int messageLength = removeFirstChar(message).length();
  int displayWidth = 16;
  int animationDelay = 400;

  for (int i = 0; i < messageLength + displayWidth; i++) {
    lcd.clear();
    lcd.setCursor(0, 1);
    lcd.print(removeFirstChar(message).substring(i, i + displayWidth));
    delay(animationDelay);

  }
  returnhome();
    }
    if(message.charAt(0) == '5'){
      
  int messageLength = removeFirstChar(message).length();
  int displayWidth = 16;
  int animationDelay = 400;

  for (int i = 0; i < messageLength + displayWidth; i++) {
    lcd.clear();
    lcd.setCursor(0, 1);
    lcd.print(removeFirstChar(message).substring(i, i + displayWidth));
    delay(animationDelay);

  }
  returnhome();
    }
    
    




    if(message.charAt(0) == '6'){
      
      lcd.display();
      returnhome();
    }
  }
}
