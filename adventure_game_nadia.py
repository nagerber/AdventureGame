import time
import random


def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(3)


def valid_input(prompt, option1, option2):
    while True:
        response = input(prompt).lower()
        if option1 in response:
            break
        elif option2 in response:
            break
        else:
            print_pause("Please try again")
    return response


def intro(characters_list, weapons_list):
    print_pause("\nYou find yourself standing in an open field,"
                " filled with grass and violet wildflowers.")
    print_pause("\nRumor has it that a " + characters_list + " is somewhere "
                "around here, and has been terrifying the nearby village.")
    print_pause("\nIn front of you is a creepy house.")
    print_pause("To your right is a very dark cave.")
    print_pause("\nIn your hand you hold your " + weapons_list + ".")


def give_choice(items, characters_list, weapons_list):
    print_pause("\nEnter 1 to knock on the door of the house.")
    print_pause("Enter 2 to peer into the cave.")
    response = valid_input("\nWhat would you like to do?"
                           "\nPlease enter 1 or 2\n",
                           "1", "2")
    if "1" in response:
        house(items, characters_list, weapons_list)
    elif "2" in response:
        cave(items, characters_list, weapons_list)


def fight_runaway(items, characters_list, weapons_list):
    response = valid_input("Would you like to (1) fight or (2) run away?"
                           " Please enter 1 or 2 \n",
                           "1", "2")
    if "1" in response:
        fight(items, characters_list, weapons_list)
    elif "2" in response:
        field(items, characters_list, weapons_list)


def fight(items, characters_list, weapons_list):
    print_pause("You do your best...")
    if "sword" in items:
        print_pause("As the " + characters_list + " moves to attack, "
                    "you unsheath your new sword.")
        print_pause("The Sword of Ogoroth shines brightly in your hand "
                    "as you brace yourself for the attack.")
        print_pause("But the " + characters_list + " takes one look at "
                    "your shiny new toy and runs away!")
        print_pause("You have rid the town of the " + characters_list + ". "
                    "You are victorious!")
        play_again()
    else:
        print_pause("...but your silly old " + weapons_list +
                    " is no match for the " + characters_list + ".")
        print_pause("You have been defeated!")
        print_pause("Soooo, sorry!")
        play_again()


def cave(items, characters_list, weapons_list):
    print_pause("You peer cautiously into the dark cave.")
    if "sword" in items:
        print_pause("You've been here before, and gotten all the good stuff."
                    "\nIt's just an empty cave now")
    else:
        print_pause("It turns out to be only a very small cave."
                    "\nYour eye catches a glint of metal behind a rock.")
        print_pause("\nYou have found the magical Sword of Ogoroth!"
                    "\nYou discard your silly old " + weapons_list +
                    " and take the sword with you.")
        items.append("sword")
        print_pause("You walk back out to the field.")
    give_choice(items, characters_list, weapons_list)


def field(items, characters_list, weapons_list):
    print_pause("You run back into the field.")
    print_pause("Luckily, you don't seem to have been followed.")
    give_choice(items, characters_list, weapons_list)


def house(items, characters_list, weapons_list):
    print_pause("You approach the door of the creepy house.")
    print_pause("You are about to knock when the door opens and out steps a "
                + characters_list + ".")
    print_pause("Eeeeeeeeep! This is the " + characters_list + "'s house!")
    print_pause("The " + characters_list + " attacks you!")
    if "sword" in items:
        print_pause("As the " + characters_list + " moves to attack, "
                    "you unsheath your new sword.")
        print_pause("The Sword of Ogoroth shines brightly in your hand "
                    "as you brace yourself for the attack.")
        print_pause("But the " + characters_list + " takes one look at "
                    "your shiny new toy and runs away!")
        print_pause("You have rid the town of the " + characters_list + ".")
        print_pause("You are victorious!")
        play_again()
    else:
        print_pause("You feel a bit under-prepared for this, "
                    "with only having a " + weapons_list)
        fight_runaway(items, characters_list, weapons_list)


def play_again():
    response = valid_input("\nWould you like to play again? "
                           "\nPlease say 'yes' or 'no'.",
                           "yes", "no")
    if "no" in response:
        print_pause("\nOK, goodbye!")
    elif "yes" in response:
        print_pause("\nVery good, let's play again.")
        play_game()


def play_game():
    characters_list = random.choice(["unicorn", "vampire", "yak",
                                     "zebra", "dragon"])
    weapons_list = random.choice(["dagger", "iphone", "swiss pocket knive",
                                  "carot", "water bottle"])
    items = []
    intro(characters_list, weapons_list)
    give_choice(items, characters_list, weapons_list)


if __name__ == "__main__":
    play_game()
