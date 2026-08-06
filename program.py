
import time

def SnakePlant(): #preset 1
    MinLevel = 250
    MaxLevel = 450

def SwissCheesePlant(): #preset 2
     MinLevel = 250
     MaxLevel = 350
     
def Pothos(): #preset 3
     MinLevel = 350
     MaxLevel = 400

def Strawberry(): #preset 4
     MinLevel = 400
     MaxLevel = 450

def Hydrangea(): #preset 5
     MinLevel = 400
     MaxLevel = 300

def Dry(): #preset 6
     MinLevel = 500
     MaxLevel = 900

def Custom(): #preset 7 (configureable)
     minLevel = 34328
     MaxLevel = 45673890

Presetlist = [SnakePlant, SwissCheesePlant, Pothos, Strawberry, Hydrangea, Dry, Custom]

for i in range(1): #main algorithim
    Presetlist[0]()
    