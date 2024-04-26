import random
def RPS():
    try:
        user_input = int(input('''
Enter The corrosponding Number of Your Action || 1.Rock 2.Paper 3.Sissors || 0 to Exit
=>'''))
    except:
        print("INVALID INPUT)
    if user_input == 0:
        exit()
    computer_input = random.choice([1, 2, 3])
    if user_input == computer_input :
        print("Its A Tie")
    if user_input == 1 and computer_input == 2:
        print("Computer Wins")
    if user_input == 2 and computer_input == 3:
        print("Computer Wins")
    if user_input == 3 and computer_input == 1:
        print("Computer Wins")
    if user_input == 1 and computer_input == 3:
        print("Player Wins")
    if user_input == 2 and computer_input == 1:
        print("Player Wins")
    if user_input == 3 and computer_input == 2:
        print("Player Wins")
while True:
    RPS()
