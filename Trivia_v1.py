import sys

title = "========================================================\n" \
        "================         Trivia         ================\n" \
        "========================================================"

def packtoTxt(pack, pack_name): #Converts a 2d array into a .txt
    text = ""
    text += pack[0][0]
    pack_name_txt = "Packs/" + pack_name
    for i in range(len(pack)):
        if i != 0:
            text += "\n"
            text += pack[i][0]
            text += "\n"
            text += pack[i][1]
    with open(pack_name_txt, "w") as f:
        f.write(text)
    with open("yourPacks", "a") as fa:
        pack_name_txt2 = "\n" + pack_name
        fa.write(pack_name_txt2)

def txtToPack(file): #Converts a .txt into a 2d array
    f_contents_new = []
    f_pack = []
    with open(file, "r") as f:
        f_contents = f.readlines()
        for i in range(len(f_contents)):
            f1 = f_contents[i]
            f_contents_new.append(f1[0:-1])
    f_pack.append([f_contents_new[0]])
    for i in range(len(f_contents_new)):
        if i%2 == 1:
            f_pack.append([f_contents_new[i],f_contents_new[i + 1]])
    return f_pack

def packPlayer(pack): #Turns a 2d array into a playable Trivia questions
    pack_len = len(pack)
    print("========================================================\n========================================================")
    print("\n" + pack[0][0] + "\n")
    correct = 0
    for i in range(pack_len):
        if i == 0:
            pass
        else:
            print(pack[i][0])
            ans = input("Enter Answer: ")
            if ans == pack[i][1]:
                print("Correct!\n")
                correct += 1
            else:
                print("Incorrect! The answer was '" + pack[i][1] + "'\n")
    print("\nYou scored", str(correct) + "/" + str(len(pack) - 1) + "!\n")
    a = input("")
    game().main_menu()

class game: #Holds the Game logic
    def __init__(self):
        pass
    def main_menu(self):
        print("\n" + "========================================================\n" \
                     "================         Trivia         ================\n" \
                     "========================================================")
        print("\nWelcome to Trivia!!! This is the best trivia game\nyou have ever played!\n")
        print("1: Play\n"
              "2: Make\n"
              "3: Quit")
        while True:
            num = input("Enter number: ")
            if num == "1":
                game().play()
                break
            elif num == "2":
                game().make()
                break
            elif num == "3":
                sys.exit()
            print("Enter a valid number!!!\n")

    def play(self):
        print("\n" + "========================================================\n" \
                     "================          Play          ================\n" \
                     "========================================================")
        print("\nThis is were you get to chose what trivia\npack you want to play!\n")
        print("1: Trivia pack (default)\n"
              "2: Your packs\n"
              "3: Quit")
        while True:
            num = input("Enter number: ")
            if num == "1":
                packPlayer(txtToPack("pack_GeneralKnowledge"))
                break
            elif num == "2":
                game().yourPacks()
                break
            elif num == "3":
                game().main_menu()
                break
            print("Enter a valid number!!!\n")

    def make(self):
        print("\n" + "========================================================\n" \
                     "================          Make          ================\n" \
                     "========================================================")
        print("\nThis is were you get to chose what trivia\npack you want to play!\n")
        print("1: New pack\n"
              "2: Quit")
        while True:
            num = input("Enter number: ")
            if num == "1":
                game().newPack()
                break
            elif num == "2":
                game().main_menu()
                break
            print("Enter a valid number!!!\n")

    def newPack(self): #creates a new pack
        print("\n========================================================\n========================================================\n")
        print("Welcome to Trivia makeer!\nThe best place to make your trivia pack!\n")
        yourPack = []
        pack_name = input("Enter Pack Name: ")
        pack_title = input("Enter Pack Discription: ")
        pack_num_questions = int(input("Enter amount of questions: "))
        yourPack.append([pack_title])
        for i in range(pack_num_questions):
            q = input("\nEnter question " + str(i + 1) + ": ")
            a = input("Enter the answer: ")
            print()
            yourPack.append([q,a])
        save = input("Do you wish to save this Pack? (y/n): ")
        lastWord = yourPack[-1][1]
        lastWord += (lastWord[-1])
        yourPack[-1][1] = lastWord
        if save == "y":
            packtoTxt(yourPack, pack_name)
            print()
            print("Pack saved!")
        game().main_menu()

    def yourPacks(self):
        with open("yourPacks", "r") as f:
            f_contents = f.readlines()
        print(f_contents)
        print("\n========================================================\n========================================================\n")
        print("These are  all of your packs!\n")
        for i in range(len(f_contents)):
            print(str(i + 1) + ": " + f_contents[i], end="")
        print("\n")
        j = True
        while True:
            play_pack = input("Which Pack do you wish to play: ")
            try:
                packPlayer(txtToPack("Packs/" + play_pack))
                game().main_menu()
                j = False
            except:
                game().main_menu()