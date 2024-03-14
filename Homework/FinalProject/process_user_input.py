
def process_user_input():
    userInput=input("Introduceti subcategoria: ")
    checkOther=0
    userInput=userInput.strip()
         
    try:
        #if not all(userInput.isalpha() or char.isspace() for char in userInput):
        for char in userInput:
            if not (char.isalpha() or char.isspace() or char=="-"):
               checkOther=checkOther+1
        if checkOther>0:       
            raise ValueError("Input should contain only text and spaces")
        userInput = userInput.lower()
        # userInput = userInput.capitalize()
        return userInput
    except ValueError as e:
        print(f"Error: {e}")
        return None

#user_input=""
# user_input=input("introduceti subcategoria: ")  
# result=process_user_input(user_input)
result=process_user_input()

#print("Processed input:-",result)