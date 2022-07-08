while True:
    x = input("\nDo you want to play the text-base adventure game? [yes/no]: ")
    if x == "yes" or x == "y":
        print("Alright great!\n")
        x = input("You have two choices for an adventure, Choose One [cave/jungle]: ")
        print("")
        if x == "cave":
            x = input("You went in the cave and you met a bear, What would you do? [fight/run]: ")
            print("")

            if x == "fight":
                print("you fought the bear but the bear is too strong, YOU LOSE!\n")
            elif x == "run":
                print("The bear was too strong, so you ran away, YOU WIN!\n")
            else:
                print("Invalid command\n")
        elif x == "jungle":
            x = input("You went in the jungle and heard a roar of a lion, What would you do? [proceed/run]: ")
            print("")
            if x == "proceed":
                print("You went in the jungle and found a lion, you tried to run but the lion was too fast. YOU LOSE!\n")
            elif x == "run":
                print("You ran away from the lion and saved yorself, YOU WIN!\n")
            else:
                print("Invalid command\n")
        else:
            print("Invalid command\n")
    elif x == "no" or "n":
        print("But this is a really fun game!\n")
        x = input("Are you sure you don't want to play this game? [yes/no]: ")
        print("")
        if x == "no" or x == "n":
            print("\n")
        elif x == "yes" or x == "y":
            print("Alright, you can close this window now")
            break
    else:
        print("Invalid command\n")
        break