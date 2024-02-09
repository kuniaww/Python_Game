import random
import time

def simon_says():
    print("Welcome to Simon Says!")
    print("I will give you commands, and you have to follow them only if they start with 'Simon says'.")

    commands = ["Simon says jump", "Simon says clap", "Simon says nod", "Jump", "Clap", "Nod"]

    while True:
        # Get a random command
        command = random.choice(commands)

        print("\n" + command)

        # Check if the command starts with "Simon says"
        if command.startswith("Simon says"):
            player_input = input("Simon says: ")
            if player_input.lower() == command[11:].lower():
                print("Good job!")
            else:
                print("Wrong! Game Over.")
                break
        else:
            player_input = input("Don't Simon says: ")
            if player_input.lower() == command.lower():
                print("Wrong! Game Over.")
                break
            else:
                print("Good job!")


if __name__ == "__main__":
    simon_says()
