#include <LiquidCrystal.h>
LiquidCrystal lcd(30, 31, 35, 34, 33, 32);

float playerHP = 100;
int bossHP = 361;
int HPplacement = 1;
String boss = "Boss";

//Custom Symbols
byte shield[8] = {
  B00000,
  B00000,
  B01110,
  B10001,
  B10101,
  B10001,
  B01110,
  B00000,
};

byte health[8] = {
  B00000,
  B00000,
  B01010,
  B11111,
  B01110,
  B00100,
  B00000,
  B00000,
};

void setup() {
//Starting Communication
Serial.begin(9600);

//Starting the LCD screen
lcd.begin(16, 2);

}

void loop() {
//Setting player and health
lcd.createChar(0, health);
lcd.setCursor(0, 1);
lcd.write(byte(0));
  
lcd.setCursor(1, 1);
lcd.print(playerHP);

lcd.setCursor(0,0);
lcd.print("Player");


//Setting boss health and name
if(bossHP >= 1){
  HPplacement = 14;
}
if(bossHP >= 10){
  HPplacement = 13;
}
if(bossHP >= 100){
  HPplacement = 12;
}
if(bossHP >= 1000){
  HPplacement = 11;
}
if(bossHP >= 10000){
  HPplacement = 10;  
}
lcd.setCursor(HPplacement, 0);
lcd.print(bossHP);

lcd.setCursor(15, 0);
lcd.write(byte(0));


lcd.setCursor(12, 1);
lcd.print(boss);

}
