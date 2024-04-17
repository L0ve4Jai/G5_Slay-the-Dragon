print("Welcome to Slay The Dragon™!")
print("In a realm shrouded in the mists of legend, the mighty kingdom of [KINGDOM NAME] once reigned supreme, its borders guarded by the valor of its knights and the wisdom of its sovereign, [KING NAME]. Yet, under the cloak of night, a shadow darker than any before descended upon the land. From the depths of ancient lore emerged [DRAGON NAME], a creature of fire and fury, whose very name struck fear into the hearts of all who heard it. Whispers of the dragon's rampage spread like wildfire, challenging the very foundation of the kingdom's strength. But amidst the chaos, three heroes emerged, their resolve unyielding in the face of insurmountable odds. Driven by a steadfast courage, they vowed to ascend the treacherous peaks of the forbidden mountain where the dragon dwelled, First among them was [PALADIN NAME], a stalwart defender whose unwavering faith in righteousness served as a beacon of hope amidst the encroaching shadows. Alongside the paladin strode [WIZARD NAME], a master of arcane arts whose intellect and mastery of magic were matched only by their unyielding determination to protect the realm from all manner of arcane threats. Completing the trio was [CLERIC NAME], a devoted servant of the gods whose healing hands and sacred prayers provided solace to those in need, bolstering the spirits of their comrades in the face of adversity.")
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
print(player_list)
