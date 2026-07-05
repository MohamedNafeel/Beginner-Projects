import json 
from Wrap import answers 
import os 
import json
def main():
    try :
        prompt = input("Enter Your Doubts Here ?? ")
        response = answers(prompt)
    except Exception as e:
        print("ERROR : ",e)
        
    filename = "Output.json"
    with open(filename, "w" , encoding= "utf-8") as f :
        json.dump(response,f,indent=4)
    choice = input("Please Select if you want to see the response in the Temrinal Or save it to a file (Terminal/File) :").lower().strip()
    if choice == "terminal":
        Answer = response["candidates"][0]["content"]["parts"][0]["text"]  
        print(f"For the Follwing Questione : The Asnwer is  {Answer}\n")      
    if choice == "file":
        print(f"HAHAHAH Got you , We Already Saved the Response in an File Called : {filename}")

        
if __name__ == "__main__":
    main()
        

    
    
        
    