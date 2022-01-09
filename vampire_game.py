import time #added to enable pause

#bhawesh
#A text based dracula survival game

#possible answers
answer_A = ['A', 'a']
answer_B = ['B', 'b']
answer_C = ['C', 'c']
y = ['yes', 'Yes', 'y', 'Y']
n = ['no', 'No', 'n', 'N']




#story begins here
def intro():
    print('You wake up in front of a castle, you have no idea where you are or why you are here.'
    'You suddenly see a colony of bats fly away.' 'You turn back and see a vampire figure appear out of nowhere. You will:')
    print('''    A. Ask for direction.
    B. Run inside the castle.
    C. Run to the cave.''')
    choice = input('>>>  ')
    if choice in answer_A:
        print('\n Well you dont ask vampires for directions. \n\nRip')
        return "Gameover"
    elif choice in answer_B:
        return "castle"
    elif choice in answer_C:
        return "cave"
    else:
        print("Invalid input")
        time.sleep(1)
        intro()


def option_castle():
    print('You ran inside the castle and see a glass front cubbord with garlic inside.You hear the Vampire coming,''You will: ')
    print('''    A. Take the garllic to scare the vampire.
    B. Hide
    C. Escape from backdoor.''')
    choice = input('>>>  ')
    if choice in answer_A:
        print("The garlic did stopped the vampire but it did not stopped it's blood thirsty bats.\n\n RIP")
        return "Gameover"
    elif choice in answer_B:
        print("This is not hide n'seek \n\n RIP" )
        return "Gameover"
    elif choice in answer_C:
        return "village"
    else:
        print('Invalid input')
        time.sleep(1)
        option_castle()


def option_cave():
    print('You ran inside a dark cave, you were not sure if its a good idea or not but in there you see a shiny silver dagger.' 'Hurry bats are coming: ')
    print('''    A. You pick up the dagger and fight.
    B. You pick up the dagger and hide.
    C. You run.''')
    choice = input('>>>  ')
    if choice in answer_A:
        print('You picked the silver dagger and stood there like a fearsome warrior. The vampire attacked you but you were cunning and avoiding its attack stabbed the vampire right in its heart. Well done vampire slayer, you may live.')
        return "Gameover"
    elif choice in answer_B:
        print("Cowards don't get to fight and live. \n\n RIP")
        return "Gameover"
    elif choice in answer_C:
        return "village"
    else:
        print("Invalid input")
        time.sleep(1)
        option_cave()


def option_abdvilllage():
    print('You ran towards an abandoned village in the open. The bats are coming faster than before, you will: ')
    print('''    A. Hide 
    B. Pick a wood to stab the vampire
    C. Enter the cave''')
    choice = input('>>>  ')
    if choice in answer_A:
        print('You hid in a hut and well it worked, you were lucky and the sun rose killing the vampire. You were a coward but a lucky one.')
        return "Gameover"
    elif choice in answer_B:
        print("You were ready to stab the vampire with the wood but neither you were fast enough nor the wood was pointed enough. \n\n RIP")
        return "Gameover"
    elif choice in answer_C:
        return "cave"
    else:
        print('Invalid Input')
        time.sleep(1)
        option_abdvilllage()

def main_loop():
    state = "intro"

    while state != "end":
        if state == "intro":
            state = intro()
        elif state == "castle":
            state = option_castle()
        elif state == "village":
            state = option_abdvilllage()
        elif state == "cave":
            state = option_cave()
        elif state == "Gameover":
            again = input("\nDo you want to play again? (Y or n)").lower()
            if again in y:
                state = "intro"
            else:
                print('\nvery well')
                time.sleep(2)
                break

def play(): 
    start = input('Do you want to play? Y or N  ')
    if start in y:
        main_loop()
    elif start in n:
        print('very well')
        time.sleep(2)
    else:
        print('wrong input')
        time.sleep(2)
        play()

play()

#hello


