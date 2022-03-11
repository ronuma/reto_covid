// Librerias
#include <LiquidCrystal.h>
#include <Keypad.h>
#include <SoftwareSerial.h>

// initialize the library with the numbers of the interface pins
LiquidCrystal lcd(6, 10, 5, 4, 3, 2);

// Teclado matricial
const byte ROWS = 3;
const byte COLS = 3;
char hexaKeys[ROWS][COLS] = {
  {'1','4','7'},
  {'2','5','8'},
  {'3','6','9'},  
};

byte colPins[COLS] = {13, 12, 11};
byte rowPins[ROWS] = {9, 8, 7};

Keypad keypad = Keypad(makeKeymap(hexaKeys),rowPins,colPins,ROWS,COLS);

//MATRIZ D DATOS
byte datos[8] = {0, 0, 0, 0, 0, 0, 0, 0};
int O, Fi, T, Po, Pg, Dg, Fa, Dc;
int covid, tratamiento, hospital, prueba, cuidarse;
float oxygen;

void setup() {
  Serial.begin(9600);
  lcd.begin(16, 2);
  lcd.print("COVID TEST");
  lcd.setCursor(0,1);
  lcd.print("PRESS TO START");
}

void loop() {
  char answer = keypad.getKey();
  if(answer){
  
/* SOLICITUDES */
    input("BAJO 02?", 0, answer);
	input("FEVER?", 1, answer);
    input("TOS SECA?", 2, answer);
    input("PERDIDA OLFATO?", 3, answer);
 	input("PERDIDA GUSTO?", 4, answer);
    input("DOLOR GARGANTA?", 5, answer);
  	input("FATIGA?", 6, answer);
  	input("DOLOR CABEZA?", 7, answer);

/* MEDICIONES */
    // Temperatura (sensor -40°C a 125°C) 
    float volts = (analogRead(A0)/1024.0)*5.0;
    float temperature = (volts-0.5)*100;
    byte FlagTemp;
    if (temperature >= 38){
      FlagTemp = 1;
    }
    else{
      FlagTemp = 0; 
    }
    lcd.clear();
    lcd.print("TEMP");
    lcd.setCursor(0,1);
    lcd.print(temperature);
    delay(3000);
    
 // Oxigeno (sensor 0% a 100%)
    float oxygen = (analogRead(A1)/1024.0)*100.0;
    byte FlagOxy;
    if(oxygen < 89){
      FlagOxy = 1;
    }
    else{
      FlagOxy = 0;
    }   
    lcd.clear();
    lcd.print("OXIGENO");
  	lcd.setCursor(0,1);
    lcd.print(oxygen);
    delay(3000);

  // Funciones y comparación
 O = datos[0];
 Fi = datos[1];
 T = datos[2];
 Po = datos[3];
 Pg = datos[4];
 Dg = datos[5];
 Fa = datos[6];
 Dc = datos[7];
 
 covid = (Fi and T and Po and Pg and Fa) or (O and(Fi or T or Po or Pg or Fa));
 hospital = O or (O and(Fi or T or Po or Pg or Fa));
 tratamiento = (Fi and T and Po and Pg and Fa);
 prueba = (Fi or T or Po or Pg or Fa) and not O;
 cuidarse = not(Fi or T or Po or Pg or Fa) and not O;
    
 Serial.print(O); Serial.print("|");
 Serial.print(Fi); Serial.print("|");
 Serial.print(T); Serial.print("|");
 Serial.print(Po); Serial.print("|");
 Serial.print(Pg); Serial.print("|");
 Serial.print(Dg); Serial.print("|");
 Serial.print(Fa); Serial.print("|");
 Serial.print(Dc); Serial.print("|");
 Serial.print(temperature); Serial.print("|");
 Serial.print(oxygen); Serial.print("|");
 Serial.print(covid); Serial.print("|");
 Serial.print(hospital); Serial.print("|");
 Serial.print(tratamiento); Serial.print("|");
 Serial.print(prueba); Serial.print("|");
 Serial.print(cuidarse); 
 delay(3000);
 Serial.flush();

 if (covid){
    diagnose("POSITIVO COVID");
  }
   if (hospital){
    diagnose("HOSPITALIZARSE");
  }
  if (tratamiento){
    diagnose("TRATESE");
  }
  if (prueba){
    diagnose("HAGASE PRUEBA");
  }
  if (cuidarse){
    diagnose("CUIDESE");
  }
}
}

/* FUNCIONES UTILIZADAS */
// Pide la respuesta del usuario
void input(String question, int index, char answer) {
	lcd.clear();
    lcd.print(question);
    lcd.setCursor(0,1);
    lcd.print("Yes=1 No=2");
  
  	boolean respuesta = 0;
    
  	while(respuesta == 0) {
    	answer = keypad.waitForKey();
    	switch(answer){
      	case '1':
       		datos[index] = 1;
      		respuesta = 1;
      		break;
      	case '2':
        	datos[index] = 0;
      		respuesta = 1;
      		break;
      	default:
      		respuesta = 1;
      		break;
        }
  	}	
}

// Imprime el diagnostico
void diagnose(String msg) {
	lcd.clear();
    lcd.print(msg);
    delay(3000);
}