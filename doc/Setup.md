# Setup

## Huvudprogram
### main.py
Main loopen styr och reglerar effektivt alla sensorer samt läser och skickar data från dessa.
Initialt så börjar Main loopen med att kontrollera (samt aktivera vid behov) inre & yttre belysning, öppna & stänga fönster, starta buzzer, och slutligen så ser den till att all relevant insamlad data skickas till pybytes och adafruit. 

### Funktion light_sensor _(main.py)_
Kontrollerar värdena från ljus sensorn (TEMT6000 Ambient). Den avger värden mellan 0 och 4095. Ju mindre värden, desto mörkare är omgivningen kring sensorn osv. 

### Funktion soil_moisture _(main.py)_
Jordfuktighets-sensorn avger värden mellan 0 och 3000. Så för att få värdet i procent används följande matematiska beräkning enligt formeln; "Jordfuktighet i % = round((volts / 3000) * 100)", således ges värden mellan 0% och 100% .
Ett mindre värde betyder att jorden behöver vatten och ett högre värde betyder att jorden har tillräckligt med vatten.

### Funktion motor _(main.py)_
För att starta motorn (Micro servo motor 9G).

### Funktion set_direction _(main.py)_
Denna funktion styr motorn, t.ex för att öpppna eller stänga fönstret i växthuset.

### Funktion motion_sensor _(main.py)_
Pir (Passive infrared) sensorn avger värdet 1 när den detekterar rörelse och 0 när den inte gör det. Denna funktion styr yttre belysningen tillsammans med ljus-sensorn.
Således så är de 4 yttre LED-lamporna påtända endast om det är mörkt eller om rörelse detekteras.

### Funktion py_bytes _(main.py)_
Denna härliga funktion försöker ständigt etablera koppling med internet ifall det skulle försvinna. Denna funktion kopplar också pycom enheten till pybytes server.
När internetuppkoppling har etablerats så hjälper funktionen också med att skicka sensordata till adafruit.

## lcd_api.py 
Är ett bibliotek för LCD_skärmen.

## gipio_lcd.py
För att styra LCD_skärmen.

### Funktion buzerr _(main.py)_
För att starta buzzer.

### Dimmerfunktion _(dimmer.py)_
Justerar en LEDs ljusstyrka genom att ändra dess duty cycle.
Den tar emot en variabel mellan 0-1 för ljusstyrka och en variabel för pin-numret i pycom som lampan är kopplad till.

### MQTT_DTH _(main.py, mqtt_dth.py)_
För att få kontakt till adafruit servern och att dessa ska fungerar utan eventuella kraschar så ändrades funktions namnet "mqtt" till mqtt_dth eftersom det visade sig att det finns en funktion med samma namn i pycom enheten.
Denna lösning implementeras för att få förbindelse med servern utan problem. För att koppla till en mqtt server måste man ange adress,namn och lösenord för servern.
