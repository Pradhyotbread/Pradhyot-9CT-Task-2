import machine
import time

# Initialize the different components of the device
MoistureSensor = machine.ADC(machine.Pin(26)) # Initialize the sensor 
led1 = machine.Pin(15, machine.Pin.OUT) # Initialize the green LED 
led2 = machine.Pin(14, machine.Pin.OUT) # Initialize the red LED
buzzer = machine.Pin(11, machine.Pin.OUT) # Initialize the buzzer
button = machine.Pin(13, machine.Pin.IN, machine.Pin.PULL_DOWN) # Initialize the button for changing presets
potentiometer = machine.ADC(machine.Pin(27)) # Initialize the potentiometer for the custom preset

def SnakePlant(): #preset 1
    MinLevel = 250
    MaxLevel = 450
    return MinLevel, MaxLevel
def SwissCheesePlant(): #preset 2
     MinLevel = 250
     MaxLevel = 350
     return MinLevel, MaxLevel
def Pothos(): #preset 3
     MinLevel = 350
     MaxLevel = 400
     return MinLevel, MaxLevel
def Strawberry(): #preset 4
     MinLevel = 400
     MaxLevel = 450
     return MinLevel, MaxLevel
def Hydrangea(): #preset 5
     MinLevel = 400
     MaxLevel = 300
     return MinLevel, MaxLevel
def Dry(): #preset 6
     MinLevel = 500
     MaxLevel = 900
     return MinLevel, MaxLevel
def Custom(): #preset 7 (configureable)
     cusLevel = potentiometer.read_u16() # Read the value from the potentiometer for a custom moisture level
     MaxLevel = cusLevel + 100 # Set the maximum level to be 100 units higher than the custom
     MinLevel = cusLevel - 100 # Set the minimum level to be 100 units lower 
     return MinLevel, MaxLevel
def tooDry(): # Function to show that its too dry
    led1.value(0) # Turn off the green LED
    led2.value(1) # Turn on the red LED
    buzzer.value(1) # Turn on the buzzer
    time.sleep(2) # Wait for 2 seconds
def justRight(): # Function to show that its just right
    led1.value(1) # Turn on the green LED
    led2.value(0) # Turn off the red LED
    buzzer.value(0) # Turn off the buzzer
    time.sleep(2) # Wait for 2 seconds
def tooWet(): # Function to show that its too wet
    led1.value(0) # Turn off the green LED
    led2.value(1) # Turn on the red LED
    buzzer.value(1) # Turn on the buzzer
    time.sleep(2) # Wait for 2 seconds

Presetlist = [SnakePlant, SwissCheesePlant, Pothos, Strawberry, Hydrangea, Dry, Custom]

while True: #main Program 
    Mvalue = MoistureSensor.read_u16() # Read the moisture level from the sensor
    if button.value() == 1: # Check if the button is pressed
        selected =+ 1
        if selected >= len(Presetlist): # If the selected preset is greater than the number of presets, reset to 0
            selected = 0
        for i in selected: # Loop through the presets
            preset = Presetlist[selected]() # Get the preset values
            MinLevel, MaxLevel = preset # Unpack the preset values into their values
    if MaxLevel < Mvalue: # If the moisture level is above the maximum level, turn on the red LED
         tooDry()
    elif MinLevel > Mvalue: # If the moisture level is below the minimum level, turn on the red LED and the buzzer
         tooWet()
    else: # If the moisture level is within the range, turn on the green LED
         justRight()
    time.sleep(3) # Wait for 3 seconds before reading again



