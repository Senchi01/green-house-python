 # Smart växthus 
 


**Grupp medlemmar :** Absi, Basel, Ghaith, Ghiath <br>
**Handledare :** Fredrik Ahlgren <br>
**Datum :** 2021-01-12 <br>
**Kurs :** Introduction Projekt (1DT308 och 1DT902) <br><br><br><br><br>

Video om projektet:

https://youtu.be/GoUWA-SEOTo

## Abstract:
Projektet handlar ett smart växthus som sköter sig själv sparsamt på olika sätt. Detta huset har krävt mycket arbete på grund av att det fungerar i olika miljöer under alla tider. Smart växthuset är helt annorlunda än alla växthus som man har sett innan. Detta huset är uppbyggd av olika material och sensorer. I projektet sköter sensorerna som vi har använt väldigt stor del av arbetet. <br>
pybytes och adafruit är det viktigaste funktionerna som projektet har, De styr över en stor del av arbetet. De hjälper till mottagaren att få alla informationer gällande växthuset bland annat kan man få informationer om ljusstyrka, fuktighet, temperatur och vilka belysningar som är på.<br>
Växthuset har en smart funktion som sköter fuktighet om den är för högt genom att öppna fönstret för att minska fuktigheten i växthuset och stängs automatiskt sen efter när man får lagom fuktighetsvärde inne i växthuset. Yttre belysningen sköter sig själv genom att känna om det är någon som rör sig utanför växthuset och om det är mörkt ute. Inne belysningen har ena funktionen och det fungerar bara när det mörkt ute och inget ljus kommer in. Ifall växthuset har för högt temperatur inne i växthuset då kommer det ett larm som sätts i gång och börja låta lagom bra så att mottagaren kan uppmärksamma det snabbare än pybytes och adafruit. 
<br>
<br>
<br>

## Inledning 
### Background:
Från början tänkte vi att vi skulle göra gatljus som bara lyser ifall det finns något som rör sig i närheten, men senare tänkte vi varför inte vi utvecklar det ännu mer på ett sätt som vi kan ha nytta av i samhället? Så istället än bara göra belysningar som lyser beroende av rörelse, vi tänkte göra något som kan minska elektricitet förbrukningen. Här har idén ändrats från en smart belysning till ett smart växthus. Meningen av ett smart växthus är att växthuset ska kunna konsumera resurserna på ett sparsam sätt. Växthuset ska ha inomhusbelysning samt utomhusbelysning och plantor och olika sorts sensorer. 


### Idea:
Själva idén är att bygga växthus som tänder inomhusbelysningen ifall det kommer inget ljus utifrån samma sak med utomhusbelysning fast utomhusbelysning behöver även att känna till ett rörelse för att dem ska tändas och en jord fuktighetssensor som känner till ifall plantorna behöver att vattnas och en vanlig fuktighetssensor som känne till fuktigheten i huset och enligt det så ska växthuset reagerar, därför ska en servo motor kopplas till ett fönster i huset som ska vara ansvarig om fuktigheten i huset. Alla informationer ska som kommer från sensorerna ska spelas på ett yttre skärm som man lätt kan veta vad som händer i huset.

<br>
<br>
<br>


## Method:<br>
### Material:
- TEMT6000 Ambient light sensor
- Soil humidity sensor.
- Micro servo motor 9G.
- Motion sensor.
- 3W LED Module.
- Digital Buzzer Module
- The DTH11 is a basic, ultra low-cost digital temperature and humidity sensor. Den här sensorn behövde ett bibliotek DTH. https://learn.adafruit.com/dht  
- 8 x 2 LCD Module 0802 Character Display Screen. Och den här skärmen behövde ett bibliotek för att fungera. https://github.com/dhylands/python_lcd/tree/master/lcd
- Potentiometer
- Visual studio code 
- Pymakr extension
- Pycom device and lopy4
- El sladdar till komponenterna.
- Breadboard 
 <br>
<br>

### Utförande 
Det börjades med att samla alla material som vi behövde för att klara för projektet ordentligt bra. Olika sensorer blev testades av olika koder tills de fungerade som man önskade. Efter att varje sensor har testats individuellt och sågs att den fungerar effektivt med koden, då blev det dags för att koppla ihop alla komponenter på pycom enheten samtidigt blev det insamling av alla koder i en masterkod. Sedan blev det första körning för koderna för att se om alla dem fungera bra ihop. Efter många försök lyckades koden att startas med ett bra resultat. <br>
Exempel på det som blev testat flera gånger tills den fungerade så att fönstret ska öppnas genom motorn när luftfuktigheten är högre än 60% och fönstret ska stängs när den är mindre än 55%. <br>
Vi ställde även ett larm som sätts på när temperaturen stiger över 30°C eller när den är under 20°C då kommer det att uppmärksamma genom en lagom bra ljud som kommer märkas av mottagaren. Det kopplades också en skärm på storlek 8 x 2 med hjälp av ett batteri 12V och då behövs inte datorn längre. Genom belysnings sensorerna kommer yttre och inre belysningen sköts. Ute blev det två sensorer som kommer att belysa om det är något rörelse utanför växthuset och om det är mörkt ut. Inne i växthuset finns det en sensor som belysa när det är mörkt inne. Vi har gjort en funktion för att återansluta WiFi-nätverket ifall nätverksanslutningen skulle avbrytas.<br>
<br>
Via pybytes webbplats vi kan ändra koderna som finns på enheten om den är ansluten till nätverk, det betyder att vi inte behöver ansluta enheten till datorn för att modifiera koden, det räcker med att ansluta enheten till nätverk.<br>
https://pybytes.pycom.io/pymakr/device/eeac549e-e805-4ac0-9e81-63aa6de4f876 
<br>
<br>
<br>

## Results:
Vår projekt tillåter en person att sköta och ta hand om flera potentiella växter digitalt. Detta sker genom användandet av flertalet unika sensorer som via pycom trådlöst skickar data till användaren och notifierar honom om eventuella händelser (t.ex om växten kanske behöver vatten eller värme osv.). Den smarta växthuset tar till och med åtgärder vid vissa fall, t.ex öppnas växthusets fönster automatiskt när fuktigheten är för hög.<br><br> 

Vår förhoppning är att det kommer att förenkla om skötandet av växter genom en smart och digital hantering. Det kommer kanske leda till att individer kan som resultat av denna utveckling spara tid och kunna ta hand om flera växter samtidigt och mer effektivt, då sensorerna kommer att hjälpa med mycket av arbetet. Via automatiskt reglering av belysning så sparas även elektricitet, och tack vare de konstanta jordfuktighet-mätningarna sparas värdefull vatten. Vi hoppas att det även i längden leder till fler och rikare skördar.<br><br>

Det smarta växthuset, trots sin komplexitet i form av komponenter och sensorer, är generellt  billig att tillverka p.g.a. den enorma utbudet av arduino delar i marknaden. Detta möjliggör att man kan vid behov snabbt masstillverka det smarta växthuset och därmed sänka dess slutpris ytterligare för konsumenten.  <br>
Smarta Växthuset kräver försiktighet vid hantering då vitala koppling och sensorer kan skadas, därför rekommenderar vi ej att t.ex barn hanterar den. <br><br>

Självklart kan projektet uppgraderas ännu mer i framtiden, det vi har åstadkommit i projektets gång är endast en grund. Faktum är att vi hade initiala planer på att till exempel installera en vattenpump och därmed även sköta vattningen automatiskt. Dessutom ville vi även montera en elektrisk fläkt som skulle hjälpa växthuset till att hantera fuktighet och temperatur bättre. Många av dessa planer fick dock ej realiseras pga projektets längd, men potentialen för utveckling finns absolut. 
