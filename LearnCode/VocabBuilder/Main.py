import Vocabe_Mange
import json

def main():
    print("Welcome To Vocab Library \n")
    while True :
        try :
            print("Your Choices Are 1) Add  2) Delete 3) View 4) Quiz 5) Exit The Vocabulary \n")
            option = int(input("Choose Your Option : "))
            if option == 1 :
                Word = input("Enter Your Word : ")
                Meaning = input("Enter The Words Meaning : \n")
                Vocabe_Mange.add(Word,Meaning)
            elif option == 2 :
                word = input("Enter The Word To Delete ")
                Vocabe_Mange.delete(word)
            elif option == 3 :
                Vocabe_Mange.display()
            elif option == 4 :
                Vocabe_Mange.quiz() 
            elif option == 5 :
                Vocabe_Mange.exit()
            else :
                print("Enter Only Numbers from 1 to 4 \n")
        except ValueError:
            print("Enter Only Numbers\n")
            
if __name__ == "__main__":
    main()
        
        

    