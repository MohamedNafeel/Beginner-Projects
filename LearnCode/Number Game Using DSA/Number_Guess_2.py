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
                    print("4. Search Element (Maximum 10 inputs int array )\n")
                    print("5. Exit \n")
                    mode = input("Enter Your Desired Mode (1, 2, or 3 or 4 or 5  ): \n")
                    mode = int(mode)
                    
                    return mode 
                except ValueError:
                    print("Invalid input. Please enter a number (1, 2, or 3 or 4 0r 5 ).\n")  
                    continue 
def mode_easy():
    easy_number = random.randint(1, 10)
    print("Since You selected Easy Mode. Guess a number between 1 and 10.\n")
    count =  0
    while True :
        try :
            guess = int(input("Enter An Number Between (1-10) :\n"))  
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 10.\n")
            continue
        if guess == easy_number :
            print("Congratulations! You guessed the correct number.\n")
            count += 1
            return count    
        elif guess < easy_number :
            print("Too low! Try again.\n")
            count += 1 
        elif  guess > easy_number :
            print("Too high! Try again.\n")
            count += 1         
def mode_medium():
    print("Since You selected Medium Mode. Guess a number between 1 and 100.\n")
    medium_number = random.randint(1, 100)
    count = 0 
    while True :
        try :
            guess = int(input("Enter A Number Between (1-100) :\n"))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 100.\n")
            continue
        if guess == medium_number :
            print("Congratulations! You guessed the correct number.\n")
            count += 1 
            return count 
        elif guess < medium_number :
            print("Too low! Try again.\n")
            count += 1 
        elif guess > medium_number :
            print("Too high! Try again.\n")
            count += 1 
def mode_hard():
    print("Since You selected Hard Mode. Guess a number between 1 and 200.")
    hard_number = random.randint(1,200)
    count = 0
    while True :
        try :
            guess = int(input("Enter a Number Between (1-200):\n"))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 200.\n")
            continue
        if guess == hard_number :
            print("Congratulations! You guessed the correct number.\n")
            count += 1 
            return count 
        elif guess < hard_number :
            print("Too low! Try again.\n")
            count += 1 
        elif guess > hard_number  :
            print("Too high! Try again.\n")
            count += 1 
def exit_game():
    print("Thank you for playing the number guessing game. Goodbye!")
    sys.exit()
def play_again():
    while True :
        try:
            play_again= input("Do you want to play Gain (YES / NO ):").lower()
            
            if play_again == "yes":
                return True 
                break
            if play_again == "no":
                exit_game()
                break
        except ValueError:
            print("Invalid input. Please enter YES or NO.")
            continue              
def counter(count):
    if count >= 10 :
        print("You are very Bad \n")
    elif 10 > count > 5 :
        print("You are Average \n")
    elif count <= 5 :
        print("You are good\n")
def BinarySearch(Numbers,target):
    low = 0
    high = len(Numbers)-1 
    while low <= high :
        mid = (low + high)//2 
        if Numbers[mid] == target  :
            return mid 
        elif Numbers[mid] < target :
            low = mid + 1 
        elif Numbers[mid]  > target :
            high = mid - 1     
    return -1      
def main():
    while True:
        mode = select_mode()
        if mode == 1 :
            count = mode_easy()
            counter(count)
            play_again()
            if not play_again: 
                break      
        elif mode == 2 :
            count = mode_medium()
            counter(count)
            play_again()
            if not play_again: 
                break
        elif mode == 3 :
            count = mode_hard()
            counter(count)
            play_again()
            if not play_again:  
                break
        elif mode == 4 :
            n =  int(input("Enter The No of elements In the Array \n"))
            print('Enter Elements In Ascending Order ')
            Numbers = [int(input(f"Enter The Element {i} \n")) for i in range (n)]   
            target = int(input("Enter Ther Element You want to search \n"))  
            result = BinarySearch(Numbers,target)
            if result != -1 :
                print(f"The Given Target Element {target} is found at  index {result}\n")
            else :
                print('No Such  Element Is Found \n')
            break
        elif mode == 5 :
            exit_game()
            break
            
if __name__ == "__main__" :
    main()   