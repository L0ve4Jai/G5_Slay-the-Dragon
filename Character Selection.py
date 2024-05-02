Class characters:
 def __init__ (self, health, armor, attack1, attack2, attack3, spell1, spell2, spell3)
 self.health = health
 self. armor = armor
 self.attack1 = attack1
 self.attack2 = attack2 
 self.attack3 = attack3
 self.spell1 = spell1
 self.spell2 = spell2
 self.spell3 = spell3

Paladin = characters(20, 100, {"slash": 2*D_12()) + 6},{"stab", 2*D_(8)+2}, {"Pierce", D_10()+6}, {"divine_smite", 12+6}, {"healing_hand", D_12()+8}), {"Holy_blast", 2*D_12()}
Wizard = characters(16, 75, {"Shiv": D_8()) + 6},{"fireball", D_(12)+6}, {"eldrich_blast", D_12()+6}, {"lightning_bolt", D_10()+8}, {"Health_spell", D_12()+8}), {"necrotic_touch", 4*D_6()}
Cleric = characters(18, 85, {"hammer_strike": D_10()) + 6},{"shield_bash", D_(12)+6}, {"holy_spear", 2*D_12()+6}, {"lightning_bolt", D_10()+8}, {"Health_spell", D_12()+8}), {"Light_of_the_goddess", 4*D_8()}


from random import *
def D_20():
    a = randint(1, 20)
    print("A", a, "was rolled")
    return a 

def D_6():
    b = randint(1,6)
    print("A", b, "was rolled")
    return b 

def D_4():
    e = randint(1,4)
    print("A", e, "was rolled")

def D_12():
    c = randint(1,12)
    print("A", c, "was rolled")
    return c

def D_10():
    d = randint(1, 10)
    print("A", d, "was rolled") 
    return d


class enemies: 
    def __init__(self, health, enemy_armor, attack_1, attack_2, attack_3) :
        self.health = health
        self.enemy_armor = enemy_armor 
        self.attack_1 = attack_1
        self.attack_2 = attack_2
        self.attack_3 = attack_3

goblin = enemies(12, 15, {"smash": D_6()} , {"hit": D_4()}, {"bite": D_10()})

troll = enemies(30, 12, {"bash": D_12()}, {"club": D_10()}, {"chomp": D_10()})

print(troll.attack_3)
print("Welcome to Slay The Dragon™!")
print('''In a realm shrouded in the mists of legend, the mighty kingdom of Vordania once reigned supreme, its borders guarded by the valor of its knights and the wisdom of its sovereign, King Soloman.
Yet, under the cloak of night, a shadow darker than any before descended upon the land.
From the depths of ancient lore emerged Emberaxus, a creature of fire and fury, whose very name struck fear into the hearts of all who heard it. 
Whispers of the dragon's rampage spread like wildfire, challenging the very foundation of the kingdom's strength.
But amidst the chaos, three heroes emerged, their resolve unyielding in the face of insurmountable odds. 
Driven by a steadfast courage, they vowed to ascend the treacherous peaks of the forbidden mountain where the dragon dwelled, First among them was Wolfram Dawnwatcher, a stalwart defender whose unwavering faith in righteousness served as a beacon of hope amidst the encroaching shadows. 
Alongside the paladin strode Adnos Weavemaster, a master of arcane arts whose intellect and mastery of magic were matched only by their unyielding determination to protect the realm from all manner of arcane threats.
Completing the trio was Nicolene Lylet, a devoted servant of the gods whose healing hands and sacred prayers provided solace to those in need, bolstering the spirits of their comrades in the face of adversity.''')
player_list = {}
def choose_character():
    available_classes = ["paladin", "wizard", "cleric"]
    for i in range(1, 4):
        while True:
            player_input = input(f"Player {i}, please choose your character: ").lower()
            if player_input in available_classes:
                player_list["Player ", i] = player_input
                available_classes.remove(player_input)
                print("Player ",i, "has chosen the ",player_input.title())
                print("classes left:", available_classes )
                break
            else:
                print("Please choose a valid class that has not been taken.")
                continue
    return player_list
player_choices = choose_character()
print("Character selection complete.")



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
Inventory = {"Slot1": "Healing" , "Slot2": "Damage Buff", "Slot3": "Tradable Items", "Slot4": "Collectibles"}
print(Inventory)
Inventory["Slot1"]  = {"Weapon"}
del Inventory["Slot2"]
Inventory["Slot5"]  = {"Sword"}
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
