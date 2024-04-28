Paladin_Health = 200
Cleric_Health = 100
Wizard_Health = 150
Goblin_Health = 300
Dragon_Health = 1000
Gargoyle_Health = 500
Dice_one = 10
Dice_two = "Fight"


print("Welcome to Slay The Dragon™!")
print('''In a realm shrouded in the mists of legend, the mighty kingdom of Vordania once reigned supreme, its borders guarded by the valor of its knights and the wisdom of its sovereign, King Soloman.
Yet, under the cloak of night, a shadow darker than any before descended upon the land.
From the depths of ancient lore emerged Emberaxus, a creature of fire and fury, whose very name struck fear into the hearts of all who heard it. 
Whispers of the dragon's rampage spread like wildfire, challenging the very foundation of the kingdom's strength.
But amidst the chaos, three heroes emerged, their resolve unyielding in the face of insurmountable odds. 
Driven by a steadfast courage, they vowed to ascend the treacherous peaks of the forbidden mountain where the dragon dwelled, First among them was Wolfram Dawnwatcher, a stalwart defender whose unwavering faith in righteousness served as a beacon of hope amidst the encroaching shadows. 
Alongside the paladin strode Adnos Weavemaster, a master of arcane arts whose intellect and mastery of magic were matched only by their unyielding determination to protect the realm from all manner of arcane threats.
Completing the trio was Nicolene Lylet, a devoted servant of the gods whose healing hands and sacred prayers provided solace to those in need, bolstering the spirits of their comrades in the face of adversity.''')
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



Weapons = {" Knight's Arsenal":"Sword/Spear", "Wizard's Arsenal":"Staff and Spells(Healing and Damage)","Paladin's Arsenal": " A bow and arrow, along with the healing and damage remedies."}

print(Weapons)


print("Your are at full health!",Paladin_Health,Cleric_Health,Wizard_Health)



Stage1 = print("Welcome to the Mountains")
print("Objective: Get pass Goblins")
if Dice_one == 10:
    print("Fight or Sneak Pass")
elif Dice_two == "fight":
    print("Attack")
elif Dice_one < 7:
    print(Goblin_Health-100)
elif Dice_one > 13:
    print(Goblin_Health-300)
elif Dice_one < 9:
    print(Paladin_Health)
elif Dice_one > 18:
    print(Cleric_Health)
elif Dice_one == 14:
    print(Dragon_Health-800)

else: Dice_two == "Sneak"
print("Goblins defeated")



Stage2 = print("Congurlations Welcome to the Cave")
print("Objective: Get pass Gargoyle")
if Dice_one == 10:
    print("Fight or Sneak Pass")
elif Dice_two == "fight":
    print("Attack")
elif Dice_one < 7:
    print(Gargoyle_Health-100)
elif Dice_one > 13:
    print(Gargoyle_Health-300)
elif Dice_one < 9:
    print(Gargoyle_Health)
elif Dice_one > 18:
    print(Gargoyle_Health)
elif Dice_one == 14:
    print(Gargoyle_Health-800)

else: Dice_two == "Sneak"
print("Gargoyles defeated")






Stage3 = print("Welcone to the Trade Center")
print("Trade and add to your Inventory")
print("Trade for Health and Damage")
Inventory["Slot 1 "] = ("Enter a Weapon, Spell, or Healing Archetype")
print(Inventory)


Stage4 = print("Congurlations Welcome to the Castle")
print("Objective: FIGHT DRAGON!")
if Dice_one == 10:
    print("Fight or Sneak Pass")
elif Dice < 6:
    print("Fight")
elif Dice < 7:
    print(Dragon_Health-100)
elif Dice > 13:
    print(Dragon_Health-800)
elif Dice == 15:
    print(Dragon_Health-800)
elif Dice < 9:
    print(Paladin_Health)
elif Dice > 18:
    print(Cleric_Health)
elif Dice == 14:
    print(Dragon_Health-800)

    


WIN = print("VICTIORY! THE DRAGON HAS BEEN SLAYED AND THE KINGDOM IS SAVED")
print("THANK YOU FOR PLAYING")
