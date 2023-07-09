# A quick translator to decode the names of cats in Mila's activity book :)
key = " abcdefghijklmnopqrstuvwxyz"

def crack_the_code():
    revealed_word = ''
    secret_code = []
   
    def enter_number():
        code_num = input("Enter a number. Enter 0 for space. Press 'q' to end): ")
        if code_num =="q":
            return secret_code
        
        try: 
            int(code_num)
        except ValueError: 
            print("You must enter only numbers")
            return enter_number()
 
        try:
            key[int(code_num)]
        except IndexError:
            print("The number must be between 0 and 26")
            return enter_number()
        
        secret_code.append(code_num)
        print(secret_code)
        enter_number()
        
    enter_number()    

    for i in range(len(secret_code)):
        revealed_word = revealed_word + key[int(secret_code[i])]
    return revealed_word
    

print(crack_the_code())