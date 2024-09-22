# jungle game
# Names
player1 = input("What is your name player 1: ")
player2 = input("What is your name player 2: ")
player3 = input("What is your name player 3: ")
#animals
animallist = ["elephant" , "lion" , "dog" , "cat" , "mouse" ]
print(animallist)
#choice
choice1 = input(f"what is your choice {player1}: ")
choice2 = input(f"what is your choice {player2}: ")
choice3 = input(f"what is your choice {player3}: ")
# condition
if choice1 == "elephant" and choice2 == "lion" and choice3 == "dog":
    print(f"{player1} is winner and {player2} is two and {player3} is three")
elif choice1 == "elephant" and choice2 =="lion" and choice3 == "cat":
    print(f"{player1} is winner and {player2} is two and {player3} is three")
elif choice1 == "elephant" and choice2 == "lion" and choice3 == "mouse":
    print(f"{player1} is winner and {player2} is two and {player3} is three")
elif choice1 == "elephant" and choice2 == "lion" and choice3 == "elephant":
    print(f"{player1} and {player2} are winners")
elif choice1 == "elephant" and choice2 == "dog" and choice3 == "lion":
    print(f"{player3} is winner and {player1} is two and {player2} is three")
elif choice1 == "elephant" and choice2 == "dog" and choice3 == "elephant":
    print(f"{player1} and {player3} are winners")
elif choice1 == "elephant" and choice2 == "dog" and choice3 == "cat":
    print(f"{player1} is winner")
elif choice1 == "elephant" and choice2 == "dog" and choice3 == "dog":
    print(f"{player2} and {player3} are winners")
elif choice1 == "elephant" and choice2 == "dog" and choice3 == "mouse":
    print(f"{player1} is winner and {player2} is two and {player3} is three")
elif choice1 == "elephant" and choice2 == "cat" and choice3 == "lion":
    print(f"{player3} is winner and {player2} is two")
elif choice1 == "elephant" and choice2 == "cat" and choice3 == "elephant":
    print(f"{player1} and {player3} are winners")
elif choice1 == "elephant" and choice2 == "cat" and choice3 == "dog":
    print(f"{player2} is winner and {player3} is two and {player1} is three")
elif choice1 == "elephant" and choice2 == "cat" and choice3 == "mouse":
    print(f"{player1} is winner and {player2} is two and {player3} is three")
elif choice1 == "elephant" and choice2 == "mouse" and choice3 == "lion":
    print(f"{player3} is winner")
elif choice1 == "elephant" and choice2 == "mouse" and choice3 == "elephant":
    print(f"{player1} and {player2} are winners")
elif choice1 == "elephant" and choice2 == "mouse" and choice3 == "dog":
    print(f"{player1} is winner and {player2} is two and {player3} is three")
elif choice1 == "elephant" and choice2 == "elephant" and choice3 == "cat":
    print(f"{player1} and {player2} are winners")
elif choice1 == "elephant" and choice2 == "elephant" and choice3 == "elephant":
    print("all players won")
elif choice1 == "elephant" and choice2 == "elephant" and choice3 == "lion":
    print(f"{player3} is winner than {player1} and {player2}")
elif choice1 == "elephant" and choice2 == "dog" and choice3 == "elephant":
    print(f"{player1} and {player3} are winner")
elif choice1 == "elephant" and choice2 == "dog" and choice3 == "dog":
    print(f"{player1} is winner")
elif choice1 == "elephant" and  choice2 == "dog" and choice3 == "cat":
    print(f"{player1} is winner and {player2} is two and {player3} is three")
elif choice1 == "elephant" and choice2 == "dog" and choice3 == "mouse":
    print(f"{player1} is winner")
elif choice1 == "lion" and choice2 == "elephant" and choice3 == "dog":
    print(f"{player1} is winner")
elif choice1 == "lion" and choice2 == "elephant" and choice3 == "lion":
    print(f"{player1} and {player3} are winners")
elif choice1 == "lion" and choice2 == "elephant" and choice3 == "cat":
    print(f"{player1} is winner")
elif choice1 == "lion" and choice2 == "elephant" and choice3 == "mouse":
    print(f"{player2} is winner")
elif choice1 == "lion" and choice2 == "dog" and choice3 == "elephant":
    print(f"{player3} is winner and {player1} is two and {player2} is three")
elif choice1 == "lion" and choice2 == "dog" and choice3 == "lion":
    print(f"{player1} and {player3} are winners")
elif choice1 == "lion" and choice2 == "dog" and choice3 == "cat":
    print(f"{player1} is winner")
elif choice1 == "lion" and choice2 ==  "dog" and choice3 == "dog":
    print(f"{player1} is winner and {player2} and {player3} are two")
elif choice1 == "lion" and choice2 == "dog" and choice3 == "mouse":
    print(f"{player1} is winner and {player2} is two and {player3} is three")
elif choice1 == "lion" and choice2 == "cat" and choice3 == "elephant":
    print(f"{player3} is winner")
elif choice1 == "lion" and choice2 == "cat" and choice3 == "dog":
    print(f"{player1} is winner")
elif choice1 == "lion" and choice2 == "cat" and choice3 == "mouse":
    print(f"{player1} is winner")
elif choice1 == "lion" and choice2 == "cat" and choice3 == "lion":
    print(f"{player1} and {player2} are winners")
elif choice1 == "lion" and choice2 == "mouse" and choice3 == "elephant":
    print(f"{player3} is winner")
elif choice1 == "lion" and choice2 == "mouse" and choice3 == "lion":
    print(f"{player1} and {player3} are winners")
elif choice1 == "lion" and choice2 == "mouse" and choice3 == "dog":
    print(f"{player1} is winner")
elif choice1 == "lion" and choice2 == "mouse" and choice3 == "cat":
    print(f"{player1} is winner")
elif choice1 == "lion" and choice2 == "mouse" and choice3 == "mouse":
    print(f"{player1} is winner")
elif choice1 == "lion" and choice2 == "lion" and choice3 == "lion":
    print("all players won")
elif choice1 == "lion" and choice2 == "lion" and choice3 == "elephant":
    print(f"{player1} and {player2} are winners")
elif choice1 == "lion" and choice2 == "lion" and choice3 == "dog":
    print(f"{player1} and {player2} are winners")
elif choice1 == "lion" and choice2 == "lion" and choice3 == "cat":
    print(f"{player1} and {player2} are winners")
elif choice1 == "lion" and choice2 == "lion" and choice3 == "mouse":
    print(f"{player1} and {player2} are winners")
elif choice1 == "cat" and choice2 == "elephant" and choice3 == "lion":
    print(f"{player2} and {player3} are  winners")
elif choice1 == "cat" and choice2 =="elephant" and choice3 == "dog":
    print(f"{player2} is winner")
elif choice1 == "cat" and choice2 == "elephant" and choice3 == "mouse":
    print(f"{player2} is winner")
elif choice1 == "cat" and choice2 == "elephant" and choice3 == "cat":
    print(f"{player2} is winner")
elif choice1 == "cat" and choice2 == "lion" and choice3 == "elephant":
    print(f"{player2} and {player3} are winners")
elif choice1 == "cat" and choice2 == "lion" and choice3 == "dog":
    print(f"{player2} is winner")
elif choice1 == "cat" and choice2 == "lion" and choice3 == "cat":
    print(f"{player2} is winner")
elif choice1 == "cat" and choice2 == "lion" and choice3 == "mouse":
    print(f"{player2} is winner")
elif choice1 == "cat" and choice2 == "dog" and  choice3 == "elephant":
    print(f"{player3} is winner")
elif choice1 == "cat" and choice2 == "dog" and choice3 == "lion":
    print(f"{player3} is winner")
elif choice1 == "cat" and choice2 == "dog" and choice3 == "dog":
    print(f"{player2} and {player3} are winners")
elif choice1 == "cat" and choice2 == "dog" and choice3 == "cat":
     print(f"{player2} is winner")
elif choice1 == "cat" and choice2 == "dog" and choice3 == "mouse":
     print(f"{player2} is winner")
elif choice1 == "cat" and choice2 == "cat" and choice3 == "elephant":
    print(f"{player3} is winner")
elif choice1 == "cat" and choice2 == "cat" and choice3 == "lion":
    print(f"{player3} is winner")
elif choice1 == "cat" and choice2 == "cat" and choice3 == "dog":
    print(f"{player1} and {player2} are winners")
elif choice1 == "cat" and choice2 == "cat" and choice3 == "cat":
    print("all players won")
elif choice1 == "cat" and choice2 == "cat" and choice3 == "mouse":
    print(f"{player1} and {player2} are winners")
elif choice1 == "cat" and choice2 == "mouse" and choice3 == "elephant":
    print(f"{player3} is winner")
elif choice1 == "cat" and choice2 == "mouse" and choice3 == "lion":
    print(f"{player3} is winner")
elif choice1 == "cat" and choice2 == "mouse" and choice3 == "dog":
    print(f"{player3} is winner")
elif choice1 == "cat" and choice2 == "mouse" and choice3 == "cat":
    print(f"{player1} and {player3} are winners")
elif choice1 == "cat" and choice2 == "mouse" and choice3 == "mouse":
    print(f"{player2} and {player3} are winners")
elif choice1 == "mouse" and choice2 == "elephant" and choice3 == "lion":
    print(f"{player3} is winner")
elif choice1 == "mouse" and choice2 == "elephant" and choice3 == "dog":
    print(f"{player2} is winner")
elif choice1 == "mouse" and choice2 == "elephant" and choice3 == "cat":
    print(f"{player2} is winner")
elif choice1 == "mouse" and choice2 == "elephant" and choice3 == "mouse":
    print(f"{player2} is winner")
elif choice1 == "mouse" and choice2 == "lion" and choice3 == "elephant":
    print(f"{player2} and {player3} are winners")
elif choice1 == "mouse" and choice2 == "lion" and choice3 == "dog":
     print(f"{player2} is winner")
elif choice1 == "mouse" and choice2 == "lion" and choice3 == "lion":
    print(f"{player2} and {player3} are winners")
elif choice1 == "mouse" and choice2 == "lion" and choice3 == "cat":
     print(f"{player2} is winner")
elif choice1 == "mouse" and choice2 == "lion" and choice3 == "mouse":
     print(f"{player2} is winner")
elif choice1 == "mouse" and choice2 == "dog" and choice3 == "elephant":
     print(f"{player3} is winner")
elif choice1 == "mouse" and choice2 == "dog" and choice3 == "lion":
     print(f"{player3} is winner")
elif choice1 == "mouse" and choice2 == "dog" and choice3 == "cat":
     print(f"{player2} is winner")
elif choice1 == "mouse" and choice2 == "dog" and choice3 == "mouse":
     print(f"{player2} is winner")
elif choice1 == "mouse" and choice2 == "cat" and choice3 == "elephant":
     print(f"{player3} is winner")
elif choice1 == "mouse" and choice2 == "cat" and choice3 == "lion":
     print(f"{player3} is winner")
elif choice1 == "mouse" and choice2 == "cat" and choice3 == "dog":
     print(f"{player3} is winner")
elif choice1 == "mouse" and choice2 == "cat" and choice3 == "cat":
    print(f"{player2} and {player3} are winner")
elif choice1 == "mouse" and choice2 == "cat" and choice3 == "mouse":
    print(f"{player2} is winner")
elif choice1 == "mouse" and choice2 == "mouse" and choice3 == "elephant":
    print(f"{player1} and {player2} are winners")
elif choice1 == "mouse" and choice2 == "mouse" and choice3 == "lion":
    print(f"{player3} is winner")
elif choice1 == "mouse" and choice2 == "mouse" and choice3 == "dog":
    print(f"{player1} and {player2} are winners")
elif choice1 == "mouse" and choice2 == "mouse" and choice3 == "cat":
    print(f"{player1} and {player2} are winners")
elif choice1 == "mouse" and choice2 == "mouse" and choice3 == "mouse":
     print("all players won")
elif choice1 == "dog" and choice2 == "elephant" and choice3 == "lion":
    print(f"{player2} and {player3} are winners")
elif choice1 == "dog" and choice2 == "elephant" and choice3 == "cat":
    print(f"{player2} is winner")
elif choice1 == "dog" and choice2 == "elephant" and choice3 == "elephant":
     print(f"{player2} and {player3} are winners")
elif choice1 == "dog" and choice2 == "elephant" and choice3 == "mouse":
    print(f"{player2} is winner")
elif choice1 == "dog" and choice2 == "elephant" and choice3 == "dog":
    print(f"{player2} is winner")
elif choice1 == "dog" and choice2 == "lion" and choice3 == "elephant":
     print(f"{player2} and {player3} are winners")
elif choice1 == "dog" and choice2 == "lion" and choice3 == "lion":
     print(f"{player2} and player3 are winners")
elif choice1 == "dog" and choice2 == "lion" and choice3 == "dog":
    print(f"{player2} is winner")
elif choice1 == "dog" and choice2 == "lion" and choice3 == "cat":
    print(f"{player2} is winner")
elif choice1 == "dog" and choice2 == "lion" and choice3 == "mouse":
    print(f"{player2} is winner")
elif choice1 == "dog" and choice2 == "cat" and choice3 == "elephant":
    print(f"{player3} is winner")
elif choice1 == "dog" and choice2 == "cat" and choice3 == "lion":
    print(f"{player3} is winner")
elif choice1 == "dog" and choice2 == "cat" and choice3 == "cat":
    print(f"{player1} is winner")
elif choice1 == "dog" and choice2 == "cat" and choice3 == "mouse":
    print(f"{player1} is winner")
elif choice1 == "dog" and choice2 == "mouse" and choice3 == "elephant":
    print(f"{player3} is winner")
elif choice1 == "dog" and choice2 == "mouse" and choice3 == "lion":
    print(f"{player3} is winner")
elif choice1 == "dog" and choice2 == "mouse" and choice3 =="cat":
    print(f"{player1} is winner")
elif choice1 == "dog" and choice2 == "mouse" and choice3 == "dog":
    print(f"{player1} and {player3} are winners")
elif choice1 == "dog" and choice2 == "mouse" and choice3 == "mouse":
    print(f"{player2} and {player3} are winners")
elif choice1 == "dog" and choice2 == "dog" and choice3 == "dog":
     print("all players won")
elif choice1 == "dog" and choice2 == "dog" and choice3 == "elephant":
     print(f"{player3} is winner")
elif choice1 == "dog" and choice2 == "dog" and choice3 == "lion":
     print(f"{player3} is winner")
elif choice1 == "dog" and choice2 == "dog" and choice3 == "cat":
    print(f"{player1} and {player2} are winners")
elif choice1 == "dog" and choice2 == "dog" and choice3 == "mouse":
    print(f"{player1} and {player2} are winners")
else:
    print("we dont have any other animals")