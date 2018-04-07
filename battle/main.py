from classes.game import Person, bcolors
from classes.magic import Spell
from classes.inventory import Item
import random

#Create Black Magic variables: name, cost, dmg, type
fire = Spell("Fire", 25, 600, "black")
thunder = Spell("Thunder", 25, 600, "black")
blizzard = Spell("Blizzard", 25, 600, "black")
meteor = Spell("Meteor", 40, 1200, "black")
quake = Spell("Quake", 14, 140, "black")
diarrhea = Spell("diarrhea", 14, 140, "black")
farts = Spell("farts", 14, 140, "black")
noTweeets = Spell("noTweeets", 14, 731, "black")
bearClaws = Spell("bearClaws", 14, 396, "black")
turdSling = Spell("turdSling", 14, 600, "black")


#Create White Magic
cure = Spell("Cure", 25, 620, "white")
cura = Spell("Cura", 32, 1500, "white")

#Create some Items
potion = Item("Potion", "potion", "Heals 50 HP", 50)
hipotion = Item("Hi-Potion", "potion", "Heals 100 HP", 100)
superpotion = Item("Super Potion", "potion", "Heals 1000 HP", 1000)
elixer = Item("Elixer", "elixer", "Fully restore HP/MP of one party member", 9999)
hielixer = Item("MegaElixer", "elixer", "Fully restores party's HP/MP", 9999)

grenade = Item("Grenade", "attack", "Deals 500 damage", 500)


player_spells = [fire, thunder, blizzard, meteor, cure, cura, diarrhea, farts, noTweeets, bearClaws, turdSling]
player_items = [{"item": potion, "quantity": 15},
                {"item": hipotion, "quantity": 5},
                {"item": superpotion, "quantity": 5},
                {"item": elixer, "quantity": 5},
                {"item": hielixer, "quantity": 2},
                {"item": grenade, "quantity": 5}]

#Instantiate People
player1 = Person("Jhona:", 3260, 132, 300, 34, player_spells, player_items)
player2 = Person("Gabi: ", 4160, 188, 311, 34, player_spells, player_items)
player3 = Person("Dad: ", 3089, 288, 60, 34, player_spells, player_items)

enemy1 =  Person("KingPin:", 1250, 130, 560, 325, [], [])
enemy2 =  Person("Trump:  ", 11200, 701, 525, 25, [], [])
enemy3 =  Person("TheHand:", 1250, 130, 560, 325, [], [])

players = [player1, player2, player3]
enemies = [enemy1, enemy2, enemy3]

pedaling = True
i = 0

print(bcolors.FAIL + bcolors.BOLD + "AN ENEMY ATTACKS!" + bcolors.ENDC)
#print("The enemy attacks")


while pedaling:
    print("===================")

    print("\n\n")
    print("NAME                  HP                                    MP")
    for player in players:
        player.get_stats()

    print("\n")

    for enemy in enemies:
        enemy.get_enemy_stats()

    for player in players:

        player.choose_action()
        choice = input("    Choose action:")
        if choice == "":
            continue

        index = int(choice) - 1

        #print("You chose", player.get_spell_name(int(index)))

        if index == 0:
            dmg = player1.generate_damage()
            enemy = player.choose_target(enemies)

            enemies[enemy].take_damage(dmg)
            print("You attacked" + enemies[enemy].name + "for", dmg, "points of damage")
        elif index == 1:
            player.choose_magic()
            magic_choice = int(input("    Choose magic: ")) - 1

            if magic_choice == -1:
                continue

            spell = player.magic[magic_choice]
            magic_dmg = player.generate_damage()

            current_mp = player.get_mp()

            if spell.cost > current_mp:
                print(bcolors.FAIL + "\nNot enough MP\n" + bcolors.ENDC)
                continue

            player.reduce_mp(spell.cost)

            if spell.type == "white":
                player.heal(magic_dmg)
                print(bcolors.OKBLUE + "\n" + spell.name
                      + " heals for", str(magic_dmg),
                      "HP." + bcolors.ENDC)
            elif spell.type == "black":
                enemy = player.choose_target(enemies)

                enemies[enemy].take_damage(magic_dmg)

                print(bcolors.OKBLUE + "\n" + spell.name + " deals", str(magic_dmg), "points of damage to" + enemies[enemy].name + bcolors.ENDC)
        elif index == 2:
            player.choose_item()
            item_choice = int(input("    Choose item: ")) - 1

            if item_choice == -1:
                continue

            item = player.items[item_choice]["item"]

            if player.items[item_choice]["quantity"] == 0:
                print(bcolors.FAIL + "\n" + "None left..."
                      + bcolors.ENDC)
                continue

            player.items[item_choice]["quantity"] -= 1

            if item.type == "potion":
                player.heal(item.prop)
                print(bcolors.OKGREEN + "\n" +
                      item.name + " heals for", str(item.prop),
                      "HP" + bcolors.ENDC)
            elif item.type == "elixer":

                if item.name == "MegaElixer":
                    for i in players:
                        i.hp = i.maxhp
                        i.mp = i.maxmp
                else:
                    player.hp = player.maxhp
                    player.mp = player.maxmp
                print(bcolors.OKGREEN + "\n" + item.name +
                      " fully restores HP/MP" + bcolors.ENDC)
            elif item.type == "attack":

                enemy = player.choose_target(enemies)

                enemies[enemy].take_damage(item.prop)

                print(bcolors.FAIL + "\n" + item.name +
                      " deals", str(item.prop), "points of damage to" + enemies[enemy].name + bcolors.ENDC)


    enemy_choice = 1
    target = random.randrange(0, 3)
    enemy_dmg = enemies[0].generate_damage()

    players[target].take_damage(enemy_dmg)
    print("\nEnemy attacks for", enemy_dmg)

    if enemies[0].get_hp() == 0:
        print(bcolors.OKGREEN + "You win!" + bcolors.ENDC)
        pedaling = False
    elif player.get_hp() == 0:
        print(bcolors.FAIL + "Your enemy has defeated you!" + bcolors.ENDC)
        pedaling = False
