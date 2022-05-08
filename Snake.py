import random
import os
os.system("cls")
com = 0
gamer = 0
print("************************  WELCOME to Rock, Scissor and Game against with Computer  ***************************\n")
a = input("Enter your Name...\n")
print(' \n                                ^^^^^^^^^^^^^^ HELLO..' +
      a.upper()+' ^^^^^^^^^^^^^^ ')
print("\n=========== Type 'Yes' to Play the Game otherwise 'No' to Quit. =========== ")
while(True):
    try:
        b = input().lower()
        if b == 'yes':
            print(
                "\nHow many Rounds of Game You want to Play with Computer --->  ", end="")
            f = int(input())
            print(
                "\nType any--> 's' for Scissor\n\t--> 'r' for Rock\n\t--> 'p' for Paper\n")
            e = 0
            while e != f:
                d = random.randint(1, 3)
                if (d == 1):
                    computer = 's'
                elif (d == 2):
                    computer = 'r'
                elif (d == 3):
                    computer = 'p'
                # print(d)
                c = input().lower()
                if c == 's' or c == 'p' or c == 'r':
                    if c == 's' and computer == 'p':
                        print(
                            f'you choose --> "Scissor" and Computer choose --> "Paper"')
                        print(f'{a} won \nChoose S,R or P Again')
                        gamer = gamer+1
                    elif c == 's' and computer == 'r':
                        print(
                            f'you choose --> "Scissor" and Computer choose --> "Rock"')
                        print('Computer won \nChoose S,R or P Again')
                        com = com+1
                    elif c == 's' and computer == 's':
                        print(
                            'DRAW!..as both choosen Scissor \nChoose S,R or P Again')
                    if c == 'r' and computer == 'p':
                        print(
                            f'you choose --> "Rock" and Computer choose --> "Paper"')
                        print('Computer won \nChoose S,R or P Again')
                        com = com+1
                    elif c == 'r' and computer == 'r':
                        print('DRAW!..as both choosen Rock \nChoose S,R or P Again')
                    elif c == 'r' and computer == 's':
                        print(
                            f'you choose --> "Rock" and Computer choose --> "Scissor"')
                        print(f'{a} won \nChoose S,R or P Again')
                        gamer = gamer+1
                    if c == 'p' and computer == 'p':
                        print('DRAW!..as both choosen Paper \nChoose S,R or P Again')
                    elif c == 'p' and computer == 'r':
                        print(
                            f'you choose --> "Paper" and Computer choose --> "Rock"')
                        print(f'{a} won \nChoose S,R or P Again')
                        gamer = gamer+1
                    elif c == 'p' and computer == 's':
                        print(
                            f'you choose --> "Paper" and Computer choose --> "Scissor"')
                        print('Computer won \nChoose S,R or P Again')
                        com = com+1
                    e = e+1
                else:
                    print(".......Wrong Character!!.......\n Write again")
            break
        elif 'no' in b:
            print('Thank You...See You Soon..!!')
            break
        else:
            print("Invalid Character...\nType only 'Yes' or 'No'")
    except ValueError:
        print("\n_____________ Invalid Integer, Enter ...'YES'... to Continue again or ...'NO'... to Exit ____________")
if gamer > com:
    print(f'\n\n==== {a} --> {gamer * 10} ==== \n==== Computer ---> {com * 10} ====\n\n*****************************   Congratulation, You defeated the Computer, See You Again :)   ******************************\n')
elif com > gamer:
    print(f'\n\n==== {a} --> {gamer * 10} ==== \n==== Computer ---> {com * 10} ====\n\n*****************************   OOPS, You are defeated by the Computer...Better Luck Next Time :)   **************************\n')
else:
    print(f"\n\n==== {a} --> {gamer * 10} ====\n==== Computer ---> {com * 10} ====\n\n****************************** ------- 'TIE' ------- ******************************* \n")