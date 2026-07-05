 
import random 
import sys 
def select_mode():
        while True:
                try :
                    print("Welcome To the number guessing Game \n")
                    print("Please Select Your Desired Mode for the game\n ")
                    print("1. Easy Mode (1-10) \n")
                    print("2. Medium Mode (1-100) \n")
                    print("3. Hard Mode (1-200) \n")
                    print("4. Exit \n")
                    mode = input("Enter Your Desired Mode (1, 2, or 3 or 4 ): ")
                    mode = int(mode)
                    return mode 
                except ValueError:
                    print("Invalid input. Please enter a number (1, 2, or 3 or 4 ).")  
                    continue 
                
                
def exit_game():
    sys.exit("Thank you for playing! Goodbye!")
        
def play_again():
    print("Do you want to play again? (yes/no)")
    while True :
        try :
            play_again = input("Enter Your Choice (yes or no) :").lower()
            if play_again == "yes" :
                return True 
            elif play_again == "no" :
                print("Thank you for playing! Goodbye!")
                sys.exit()
        except ValueError:
            print("Invalid input. Please enter 'yes' or 'no'.")
            continue
    

def play_game(mode,Max_number):
    
        number = random.randint(1,Max_number)
        print(f"Since You selected {mode} Mode. Guess a number between 1 and {Max_number}.\n")
        while True :
            try : 
                guess = int(input(f"Enter An Number Between (1-{Max_number}) :"))
                if guess < 1 or guess > Max_number :
                    print(f"Invalid input. Please enter a number between 1 and {Max_number}.")
            except ValueError:
                print(f"Invalid input. Please enter a number between 1 and {Max_number}.")
                continue
            if guess == number :
                print("Congratulations! You guessed the correct number.\n")
                break
            elif guess < number :
                print("Too low! Try again.\n")
            elif guess > number :
                print("Too high! Try again.\n")
            
            

            
def main():
    while True :
        mode = select_mode()
        if mode == 1 :
            play_game("Easy",10)
            play_again()
            if not play_again:  break
        elif mode == 2 :
            play_game("Hard",100)
            play_again()
            if not play_again:  break
            
        elif mode == 3 :
            play_game("Impossible ",200)
            play_again()
            if not play_again:  break
        elif mode == 4 :
            exit_game()
            break
    
    
if __name__ == "__main__":
    main()