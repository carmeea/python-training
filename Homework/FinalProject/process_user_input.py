
def process_user_input():
    userInput=input("Introduceti subcategoria: ")
    checkOther=0
    userInput=userInput.strip()
         
    try:
        
        for char in userInput:
            if not (char.isalpha() or char.isspace() or char=="-"):
               checkOther=checkOther+1
        if checkOther>0:       
            raise ValueError("Input should contain only text and spaces or -")
        userInput = userInput.lower()
        userInput = userInput.replace(" ","-")
        
        return userInput
    except ValueError as e:
        print(f"Error: {e}")
        return None

result=process_user_input()
