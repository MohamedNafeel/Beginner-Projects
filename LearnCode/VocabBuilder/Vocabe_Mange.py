import json , sys , random
def add(word,meaning):
    with open(file = "Vocab.json" , mode = "r") as file :
        try :
            data = json.load(file)
        except json.JSONDecodeError:
            data = {}
            print("Dictionary Was Empty Before , try adding the word now ")
        data[word] = meaning 
    with  open(file = "Vocab.json", mode = "w") as file :
        json.dump(data,file,indent = 4)
def delete(word):
    with open("Vocab.json","r") as file :
        data = json.load(file)
    if word not in data :
        print("Word Does Not Exist")
    else : 
        del data[word]
    with open("Vocab.json" , "w") as file :
        json.dump(data,file,indent= 4)
def display():
    with open("Vocab.json","r") as file :
            Display_elements = json.load(file)
    if not Display_elements:
        print("No Elements in File ")
    for Key , Value in Display_elements.items() :
        print(f"{Key} : {Value}\n")           
def exit():
    sys.exit()
def quiz():
    with open("Vocab.json" , "r") as file :
        qdata = json.load(file)
    try : 
        q_key = random.choice(list(qdata))
        q_value = input(f"Enter The Meaning For The Word : {q_key}  : ").lower().strip()
        if q_value == qdata[q_key]:
            print("The Meaniing Is Indeed Correct !!!!")
        else :
            print(f"Wrong ! The Correct Meanng was {qdata[q_key]}")
    except IndexError :
        print("The Vocabulary Is Empty , Please Add Some Words First ")
        return 
        