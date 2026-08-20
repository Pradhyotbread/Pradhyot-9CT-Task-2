# Pradhyot-9CT-Task-2
term 3 mechatronics assesment  
A moisture dectector machine

## Requirement Outline
### The Problem: 
how do you know if something has properly dried or perhaps if a plant is within its correct moisture level?

### The Solution: 
The moisture detection device (MDD) will use its sensors to detect the moisture level within an item or an area, there would be LEDs on the device to show the level based on the mode that the person selects, for example: drying mode - will light up green when the object is almost void of moisture within the item, or plant mode - will light up green if a plant has the correct moisture level based on several plant presets and red if it is out of that range

### Functions of the Device: 
* has several modes able to be cycled through via a button
* based on the mode selected an LED array will light to indicate the correct level 
* user could input a custom moisture level based on the potentiometer 
* buzzer gives physical response to the non-corresponding values 
* moisture sensor is able to read moisture levels without issue

### Functional Requirements
* **Moisture Sensor** - detects the moisture level within an object and outputs a response within the provided value range
* **LED Output** - a Set of LEDs that will dictate if the object is out of its preset level
* **Buzzer** - a simple buzzer to set dictate when the object is out of its preset range with a tactitle feeling (of which is the buzz)
* **Button** - a simple button that is able to rotate through the different preset values
* **Potentiometer** - uses its swivel to create a custom preset that would allow for the use of a custom preset

### Non-functional Requirements
* **response time** - a response should be given within about 3 seconds as the device would take a little time to analyze the whole amount of data
* **efficiency** - have concise and purposeful code within the pico 
* **accuracy** - the readings should be within 5kPa so that the readings are accurate  

### Test Cases
| Test Case | Input     | Expected Output   |
|---------- |---------- |----------------   |
|object too dry| moisture sensor reads a value above the provided value|light an LED and a small, harsh buzzer humm to signify the object is too dry |
|Object too wet|moisture sensor reads a value below the provided value|light an LED and a small buzzer but harsh humm to signify the object is too wet|
|object within the correct moisture|moisture sensor detects a value within the provided range|light an LED accompanied with a gentle buzzer humm.|
|Device changes measuring type|With a button press the device will change presets to another value range|A small LED changes color to signify the mode and the presets within the device would change| 
|User makes a custom value|using a potentiometer the user could manually create a value range for the device to use| the device temporarily stores the value and uses it to provide a reading| 

## Algorithms 
### Flowchart
 ![Diagram](MDD.png)

### Pseudocode 
pseudocode()  
BEGIN PerfectM()  
    clear_outputs()  
    OUTPUT green_led.value(1)  
    OUTPUT buzzer.on()  
END PerfectM()  

BEGIN too_dry()  
    clear_outputs()  
    OUTPUT yellow_Led.value(1)  
    OUTPUT buzzer.on()  
END too_dry  

BEGIN too_wet()  
    clear_outputs()  
    OUTPUT red_Led.value(1)  
    OUTPUT buzzer.on()  
END too_wet  

BEGIN Preset_Mode()  
    clear_outputs()  
    INPUT Button.value(+1)  
    Preset_List[] (navigate through list with button)  
    Preset_Value = Preset_List[chosen value]  
END Preset_Mode()  

BEGIN  
    WHILE Device is on   
       READ moisture level  
       Preset_Mode()  
       IF Mosture > Preset_Value  
            THEN too_wet()  
       END IF  
       IF Moisture < Preset_Value  
            THEN too_dry()  
            ELSE PerfectM()  
       END IF  
    ENDWHILE  
END
## Development and Intergration
### prototyping code 
#### Prototype 1

```
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
```
#### prototype 2
```
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
potentiometer = machine.ADC(machine.Pin(26)) # Initialize the potentiometer for the custom preset

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
     MinLevel = 300
     MaxLevel = 400
     return MinLevel, MaxLevel
def Dry(): #preset 6
     MinLevel = 500
     MaxLevel = 9999999
     return MinLevel, MaxLevel
def Custom(): #preset 7 (configureable)
     cusLevel = potentiometer.read_u16() * 100 / 65535 # Read the value from the potentiometer for a custom moisture level
     MaxLevel = cusLevel + 10 # Set the maximum level to be 100 units higher than the custom
     MinLevel = cusLevel - 10 # Set the minimum level to be 100 units lower 
     return MinLevel, MaxLevel
def tooDry(): # Function to show that its too dry
    led1.value(1)
    led2.value(0) 
    led3.value(1) 
    led4.value(0) 
    buzzer.freq(700)
    buzzer.duty_u16(1000)
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
    buzzer.freq(700)
    buzzer.duty_u16(1000)
def clearAll():
     led1.value(0)
     led2.value(0)
     led3.value(0)
     led4.value(0)
     buzzer.duty_u16(0)

# making variables
MaxLevel = 0
MinLevel = 0
selected = 0
minm = 0
maxm = 65535
Presetlist = [SnakePlant, SwissCheesePlant, Pothos, Strawberry, Hydrangea, Dry, Custom]

while True: #main Program
    Mvalue = (maxm - MoistureSensor.read_u16())*100/(maxm)
    if button.value() == 0:  # button pressed
        selected += 1
        if selected >= len(Presetlist):
            selected = 0
        print(selected)
        preset = Presetlist[selected]()      # always fetch, every press
        MinLevel, MaxLevel = preset
        while button.value() == 0:           # always debounce, every press
            time.sleep(0.05)
    if MaxLevel <= Mvalue:
        tooDry()
    elif MinLevel >= Mvalue:
        tooWet()
    else:
        justRight()
```
    
#### prototype 3
```
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
potentiometer = machine.ADC(machine.Pin(26)) # Initialize the potentiometer for the custom preset

def SnakePlant(): #preset 1
    MinLevel = 250
    MaxLevel = 450
    print(MaxLevel)
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
     MinLevel = 300
     MaxLevel = 400
     return MinLevel, MaxLevel
def Dry(): #preset 6
     MinLevel = 500
     MaxLevel = 9999999
     print(MaxLevel)
     return MinLevel, MaxLevel
def Custom(): #preset 7 (configureable)
     cusLevel = (potentiometer.read_u16()*1000) // 65535# Read the value from the potentiometer for a custom moisture level
     MaxLevel = cusLevel + 100 # Set the maximum level to be 100 units higher than the custom
     MinLevel = cusLevel - 100 # Set the minimum level to be 100 units lower
     print(MaxLevel)
     return MinLevel, MaxLevel
def tooDry(): # Function to show that its too dry
    led1.value(1)
    led2.value(0) 
    led3.value(1) 
    led4.value(0) 
    buzzer.freq(700)
    buzzer.duty_u16(1000)
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
    buzzer.freq(700)
    buzzer.duty_u16(1000)
def clearAll():
     led1.value(0)
     led2.value(0)
     led3.value(0)
     led4.value(0)
     buzzer.duty_u16(0)

# making variables
MaxLevel = 0
MinLevel = 0
selected = 0
Presetlist = [SnakePlant, SwissCheesePlant, Pothos, Strawberry, Hydrangea, Dry, Custom]

while True: #main Program
    Mvalue = ((MoistureSensor.read_u16()*1000)//65535)*10
    if button.value() == 0:  # button pressed
        selected += 1
        if selected >= len(Presetlist):
            selected = 0
        preset = Presetlist[selected]()      # always fetch, every press
        MinLevel, MaxLevel = preset
        while button.value() == 0:           # always debounce, every press
            time.sleep(0.05)
    if MaxLevel <= Mvalue:
        tooDry()
    elif MinLevel >= Mvalue:
        tooWet()
    else:
        justRight()
```
#### finalized code
```
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
     print("dry")
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

# making variables
MaxLevel = 0
MinLevel = 0
selected = 0
buzzer.freq(700) 
Presetlist = [SnakePlant, SwissCheesePlant, Pothos, Strawberry, Hydrangea, Dry, Custom]

while True: #main Program
    Mvalue = ((MoistureSensor.read_u16()*1000)//65535)*10
    print("raw:", MoistureSensor.read_u16(), "scaled:", Mvalue)
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
```
## Evaluation 
### Peer Evaluation 

#### Reviewer #1 (Alfonso D)
|plus|minus|Implication|
|-|-|-|
The cables whilst seemingly messy do have a clean layout and are purposefully placed| the potentiometer seems complicated and annoying to use| the preset system is interesting and practical for the way its used but as for the potentiometer preset it seems complicated and problematic as the values that are inputed can't easily be figured out when first using the machine|

#### Reviewer #2 (Lucas L)
|plus|minus|Implication|
|-|-|-|
|the design is simple and easy to grasp at a moment's notice and the code for the project is also simple making so that there are very few issues when actually running the design| The decision to import the whole machine library made the code more crowded and cluttered than it had needed to be|the design of the device is well thought out with the inputs and outputs separated with the the wires within the middle making the potential for wiring issues or mistakes decrease rapidly so although the code is more cluttered than neccessary it is compensated for by the wiring of the device.| 

### Final Evaluation
#### Evaluate your Final Test in Relation to Functional Criteria
In relation to the original functional critera outlined within the first section, my final product has been able to reach all of these goals. Although whilst all of these features have been implemented the purposes of some of these devices have been changed, with the buzzer being changed to dictate the preset that has been chosen as i had deemed it too annoying for its original purpose. Overall all the criteria that i had originally outlined have been met although with tweaking of their purpose to better suit their functions within the device so that it could function more cohesively.

#### Evaluate your Final Test in Relation to Non-Functional Criteria
In respect to the Non-Functional criteria that i had outlined most of the criteria have been fufilled. Efficieny and Response times have been fufilled with times resulting in less than a second as it is a efficent and condense project, although the Accuracy requirement has not quite been fufilled as kPa is not recorded within the instrument that was chosen and the resulting algorithim to transform the output into that level would be far too unnescessary for a machine like this. As a whole the device was able to achive most of its given criteria perfectly and its others with minor issues resulting in their exclusion

#### Evaluate your Final Performance in Relation to the Identified Need
In relation to the Need that had been outlined, the device is able to succesfully and accurately able to measure and provide assistance when it comes to the already assigned values that had been given. Although the sensor is only able to detect and measure the items infornt of it the function is still the same and as more LED's have been added into the project the device has been tweaked to ensure a better and more effective final device.

#### Evaluate your Project in Relation to Project Management
This project in relation to its Project management has been slightly unstable as it was quite difficult to find the correct sensor for the project, but the project has been done over a large time period as thus not inducing too much stress or inducing a need to rush the project, in terms the project whilst having some minor difficulties when it came to finding parts were compensated for as both the Coding portion and Project Documentation sections were able to be wittled down over the given period of time properly.

#### Evaluate your Project in Relation to Peer Feedback.
In relation to the Peer Feedback given, both peers had critized the potentiometer as it was 'complicated and annoying' of which I concur, as the device has limited space the potenitometer is suffocated thus leading to it being harder to use and the strange way the sensors are coded into the system also is a large barrier for users to overcome when it comes to using the custom preset. Although Both reviewers had responded to the excellence of the wiring and its clean look alongside the programming being concise for its function. Overall the general concensus that was given about the device is that it was clean but certain parts could be refined and further taken so that the device could be elevated to a better one.

#### Justify Future Improvements you could make to your Final Product
future improvements that could be made for the device is possibly to instead of using separte LEDs it would be more efficent to use a light board, to not only save on space but also make it clearer on the needed fixes within the object. Another potential change is to fufill the accuracy criteria i had neglected, although seemingly redundant this feature could make the device useful for more than just house plants and provide a more overarching use with precise values. 

## Final Statement
To finalise the Moisture Detection Device is a comprehensive, and condensed product that is efficent and useful for its purpose, it uses an intuitive preset system to get readings for different objects/plants to ensure that they are within the correct moisture level as to prosper. It hosts a set of LEDs (light emitting diodes) to display the findings of the moisture sensor with: green signifying that it is within the correct level, Red to express otherwise and finally Yellow and Blue to show if the object/plant is too dry or wet respectively.
