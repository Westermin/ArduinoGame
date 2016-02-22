import serial
import time
from GamerinoClasses import Player, Enemy

ser = serial.Serial(port='COM3', baudrate=9600)
character = Player(2000, 20, 0, 4, 0, 'Player')
goblin = Enemy(100, 1, 4, 8, 16, 'Goblin')
slime = Enemy(20, 8, 16, 40, 80, 'Slime')
orc = Enemy(800, 80, 160, 400, 800, 'Orc')
mobs_list = [goblin, slime, orc]
currentfight = 0
# The instructions
'''
print("""You have got 4 button on your gamepad. The 1. button is for an basic attack,
    By using the basic attack you will preform an attack on the current enemy you are against and add some mana
    to your mana bar, it will also charge up your charging.
    The charging works by each time you attack with an basic attack it add up in charge,
    the more you use the basic attack the more it charges. And at one point it release a critical attack
    on the current enemy.

    The 2. button is special attack than can only be used if enough mana is filled.

    The 3. button is block, block is used when you know the enemy is gonna use a charge, it's greatly recommended
    to know the pattern of an enemy cause when the enemy is charged up he can do a lot of damage.
    The block works by block half of the attack the enemy are preforming.

    The 4. Button is heal, you need mana to heal yourself but if you do, you will add 100 health to your current health
    """)
'''
i = 1
print("You are currently fighting a {}".format(mobs_list[currentfight].name))
messange = ser.read()
time.sleep(1)
print(messange)
while mobs_list[2].health >= 0:
    messange = ser.read()
    print(messange)
    if mobs_list[currentfight].health <= 0:
        currentfight += 1
    if character.currentcharge > character.charge:
        character.currentcharge = character.charge
    if "btnAttack" in messange and character.currentcharge >= 4:
        mobs_list[currentfight].health -= character.attack * 2
        print("You charged into {}'s stomach and ripped it out with a total damage of {}!".format(
            mobs_list[currentfight].name, character.attack * 2))
        character.currentcharge = 0
    elif "btnAttack" in messange and character.currentcharge < 4:
        mobs_list[currentfight].health -= character.attack
        character.health -= mobs_list[currentfight].attack
        character.mana += 2
        character.currentcharge += 1
        mobs_list[currentfight].currentcharge += 1
        print("You took damage {} from the {} and gave {} to the {}!".format(
            mobs_list[currentfight].attack,
            mobs_list[currentfight].name, character.attack, mobs_list[currentfight].name))
        print("Your health is {} and the {}'s health is {}".format(character.health,
                                                                   mobs_list[currentfight].name,
                                                                   mobs_list[currentfight].health))
        print("Charge is {} out of 4!".format(character.currentcharge))
        i = 0
    i += 1
    if "btnManaDamage" in messange and character.mana >= 4:
        mobs_list[currentfight].health -= character.attack * 4
        print("You shot lasers out from your eyes and dealt {}!".format(character.attack * 4))
        print("Your mana now is {}".format(character.mana))
        i = 0
        if character.mana < 4:
            print("You don't have enough mana!")
            i = 0

    if "btnBlock" in messange and character.mana >= 3:
        character.health -= mobs_list[currentfight].attack / 2
        character.mana -= 3
        mobs_list[currentfight].currentcharge += 1
        print("You blocked {0} damage from {1} but took {1} damage.".format(mobs_list[currentfight].name,
                                                                            mobs_list[currentfight].attack / 2))
        i = 0
    elif "btnBlock" in messange and character.mana < 3:
        print("You don't have enough mana!")
    if "btnHeal" in messange and character.mana >= 6:
        character.health += 100
        print("You flashed the monster with a flash so bright he was blind for 1 turn!")
        i = 0
    elif "btnHeal" in messange and character.mana < 6:
        print("You don't have enough mana!")
    if mobs_list[currentfight].health <= 0:
        print("You killed {}! after 5 mins of walking deeper into the cave you found a {}!".format(
            mobs_list[currentfight].name, mobs_list[currentfight + 1].name))
        currentfight += 1
        i = 1
