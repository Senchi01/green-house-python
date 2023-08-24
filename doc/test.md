# Test

# Kravspecifikation
1. Testa sensorernas under olika situationer.

- Sensorernas och andra material:
   - PIR sensor (Motion sensor).
   - TEMT6000 Ambient light sensor.
   - Soil humidity sensor.
   - Micro servo motor 9G.
   - The DTH11 is a basic, temperature and humidity sensor.
   - 8 x 2 LCD Module 0802 Character Display Screen.
   - 3W LED Module (for inerior lighting).
   - Four white led (for outdoor lighting).
   - Battery (10,000 mAH) with built-in solar panel.
   - Buzzer.
   - Small fan.
   - Air gas quality sensor.

\
2. Bygg ett smart växthus som är beroende av solenergi.

\
3. Samla alla sensorer i växthuset.

\
4. Grafisk dashboard som visualiserar data som registreras

## Krav 1: Testa sensorernas under olika situationer 
Steg 1 i detta krav var att testa sensorernas möjlighet att registrera värdena under olika fall. Detta skedde genom att testa varje sensor separat och sedan koppla in en i taget till projektet.
Detta genomfördes genom att t.ex gå framför eller sträcka ut en hand vid rörelse-sensorn, använda ficklampor på ljussensor och placera en jord-fuktighetssensor i jord.

## Krav 2: Bygga smart växthuset
Andra steget behandlar konstruktionsprocessen av själva växthuset. Denna process utfördes genom anskaffandet av ett färdigt miniväxthus av trä. 
Ytterligare material som behövdes var sugrör (för utomhusbelysningen i växthuset), hårdplast (för väggarna), tråd (för att binda fast hårdplasten med växthuset), sensorer och slutligen ett batteri (10.000 mAH) med inbyggd solpanel.

## Krav 3: Samla alla sensorer i växthuset
Denna steg påbörjades genom den separata monteringen varje sensor i växthuset, organisering av de många kablarna och sedan slutligen kopplandet av kablarna i Pycom-enheten.
Detta gick slutligen väldigt bra men tog dock lång tid på grund av de förhållandevis många kablarna som behövdes förlängas och organiseras prydligt.

### PIR sensor (Motion sensor):
PIR-sensorn registrerade alltid rörelse på max-avståndet (7 meter). Den här sensorn behövde inte ställas in via kod vilket innebar mindre kodtest.

### TEMT6000 Ambient light sensor:
Light sensor som registrerar ljusets styrka i räckvidden mellan (0, 4095). Den här sensorn behövde inte ställas in via kod vilket innebar mindre kodtest.

### Soil humidity sensor:
Jordfuktighetssensor som registrerar fuktigheten i jorden i räckvidden mellan (0, 3000). Denna typ av sensor har olika räckvidd beroende på kvalitén på dem. Den här sensorn behöver ställas in via kod vilket innebar många kodtest. 

### Micro servo motor 9G:
Micro servo motor för att öppna och stänga fönster. Den här motorn behöver ställas in via kod vilket innebär många kodtest, särskilt för att hitta den korrekta vinkel räckvidden för att styra motorn på ett perfekt sätt.

### Buzzer:
Buzzer används för att varna och skapa uppmärksamhet vid t.ex en för hög temperatur i växthuset eller vid en potentiell brand. Eftersom denna komponent användes i tidigare labb gick dess integrationen inom projektet smidigt.

### DTH11, digital temperatur- och fuktighetssensor:
Den här sensorn används i labb 2. Men när man kopplar ihop den med andra sensorer fungerade det inte bra, vilket innebar många kod redigeringar & pin-ändringar för att få sensorn att fungera bra samtidigt med resten av sensorerna.

### LCD_skärmen:
Denna komponent var den mest tidskrävande av alla, men när den rätt avancerade kopplingen och sedan dess kod och bibliotek fixades så blev skärmen full fungerande att visa insamlad data på.

### Små fläkt:
Detta kunde inte läggas till i projektet. Fick det beställda paketet med fläkten en dag innan kursen slutade, på grund av lovet under jul och nyår. Tanken var att använda en fläkt för att dra ut fukt i samband med att fönstret öppnas.

### luft gas kvalite:
Lyckades ej att få den fungera som vi behövde.

### 3W LED Module (för innerbelysning) och 4 vita led (för utomhusbelysning):
De behövde inte ställas in via kod vilket innebar mindre kodtest.


## Krav 4: Grafisk dashboard som visualiserar data som registreras
Dashboarden skapas med adafruit.  

## Övrigt: 
Först skrevs en Wifi-funktion för att automatiskt ansluta samt återansluta till wifi (ifall det kopplades bort). Men senare skapades en py_byts-funktion som fungerade bättre för att få kopplingen specifikt till pybets och adafruit.
