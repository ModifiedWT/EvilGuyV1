import sys
import time
import random
import os

run = True
menu = True
play = False
rules = False
key = False
Fight = False
Standing = True
buy = False
speak = False
boss = False
defeated = False
map = 0
boss1 = False
sword = False
rest1 = False
q = False
r = False
school = False

HP = 500
MAXHP = HP
ATK = 500
pot = 1
elix = 1
gold = 10
x = 0
y = 0

def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.1)

map0 = [["bunny plains", "bunny plains", "forest", "mountain", "forest", "plains", "cave"],
       ["forest", "forest", "magic forest", "forest", "mountain", "mountain", "hills"], 
       ["forest", "forest", "bridge", "plains", "bunny plains", "hills", "mountain"],
       ["plains", "shop", "town", "mayor", "plains", "hills", "mountain"],
       ["plains", "fields", "fields", "plains", "hills", "mountain", "mountain"]]

map1 = [["stalactites", "stalactites", "rocks", "rocks", "rocks", "rocks", "hole"],
        ["rocks", "rocks", "gravel", "gravel", "gravel", "gravel", "gravel"],
        ["gravel", "deep", "townofzazarm", "knight", "inn", "shop1", "qwerty"],
        ["deep", "deep", "deep", "pentagram", "deep", "deep", "deep", "deep"],
        ["deep", "deep", "gravel", "gravel", "deep", "rocks", "stalactites"],
        ["gravel", "deep", "rocks", "rocks", "gravel", "deep", "rocks"]
        ]

map2 = [["path", "path", "path", "path", "path", "path", "path", "path", "path", "path", "path"],
        ["hills", "hills", "path", "path", "gravel", "gravel", "gravel", "river", "lake", "lake", "lake"],
        ["plains", "forest", "path", "forest", "ruins", "forest", "mountain", "river", "lake", "lake", "lake"],
        ["plains", "hills", "forest", "path", "deep", "deep", "mountain", "mountain", "plains", "bunny plains", "bunny plains"],
        ["hills", "hills", "path", "path", "deep", "rocks", "mountain", "river", "ruins", "bunny plains", "bunny plains"],
        ["hills", "hills", "path", "path", "gravel", "gravel", "mountain", "gravel", "rocks", "hills", "hills"],
        ["hills", "plains", "path", "path", "rocks", "congress", "hills", "bridge", "inn", "gravel", "rocks"],
        ["hills", "", "path", "path", "hills", "hills", "rocks", "rocks", "gravel", "mountain", "river"],
        ["school", "deep", "path", "path", "river", "plains", "hills", "rocks", "hills", "mountain", "river"],
        ["deep", "rocks", "path", "path", "river", "plains", "plains", "ruins", "mountain", "river", "river"],
        ["valve", "forest", "path", "path", "river", "forest", "forest", "bunny plains", "mountain", "river", "river"]
        ]

y_len = len(map0)-1 or len(map1)-1
x_len = len(map0[0])-1 or len(map1[0])-1

biom = {
    "plains": {
    "t": "PLAINS",
    "e": True
    },
    "bunny plains": {
    "t": "BUNNY PLAINS",
    "e": True
    },
    "forest": {
    "t": "FOREST",
    "e": True
    },
    "mountain": {
    "t": "MOUNTAIN",
    "e": False
    },
    "cave": {
    "t": "CAVE",
    "e": True
    },
    "fields": {
    "t": "FIELDS",
    "e": True
    },
    "shop": {
    "t": "BARGINS SHOP",
    "e": False
    },
    "town": {
    "t": "THE TOWN OF AZMARIN",
    "e": False
    },
    "mayor": {
    "t": "MAYOR",
    "e": False
    },
    "magic forest": {
    "t": "MAGIC FOREST",
    "e": True
    },
    "hills": {
    "t": "HILLS",
    "e": False
    },
    "bridge": {
    "t": "BRIDGE",
    "e": True
    },
    "stalactites": {
    "t": "STALACTITES",
    "e": True
    },
    "rocks": {
    "t": "BOLDERS",
    "e": True
    },
    "hole": {
    "t": "INFINITY HOLE",
    "e": False
    },
    "gravel": {
    "t": "GRAVEL",
    "e": True
    },
    "deep": {
    "t": "DEEP",
    "e": True
    },
    "townofzazarm": {
    "t": "TOWN OF ZAZARM",
    "e": False
    },
    "knight": {
    "t": "KNIGHT",
    "e": False
    },
    "inn": {
    "t": "INN",
    "e": False
    },
    "shop1": {
    "t": "SHOP OF TREY",
    "e": False
    },
    "qwerty": {
    "t": "QWERTY",
    "e": False
    },
    "pentagram": {
    "t": "PENTAGRAM",
    "e": False
    },
    "school": {
    "t": "ABANDONED SCHOOL",
    "e": False
    },
    "congress": {
    "t": "CONGRESS HALL",
    "e": False
    },
    "path": {
    "t": "A PATH",
    "e": True
    },
    "valve": {
    "t": "A VALVE",
    "e": False
    },
    "river": {
    "t": "A RIVER",
    "e": True
    },
    "lake": {
    "t": "A LAKE",
    "e": True
    },
    "ruins": {
    "t": "SOME RUINS",
    "e": True
    }


}

e_list = ["Goblin", "Orc", "Slime", "Mutant Rabbit", "Bear", "Demon", "CockRoacher", "Golem", "Mimic", "Wolf", "Possesed Child", "Mountain Lion", "Giant"]

mobs = {
    "Goblin": {
    "hp": 15,
    "at": 3,
    "go": 8
    },
    "Orc": {
    "hp": 25,
    "at": 5,
    "go": 18
    },
    "Slime": {
    "hp": 30,
    "at": 4,
    "go": 5
    },
    "Mutant Rabbit": {
    "hp": 25,
    "at": 6,
    "go": 10
    },
    "Damned Knight": {
    "hp": 200,
    "at": 20,
    "go": 4
    },
    "Bear": {
    "hp": 30,
    "at": 20,
    "go": 5
    },
    "Demon": {
    "hp": 40,
    "at": 5,
    "go": 4
    },
    "CockRoacher": {
    "hp": 20,
    "at": 8,
    "go": 50
    },
    "Satan": {
    "hp": 400,
    "at": 30,
    "go": 4
    },
    "Golem": {
    "hp": 60,
    "at": 12,
    "go": 20
    },
    "Mimic": {
    "hp": 58,
    "at": 8,
    "go": 20
    },
    "Wolf": {
    "hp": 35,
    "at": 15,
    "go": 60
    },
    "Possesed Child": {
    "hp": 40,
    "at": 16,
    "go": 20
    },
    "Mountain Lion": {
    "hp": 55,
    "at": 12,
    "go": 10
    },
    "Giant": {
    "hp": 100,
    "at": 15,
    "go": 13
    },
}


current_title = map0[y][x] or map1[y][x]
print(current_title)
name_of_title = biom[current_title]["t"]
print(name_of_title)
enemy_title = biom[current_title]["e"]
print(enemy_title)

def clear():
    #os.system('cls')
    print("\n"*500)

def draw():
    print("xX----------------------Xx")

def heal(amount):
    global HP, MAXHP
    HP = int(HP)
    if HP + amount < MAXHP:
        HP += amount
    else:
        HP = MAXHP
    print(name + "'s HP refilled to " + str(HP) + "!")
    time.sleep(1.5)

def shop1():
    global buy, gold, pot, elix, ATK, MAXHP
    ATK = int(ATK)
    while buy:
        clear()
        draw()
        print("Welcome to The Shop Traveler!")
        draw()
        print("GOLD: " + str(gold))
        print("POTIONS: " + str(pot))
        print("ELIXIRS: " + str(elix))
        print("ATK: " + str(ATK))
        draw()
        print("1 - BUY ELIXIR (50HP) - 10 GOLD")
        print("2 - ARMOR UPGRADE! (+ 50 Health) - 50 GOLD")
        print("3 - Sword GEMS! (+ 50 ATK) - 200 GOLD")
        print("4 - LEAVE")
        draw()

        choice = input("_> ")


        if choice == "1":
            if gold >= 10:
                elix += 1
                gold -= 10
                print("# YOU BOUGHT ELIXIR!")
                time.sleep(1.5)
            else:
                print("# NOT ENOUGH GOLD!")
                print("> ")
                time.sleep(1.5)
        elif choice == "2":
            if gold >= 30:
                MAXHP += 50
                gold -= 30
                print("# YOU'VE GOTTEN STRONGER ARMOR!")
                time.sleep(1.5)
            else:
                print("# NOT ENOUGH GOLD!")
                print("> ")
                time.sleep(1.5)
        elif choice == "3":
            if gold >= 200:
                ATK += 50
                gold -= 200
                print("# You Made Your Sword Shiny!")
                time.sleep(1.5)
            else:
                print("# NOT ENOUGH GOLD")
                print("> ")
        elif choice == "4":
            buy = False

def shop():
    global buy, gold, pot, elix, ATK, MAXHP
    ATK = int(ATK)
    while buy:
        clear()
        draw()
        print("Welcome to The Shop Traveler!")
        draw()
        print("GOLD: " + str(gold))
        print("POTIONS: " + str(pot))
        print("ELIXIRS: " + str(elix))
        print("ATK: " + str(ATK))
        draw()
        print("1 - BUY POTION (30 HP) - 5 GOLD")
        print("2 - BUY ELIXIR (50HP) - 10 GOLD")
        print("3 - UPGRADE SWORD (+4 ATK) - 15 GOLD")
        print("4 - ARMOR UPGRADE! (+ 50 Health) - 50 GOLD")
        print("5 - LEAVE")
        draw()

        choice = input("_> ")

        if choice == "1":
            if gold >= 5:
                pot += 1
                gold -= 5
                print("# YOU BOUGHT POTION!")
            else:
                print("# NOT ENOUGH GOLD!")
                print("> ")
        elif choice == "2":
            if gold >= 10:
                elix += 1
                gold -= 10
                print("# YOU BOUGHT ELIXIR!")
                time.sleep(1.5)
            else:
                print("# NOT ENOUGH GOLD!")
                print("> ")
                time.sleep(1.5)
        elif choice == "3":
            if gold >= 15:
                ATK += 4
                gold -= 15
                print("# YOU BOUGHT A SWORD UPGRADE!")
                time.sleep(1.5)
            else:
                print("# NOT ENOUGH GOLD!")
                print("> ")
                time.sleep(1.5)
        elif choice == "4":
            if gold >= 30:
                MAXHP += 50
                gold -= 30
                print("# YOU'VE GOTTEN STRONGER ARMOR!")
                time.sleep(1.5)
            else:
                print("# NOT ENOUGH GOLD!")
                print("> ")
                time.sleep(1.5)
        elif choice == "5":
            buy = False

def save():
    global HP,ATK,pot,elix,gold,x,y,key,MAXHP
    list = [
        name,
        str(HP),
        str(ATK),
        str(pot),
        str(elix),
        str(gold),
        str(x),
        str(y),
        str(key),
        str(MAXHP)
    ]

    f = open("load.txt", "w")

    for item in list:
        f.write(item + "\n")
    f.close()

def penta():
    global boss1, fight, map, sword,r
    clear()
    draw()
    print_slow("You Find Yourself Standing In The Middle of a Giant Pentagram...Your Body Shakes Violently...A Voice Wispears Out to You...")
    if r:
        if sword == False:
            print("UNKNOWN: 'You Must Find The Sword of Zazarm'...")
        elif sword == True:
            print("I see...I Guess Ill Summon The Devil...")
            fight = True
            boss1 = True
            battle()
        print("1 - LEAVE")
        choice = input("_> ")

        if choice == "1":
            pass

def rest():
    global rest1, HP, MAXHP, gold
    while rest1:
        clear()
        draw()
        print("Welcome To The INN!")
        draw()
        print("GOLD: " + str(gold))
        draw()
        print("1 - Take a Rest On Hard Bed - 10 Gold (+20 HP)")
        print("2 - Take a Rest On Light Bed - 20 Gold (+40 HP)")
        print("3 - Take a Rest On Dreamy Bed - 50 Gold (MAXHP)")
        print("4 - LEAVE")
        draw()
        choice = input("_> ")
        if choice == "1":
            if gold >= 10:
                print("# You Take a Nap On The Hard Bed")
                print("# + 20 HP")
                gold -= 10
                HP += 20
            else:
                print("# NOT ENOUGH GOLD!")
                print("> ")
        elif choice == "2":
            if gold >= 20:
                print("# You Take a Nap on the Light Bed!")
                gold -= 20
                print("# + 40 HP")
                HP += 40
                time.sleep(1.5)
            else:
                print("# NOT ENOUGH GOLD!")
                print("> ")
                time.sleep(1.5)
        elif choice == "3":
            if gold >= 50:
                print("# You Take a Nap On the Dreamy Bed!")
                gold -= 50
                HP += MAXHP
                print("# MAXHP has Been Restored!")
                time.sleep(1.5)
            else:
                print("# NOT ENOUGH GOLD!")
                print("> ")
                time.sleep(1.5)
        elif choice == "4":
            rest1 = False

def qwerty():
    global ATK, sword, q
    while q:
        print("Hello " + name + "!")
        print("My Days of Adventuring Are Over... There is One Thing Ive always Wanted to do, But My Old Body Can't...I Need You To Defeat Satan For me...With the Sword of Zazarm...May God Give You Power...")
        print("# You Need At Least 60 ATK to get the sword!")
        if ATK >= 60:
            print("Heres The Sword...Keep it")
            sword = True
        else:
            print("Your Not Strong Enough, Hurry I Can feel Myself Slipping...")
            q = False
        print("1 - LEAVE")
        choice = input("_> ")

        if choice == "1":
            q = False

def mayor():
    global key, speak, ATK, MAXHP, defeated
    
    while speak:
        clear()
        draw()
        print("Hello " + name)
        if int(ATK) < 10 and int(MAXHP) <= 200:
            print("Im Sorry But I Can't Have a Child Like You Running Around Killing Damned Knights, Come Back When Your Stronger! Get Better Armor and Swords!")
        else:
            print("You've Acctually OutDone Yourself! Take The Key But Be Carful! The Damned Knight is Powerful!")
            key = True

            draw()
            print("1 - LEAVE")
            draw()

            choice = input("_> ")

            if choice == "1":
                speak = False

def cave():
    global fight, boss, map
    clear()
    draw()
    print_slow("You Enter a Spooky Cave, and a Door Lies ahead, With a KeyHole...\n")      
    draw()
    if key:
        print("1 - USE KEY")
    print("2 - TURN BACK")
    draw()

    choice = input("_> ")

    if choice == "1":
        if key:
            fight = True
            boss = True
            map = 1
            battle()
    elif choice == "2":
        boss = False

def battle():
    
    global fight, play, run, HP, pot, elix, gold, boss, ATK, defeated, boss1, key, map
    HP = int(HP)

    if key:
        if boss is True:
            enemy = "Damned Knight"    
        elif boss1 is True:
            enemy = "Satan"
        else:
           enemy = random.choice(e_list) 
    else:
         enemy = random.choice(e_list)
    hp = mobs[enemy]["hp"]
    hpmax = hp
    atk = mobs[enemy]["at"]
    g = mobs[enemy]["go"]

    while fight:
        clear()
        draw()
        print("Defeat the " + enemy + "!")
        draw()
        print(enemy + "'s HP: " + str(hp) + "/" + str(hpmax))
        print(name + "'s HP: " + str(HP) + "/" + str(MAXHP))
        print("POTIONS: " + str(pot))
        print("ELIXIR: " + str(elix))
        draw()
        print("1 - ATTACK")
        if pot > 0:
            print("2 - USE POTION (30 HP)")
        if elix > 0:
            print("3 - USE ELIXIR (50 HP)")
        draw()

        choice = input("_> ")
        
        ATK = int(ATK)
        if choice == "1":
            hp -= ATK
            print(name + " dealt " + str(ATK) + " damage to " + enemy)
            time.sleep(1.5)
            if hp > 0:
                HP -= atk
                print(enemy + " dealt " + str(atk) + " damage to " + name)
                time.sleep(1.5)            
            print("> ")
        elif choice == "2":
            if pot > 0:
                pot -= 1
                heal(30)
                HP -= atk
                print(enemy + " dealt " + str(atk) + " damage to " + name)
                time.sleep(1.5)
                print("> ")
            else:
                print("No Potions!")
                time.sleep(1.5)
                print("> ")
                
        elif choice == "3":
            if elix > 0:
                elix -= 1
                heal(50)
                HP -= atk
                print(enemy + " dealt " + str(atk) + " damage to " + name)
                time.sleep(1.5)
                print("> ")
            else:
                print("No Elixirs!")
                time.sleep(1.5)
                print("> ")

        if HP <= 0:
            print(enemy + " defeated " + name + "...")
            draw()
            fight = False
            play = False
            run = False
            print("# GAME OVER #")
            print("> ")
        if hp <= 0:
            print(name + " defeated the " + enemy + "!")
            draw()
            fight = False
            gold += g
            print("You've Found Some Gold!")
            time.sleep(1.5)
            if random.randint(0,100) < 30:
                pot += 1
                print("You Found a Potion!")
                print("> ")
                time.sleep(1.5)
            if enemy == "Damned Knight":
                draw()
                print_slow("You Jump Up and Strike The Damned Knight, Wondering Why This Was so Easy...")
                time.sleep(3.5)
                draw()
                boss = False
                defeated = True
            elif enemy == "Satan":
                draw()
                print_slow("BY Killing The Lord of The Dead You Realie You Reverse Everything That had Happened to this cruel World...Your Sent backwards into time.")
                map = 2
            clear()

def school():
    global school
    while school:
        print_slow("You Enter a school, You Hear Metal Scrapping on a WhiteBoard...")
        #Wisper Sound effect here :D


while run:
    while menu:
        clear()
        draw()
        print("1. NEW GAME")
        print("2. LOAD GAME")
        print("3. RULES")
        print("4. QUIT GAME")
        draw()

        if rules:
            draw()
            print_slow("Made By ModifiedWT! The Rules are To Not Break My Game! And Report any Bugs To ME :D ENJOY!!\n")
            time.sleep(2)
            rules = False
            choice = ""
            print("> \n")
            draw()
        else:
            choice = input("_> ")

        if choice == "1":
            clear()
            draw()
            print_slow("# There was Once a Big Conflict Between Heaven and Hell...Long Ago a Person Named Avrun, Disrupting The Force of Balance, by Summoning Demons and Ghouls...\n")
            clear()
            name = input("# Whats Our Hero's Name? ")
            menu = False
            play = True
            map = 0
            draw()
        elif choice == "2":
            try:
               f = open("load.txt", "r")
               load_list = f.readlines()
               if len(load_list) == 10:
                  name = load_list[0][:-1]
                  HP = load_list[1][:-1]
                  ATK = load_list[2][:-1]
                  pot = int(load_list[3][:-1])
                  elix = int(load_list[4][:-1])
                  gold = int(load_list[5][:-1])
                  x = int(load_list[6][:-1])
                  y = int(load_list[7][:-1])
                  key = bool(load_list[8][:-1])
                  MAXHP = int(load_list[9][:-1])
                  clear()
                  draw()
                  print("Welcome Back, " + name + "!")
                  print("> \n")
                  draw()
                  time.sleep(1.5)
                  menu = False
                  play = True
               else:
                   print("# CORRUPTED SAVE FILE!")
                   print("> \n")
                   time.sleep(1.5)
            except OSError:
                print("# No Loadable Save File!")
                print("> \n")
                time.sleep(1.5)
        elif choice == "3":
            rules = True
        elif choice == "4":
            sys.exit()
    while play:
        save() #autoSave
        clear()

        if not Standing:
            if defeated != True:
                if biom[map0[y][x]]["e"]:
                    if random.randint(0,100) <= 30:
                            fight = True
                            battle()
            else: 
                if biom[map1[y][x]]["e"]:
                    if random.randint(0,100) <= 30:
                            fight = True
                            battle()

        if play:
            if map == 0:
            
                draw()
                print("LOCATION: " + biom[map0[y][x]]["t"])
                draw()
                print("NAME: " + name)
                print("HP: " + str(HP) + "/" + str(MAXHP))
                print("ATK: " + str(ATK))
                print("POTIONS: " + str(pot))
                print("ELIXERS: " + str(elix))
                print("GOLD: " + str(gold))
                print("COORDS: ", x, y)
                draw()
                print("0 - SAVE AND QUIT")
                print("1 - NORTH")
                print("2 - EAST")
                print("3 - SOUTH")
                print("4 - WEST")
                print("5 - USE POTION (30 HP)")
                print("6 - USE ELIXIR (50 HP)")
                print("7 - ENTER/TALK")
                draw()
                dest = input("_> ")

                if dest == "0":
                    play = False
                    menu = True
                    save()
                elif dest == "1":
                    if y > 0:
                        y-= 1
                        Standing = False
                    else:
                        y = y_len
                elif dest == "2":
                    if x > 0:
                        x -= 1
                        Standing = False
                    else:
                        x = x_len
                    
                elif dest == "3":
                    if y < y_len:
                        y += 1
                        Standing = False
                    else:
                        y = 0
                elif dest == "4":
                    if x < x_len:
                        x += 1
                        Standing = False
                    else:
                        x = 0
                elif dest == "5":
                    if pot > 0:
                        pot -= 1
                        heal(30)
                        print("> ")
                    else:
                        print("No Potions!")
                        time.sleep(1.5)
                    print("> ")
                    standing = True
                elif dest == "6":
                    if elix > 0:
                        elix -= 1
                        heal(50)
                    else:
                        print("No Elixirs!")
                        time.sleep(1.5)
                    print("> ")
                    standing = True
                elif dest == "7":
                    if map0[y][x] == "shop":
                        buy = True
                        shop()
                    elif map0[y][x] == "mayor":
                        speak = True
                        mayor()
                    elif map0[y][x] == "cave":
                        boss = True
                        cave()
                else:
                    standing = True
            elif map == 1:
                    draw()
                    print("LOCATION: " + biom[map1[y][x]]["t"])
                    draw()
                    print("NAME: " + name)
                    print("HP: " + str(HP) + "/" + str(MAXHP))
                    print("ATK: " + str(ATK))
                    print("POTIONS: " + str(pot))
                    print("ELIXERS: " + str(elix))
                    print("GOLD: " + str(gold))
                    print("COORDS: ", x, y)
                    draw()
                    print("0 - SAVE AND QUIT")
                    print("1 - NORTH")
                    print("2 - EAST")
                    print("3 - SOUTH")
                    print("4 - WEST")
                    print("5 - USE POTION (30 HP)")
                    print("6 - USE ELIXIR (50 HP)")
                    print("7 - ENTER/TALK")
                    draw()
                    dest = input("_> ")

                    if dest == "0":
                        play = False
                        menu = True
                        save()
                    elif dest == "1":
                        if y > 0:
                            y-= 1
                            Standing = False
                        else:
                            y = y_len
                    elif dest == "2":
                        if x > 0:
                            x -= 1
                            Standing = False
                        else:
                            x = x_len
                        
                    elif dest == "3":
                        if y < y_len:
                            y += 1
                            Standing = False
                        else:
                            y = 0
                    elif dest == "4":
                        if x < x_len:
                            x += 1
                            Standing = False
                        else:
                            x = 0
                    elif dest == "5":
                        if pot > 0:
                            pot -= 1
                            heal(30)
                            print("> ")
                        else:
                            print_slow("No Potions!")
                            time.sleep(1.5)
                        print("> ")
                        standing = True
                    elif dest == "6":
                        if elix > 0:
                            elix -= 1
                            heal(50)
                        else:
                            print("No Elixirs!")
                            time.sleep(1.5)
                        print("> ")
                        standing = True
                    elif dest == "7":
                        if map1[y][x] == "pentagram":
                            r = True
                            penta()
                        elif map1[y][x] == "shop1":
                            buy = True
                            shop1()
                        elif map1[y][x] == "qwerty":
                            q = True
                            qwerty()
                        elif map1[y][x] == "inn":
                            rest1 = True
                            rest()
                        standing = True
            elif map == 2:
                draw()
                print("LOCATION: " + biom[map2[y][x]]["t"])
                draw()
                print("NAME: " + name)
                print("HP: " + str(HP) + "/" + str(MAXHP))
                print("ATK: " + str(ATK))
                print("POTIONS: " + str(pot))
                print("ELIXERS: " + str(elix))
                print("GOLD: " + str(gold))
                print("COORDS: ", x, y)
                draw()
                print("0 - SAVE AND QUIT")
                print("1 - NORTH")
                print("2 - EAST")
                print("3 - SOUTH")
                print("4 - WEST")
                print("5 - USE POTION (30 HP)")
                print("6 - USE ELIXIR (50 HP)")
                print("7 - ENTER/TALK")
                draw()
                dest = input("_> ")
                if dest == "0":
                    play = False
                    menu = True
                    save()
                elif dest == "1":
                    if y > 0:
                        y-= 1
                        Standing = False
                    else:
                        y = y_len
                elif dest == "2":
                    if x > 0:
                        x -= 1
                        Standing = False
                    else:
                        x = x_len
                        
                elif dest == "3":
                    if y < y_len:
                        y += 1
                        Standing = False
                    else:
                        y = 0
                elif dest == "4":
                    if x < x_len:
                        x += 1
                        Standing = False
                    else:
                        x = 0
                elif dest == "5":
                    if pot > 0:
                        pot -= 1
                        heal(30)
                        print("> ")
                    else:
                        print_slow("No Potions!")
                        time.sleep(1.5)
                    print("> ")
                    standing = True
                elif dest == "6":
                    if elix > 0:
                        elix -= 1
                        heal(50)
                    else:
                        print("No Elixirs!")
                        time.sleep(1.5)
                    print("> ")
                    standing = True
                elif dest == "7":
                    if map2[y][x] == "school":
                        school = True
                        school()
                    elif map2[y][x] == "congress":
                        pass
                    elif map2[y][x] == "inn":
                        rest1 = True
                        rest()
                    elif map2[y][x] == "valve":
                        pass
                    standing = True
