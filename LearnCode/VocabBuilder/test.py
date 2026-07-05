
import json , random 

def quiz():
    with open("Vocab.json" , "r") as file :
        qdata = json.load(file)
    q_key = random.choice(list(qdata))
    q_value = input(f"Enter The Meaning For The Word : {q_key}  : ").lower().strip()
    if q_value == qdata[q_key]:
        print("The Meaniing Is Indeed Correct !!!!")
    else :
        print("The Meaning Is InCorrect ")
        
      
    
quiz()