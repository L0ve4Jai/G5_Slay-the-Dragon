Paladin_Health = 150
Cleric_Health = 75
Wizard_Health = 100
Goblin_Health = 300
Dragon_Health = 1000
Gargoyle_Health = 500
from random import randint
print(randint(1,10))

Welcome = print("Welcome to Slay The Dragon™!")
Intro = print("In a realm shrouded in the mists of legend, the mighty kingdom of [KINGDOM NAME] once reigned supreme, its borders guarded by the valor of its knights and the wisdom of its sovereign, [KING NAME]. Yet, under the cloak of night, a shadow darker than any before descended upon the land. From the depths of ancient lore emerged [DRAGON NAME], a creature of fire and fury, whose very name struck fear into the hearts of all who heard it. Whispers of the dragon's rampage spread like wildfire, challenging the very foundation of the kingdom's strength. But amidst the chaos, three heroes emerged, their resolve unyielding in the face of insurmountable odds. Driven by a steadfast courage, they vowed to ascend the treacherous peaks of the forbidden mountain where the dragon dwelled, First among them was [PALADIN NAME], a stalwart defender whose unwavering faith in righteousness served as a beacon of hope amidst the encroaching shadows. Alongside the paladin strode [WIZARD NAME], a master of arcane arts whose intellect and mastery of magic were matched only by their unyielding determination to protect the realm from all manner of arcane threats. Completing the trio was [CLERIC NAME], a devoted servant of the gods whose healing hands and sacred prayers provided solace to those in need, bolstering the spirits of their comrades in the face of adversity.")
while True:
    Menu = str(input("Please choose a mighty character to wield; Paladin, Wizard, Cleric: ")).lower()
    if Menu == "cleric":
        print("You have chosen the brave [CLERIC NAME], Strength: Healing, Weakness: Damage")
        break
    elif Menu == "paladin":
        print("You have chosen the mighty [PALADIN NAME], Strength: Damage, Weakness: Healing")
        break
    elif Menu == "wizard":
        print("You have chosen the intelligent [WIZARD NAME], Strength: Healing, Damage Weakness: Extended cooldown ")
        break
    else:
        print("Please choose an active charater to wield!")

print("Be brazen, you lead on a trechourous path.")
'''
Inventory = {"Slot 1":"Healing" , "Slot 2":"Damage Buff", "Slot 3":"Tradable Items", "Slot 4": "Collectibles"}
print(Inventory)
'''
Healing = 6
if Healing >= 6:
    print("You are at full health!",Paladin_Health+50)

Damaged = 6       
if Damaged >= 6:
    print("Health is now!",Paladin_Health-50)


Stage1 = print("Welcome to the Mountains")
print("Objective: Get pass Goblins")
if Dice == str(int("Enter a number")):
    elif Dice >= 6:
        print("Sneak Pass")
    elif Dice <= 6:
        print("Fight")
    elif Dice == 6:
        print("Trade")

Stage2 = print("Congurlations Welcome to the Cave")
print("Objective: Get pass Gargoyle")
if Dice = str(int("Enter a number"))
elif Dice > 6:
    print("Sneak Pass")
elif Dice < 6:
    print("Fight")
elif Dice == 6:
    print("Trade")



Stage3 = print("Welcone to the Trade Center")
print("Trade and add to your Inventory")
print("Trade for Health and Damage")
Inventory["Slot 1 "] = 
print(Inventory)


Stage4 = print("Congurlations Welcome to the Castle")
print("Objective: FIGHT DRAGON!")
if Dice = str(int("Enter a number"))
elif Dice < 6:
    print("Fight")
elif Dice == 6:
    print("Trade")


WIN = print("VICTIORY! THE DRAGON HAS BEEN SLAYED AND THE KINGDOM IS SAVED")
print("THANK YOU FOR PLAYING")

