from machine import Pin, ADC, PWM
from time import sleep
import utime
from dth import DTH
import pycom
import machine
from network import WLAN
from mqtt_DTH import MQTT_DTH_Client
from gipio_lcd import GpioLcd
from _pybytes import Pybytes
from _pybytes_config import PybytesConfig


B0  = 31
C1  = 33
CS1 = 35
D1  = 37
DS1 = 39
E1  = 41
F1  = 44
FS1 = 46
G1  = 49
GS1 = 52
A1  = 55
AS1 = 58
B1  = 62
C2  = 65
CS2 = 69
D2  = 73
DS2 = 78
E2  = 82
F2  = 87
FS2 = 93
G2  = 98
GS2 = 104
A2  = 110
AS2 = 117
B2  = 123
C3  = 131
CS3 = 139
D3  = 147
DS3 = 156
E3  = 165
F3  = 175
FS3 = 185
G3  = 196
GS3 = 208
A3  = 220
AS3 = 233
B3  = 247
C4  = 262
CS4 = 277
D4  = 294
DS4 = 311
E4  = 330
F4  = 349
FS4 = 370
G4  = 392
GS4 = 415
A4  = 440
AS4 = 466
B4  = 494
C5  = 523
CS5 = 554
D5  = 587
DS5 = 622
E5  = 659
F5  = 698
FS5 = 740
G5  = 784
GS5 = 831
A5  = 880
AS5 = 932
B5  = 988
C6  = 1047
CS6 = 1109
D6  = 1175
DS6 = 1245
E6  = 1319
F6  = 1397
FS6 = 1480
G6  = 1568
GS6 = 1661
A6  = 1760
AS6 = 1865
B6  = 1976
C7  = 2093
CS7 = 2217
D7  = 2349
DS7 = 2489
E7  = 2637
F7  = 2794
FS7 = 2960
G7  = 3136
GS7 = 3322
A7  = 3520
AS7 = 3729
B7  = 3951
C8  = 4186
CS8 = 4435
D8  = 4699
DS8 = 4978
note = [B0,0, C1,0, CS1,0, D1,0,0, DS1,0,0, E1,0, F1,0, FS1,0, G1,0, GS1,0, A1, AS1,
B1, C2, CS2, D2, DS2, E2, F2, FS2, G2, GS2, A2, AS2, B2, C3, CS3, D3, DS3, E3, F3, FS3, 
G3, GS3, A3, AS3, B3, C4, CS4, D4, DS4, E4, F4, FS4, G4, GS4, A4, AS4, B4, C5, CS5, D5,
DS5, E5, F5, FS5, G5, GS5, A5, AS5, B5, C6, CS6, D6,DS6, E6, F6, FS6, G6, GS6, A6, AS6,
B6, C7, CS7, D7, DS7, E7, F7, FS7, G7, GS7, A7, AS7, B7, C8, CS8, D8, DS8,0,0,0]

lcd = GpioLcd(rs_pin=Pin('P2'),
                  enable_pin=Pin('P3'),
                  d4_pin=Pin('P4'),
                  d5_pin=Pin('P5'),
                  d6_pin=Pin('P6'),
                  d7_pin=Pin('P7'),
                  num_lines=4, num_columns=20)


# I managed to connect to wifi in another way so I do not need this function. 
# But I left it to you to see what we done.
"""def wifi():
    try:
        wlan = WLAN(mode=WLAN.STA)
        nets = wlan.scan()
        for net in nets:
            if net.ssid == "AndroidAP12FC":
                print('Network found!')
                wlan.connect(net.ssid, auth=(net.sec, '12341234567'), timeout=5000)
                print('WLAN connection succeeded!')
                sleep(1)
                break
    except OSError:
        print()"""

adc = ADC()
def light_sensor():
    global lightsensor
    light = adc.channel(pin='P17', attn=adc.ATTN_11DB)  # create an analog pin on P18
    lightsensor = light.value()
    if lightsensor > 100:  # inner_led is off
        dimmer(inner_led, 0)
    if lightsensor < 100:  # inner_led is on
        dimmer(inner_led, 1)

def soil_moisture():
    global soilmoisture
    global volts
    moisture = adc.channel(pin='P15', attn=ADC.ATTN_11DB)
    volts = moisture.value()
    soilmoisture = round((volts / 3000) * 100)
    # I divided by 3000 because the largest value of volts I got from the sensor is about 3000
    return soilmoisture


motion = Pin('P13', mode=Pin.IN, pull=None)


inner_led = Pin('P12', mode=Pin.OUT, pull=None)
out_led = Pin('P11', mode=Pin.OUT)
out_led_2 = Pin('P9', mode=Pin.OUT)
out_led_3 = Pin('P8', mode=Pin.OUT)

th = DTH(Pin('P23', mode=Pin.OPEN_DRAIN), 0)


def dimmer(pn, level):
    p = Pin(pn)
    tim = PWM(0, frequency=10)
    ch = tim.channel(2, duty_cycle=level, pin=p)


def motor(level):
    global G9
    servo = PWM(0, frequency=50)  # use PWM timer 0, with a frequency of 50Hz
    G9 = servo.channel(0, pin='P10', duty_cycle=level)


def set_direction(direction):
    level = (1 / 18 * direction + 2) / 100
    sleep(3)
    motor(round(level,3))
    print("direction =", direction, "-> duty =", round(level,3))
    print()
    sleep(1) 
        

def buzzer():
    global note
    global chbuz    
    buz = Pin("P20") 
    tim = PWM(0, frequency=300)
    chbuz = tim.channel(2, duty_cycle=0.5, pin=buz)
            
def sub_cb(topic, msg):
    print(msg)

def MQTT_Client_DTH():
    global client
    try:
        client = MQTT_DTH_Client("project-2021", "io.adafruit.com",user="absik", password="aio_RqkM03YvtKrQnSscmP9qRzJD6FA1", port=1883)
        client.set_callback(sub_cb)
        client.connect()
        client.subscribe(topic="absik/dashboards/project-2021")
    except OSError:
        print()    

def py_bytes():
    global pybytes
    conf = PybytesConfig().read_config()
    pybytes = Pybytes(conf)
    pybytes.start()
    print("srtat pybytes")

def motion_sensor():
    # out_led is off if there is motion and no other lights
    if motion.value() == 0 and lightsensor > 100:  
        out_led.value(0)
        out_led_2.value(0)
        out_led_3.value(0)

    # out_led is on if there is motion and no other lights
    if motion.value() == 1 and lightsensor < 100:  
        out_led.value(1)
        out_led_2.value(1)
        out_led_3.value(1)
        print('Motion detected!')
        lcd.clear()
        lcd.putstr("Motion\n")
        lcd.putstr("detected!")
        sleep(2)
        print()

wlan = WLAN(mode=WLAN.STA)
t = utime.ticks_ms()
while True:
    light_sensor()
    motion_sensor()    
    print("lightsensor: ",lightsensor)
    print()
    lcd.clear()
    lcd.putstr("Light: \n")    
    lcd.putstr(str(lightsensor))
    lcd.putstr(" Lux")
    sleep(5)
    
    result = th.read()
    while not result.is_valid():
        sleep(0.5)
        result = th.read()
    print("Temp:",result.temperature,"Humidity: ",result.humidity)
    print()
    lcd.clear()
    lcd.putstr("Temp:")    
    lcd.putstr(str(result.temperature))
    lcd.putstr("C")
    lcd.putstr("\nHum: ")
    lcd.putstr(str(result.humidity))
    lcd.putstr("%")
    sleep(5)
    light_sensor()    
    motion_sensor()

    soil_moisture()
    print("soil moisture: ",soilmoisture,"%", "\t\t\t\t", volts)
    print()
    lcd.clear()
    lcd.putstr("soilmo: \n")    
    lcd.putstr(str(soilmoisture))
    lcd.putstr(" %")
    sleep(1)

    if result.humidity >= 55:
        set_direction(140)
        sleep(3)
        G9.duty_cycle(0)
    else:
        set_direction(60)
        sleep(3)
        G9.duty_cycle(0)
    
    
    if result.temperature > 30 or result.temperature < 20:
        buzzer()
        for i in note:
            if i == 0:
                chbuz.duty_cycle(0)
            else:
                tim=PWM(0, frequency=i)  # change frequency for change tone
                chbuz.duty_cycle(0.50)
                sleep(0.150)
    light_sensor()
    motion_sensor()
    if not wlan.isconnected() and utime.ticks_ms() - t > 30000:
        print("Trying to connect!")
        lcd.clear()
        lcd.putstr("Try To\n")    
        lcd.putstr("connect!")
        sleep(5)        
        py_bytes()
        print()

        if wlan.isconnected() == True:
            print("IS online NOW! ")
            lcd.clear()
            lcd.putstr("Wifi ^_^\n")    
            lcd.putstr("Connect")
            sleep(5)        
            MQTT_Client_DTH()
            client.publish(topic="absik/feeds/temp", msg=str(result.temperature))
            client.publish(topic="absik/feeds/humidity", msg=str(result.humidity))
            client.publish(topic="absik/feeds/light", msg=str(lightsensor))
            client.publish(topic="absik/feeds/soil", msg=str(soilmoisture))
            pybytes.send_signal( 1, result.temperature)
            pybytes.send_signal( 2, result.humidity)
            pybytes.send_signal( 3, lightsensor)
            pybytes.send_signal( 4, soilmoisture)
            print("THE Data Sent")
            lcd.clear()
            lcd.putstr("The Data: \n")
            lcd.putstr("==> Sent")
            sleep(5)
            t = utime.ticks_ms()
    if wlan.isconnected() and utime.ticks_ms() - t > 30000:
        print("Connected!")
        MQTT_Client_DTH()
        client.publish(topic="absik/feeds/temp", msg=str(result.temperature))
        client.publish(topic="absik/feeds/humidity", msg=str(result.humidity))
        client.publish(topic="absik/feeds/light", msg=str(lightsensor))
        client.publish(topic="absik/feeds/soil", msg=str(soilmoisture))
        pybytes.send_signal( 1, result.temperature)
        pybytes.send_signal( 2, result.humidity)
        pybytes.send_signal( 3, lightsensor)
        pybytes.send_signal( 4, soilmoisture)
        print("THE Data Sent")
        lcd.clear()
        lcd.putstr("The Data: \n")
        lcd.putstr("==> Sent")
        sleep(5)
        t = utime.ticks_ms()
    light_sensor()
    motion_sensor()
