import machine
import time

# Initialize the different components of the device
MoistureSensor = machine.ADC(machine.Pin(27)) # Initialize the sensor 
led1 = machine.Pin(15, machine.Pin.OUT) # Initialize the green LED 
led2 = machine.Pin(14, machine.Pin.OUT) # Initialize the red LED
led3 = machine.Pin(13, machine.Pin.OUT) # Initialize the yellow LED
led4 = machine.Pin(11, machine.Pin.OUT) # Initialize the blue LED
buzzer = machine.PWM(machine.Pin(10, machine.Pin.OUT)) # Initialize the buzzer
button = machine.Pin(12, machine.Pin.IN, machine.Pin.PULL_UP) # Initialize the button for changing presets
pot = machine.ADC(machine.Pin(26)) # Initialize the potentiometer for the custom preset

# Create the presets of which will be held within functions, each function will return the min and max moisture level for the preset and use the buzzer to dictate their which preset is selected. The buzzer will beep a number of times equal to the preset number.
def SnakePlant(): #preset 1
    MinLevel = 750
    MaxLevel = 1050
    for i in range(1):
        buzzer.duty_u16(1000)
        time.sleep(0.1)
        buzzer.duty_u16(0)
        time.sleep(0.2)
    return MinLevel, MaxLevel

def SwissCheesePlant(): #preset 2
     MinLevel = 750
     MaxLevel = 950
     for i in range(2):
        buzzer.duty_u16(1000)
        time.sleep(0.1)
        buzzer.duty_u16(0)
        time.sleep(0.2)
     return MinLevel, MaxLevel
def Pothos(): #preset 3
     MinLevel = 650
     MaxLevel = 900
     for i in range(3):
        buzzer.duty_u16(1000)
        time.sleep(0.1)
        buzzer.duty_u16(0)
        time.sleep(0.2)
     return MinLevel, MaxLevel
def Strawberry(): #preset 4
     MinLevel = 550
     MaxLevel = 650
     for i in range(4):
        buzzer.duty_u16(1000)
        time.sleep(0.1)
        buzzer.duty_u16(0)
        time.sleep(0.2)
     return MinLevel, MaxLevel
def Hydrangea(): #preset 5
     MinLevel = 600
     MaxLevel = 750
     for i in range(5):
        buzzer.duty_u16(1000)
        time.sleep(0.1)
        buzzer.duty_u16(0)
        time.sleep(0.2)
     return MinLevel, MaxLevel
def Dry(): #preset 6
     MinLevel = -100000
     MaxLevel = 300
     for i in range(6):
        buzzer.duty_u16(1000)
        time.sleep(0.1)
        buzzer.duty_u16(0)
        time.sleep(0.2)
     return MinLevel, MaxLevel
def Custom(): #preset 7 (configureable)
     cusLevel = ((pot.read_u16()*1000)//65535)# Read the value from the potentiometer for a custom moisture level
     MaxLevel = cusLevel + 100 # Set the maximum level to be 100 units higher than the custom
     MinLevel = cusLevel - 100 # Set the minimum level to be 100 units lower
     for i in range(7):
        buzzer.duty_u16(1000)
        time.sleep(0.1)
        buzzer.duty_u16(0)
        time.sleep(0.2)
     return MinLevel, MaxLevel
# Functions to control the LEDs based on the moisture level, green LED for just right, red LED to dictate if the subject is not within the selected range, yellow LED for too dry, blue LED for too wet
def tooDry(): # Function to show that its too dry
    led1.value(1)
    led2.value(0) 
    led3.value(1) 
    led4.value(0) 

def justRight(): # Function to show that its just right
    led1.value(0) 
    led2.value(1) 
    led3.value(0)
    led4.value(0) 
def tooWet(): # Function to show that its too wet
    led1.value(1) 
    led2.value(0)
    led3.value(0) 
    led4.value(1) 

# making variables (will be updated in the main loop)
MaxLevel = 0
MinLevel = 0
selected = 0
buzzer.freq(700) 
Presetlist = [SnakePlant, SwissCheesePlant, Pothos, Strawberry, Hydrangea, Dry, Custom]

while True: #main Program
    Mvalue = ((MoistureSensor.read_u16()*1000)//65535)*10
    time.sleep(0.1)
    if button.value() == 0:  # button pressed
        selected += 1
        if selected >= len(Presetlist):
            selected = 0
        preset = Presetlist[selected]()      # always fetch, every press
        MinLevel, MaxLevel = preset
        while button.value() == 0:           # always debounce, every press
            time.sleep(0.05)
    if MaxLevel < Mvalue:
        tooDry()
    elif MinLevel > Mvalue:
        tooWet()
    else:
        justRight()

