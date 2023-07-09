# A quick translator to decode the names of cats in Mila's activity book :)
key = " abcdefghijklmnopqrstuvwxyz"

def crack_the_code():
    revealed_word = ''
    secret_code = []
   
    # recursive function to capture input
    def enter_number():
        code_num = input("Enter a number. Enter 0 for space. Press 'q' to end): ")
        # escape key
        if code_num =="q":
            return secret_code
        # check to see if the input is an integer
        try: 
            int(code_num)
        except ValueError: 
            print("You must enter only numbers")
            return enter_number()
        # check to see if the number is in range of the indexes in the key
        try:
            key[int(code_num)]
        except IndexError:
            print("The number must be between 0 and 26")
            return enter_number()
        # If the input gets to this point, add it to the array holding the code
        secret_code.append(code_num)
        print(secret_code)
        enter_number()
    # initialize the number entering 
    enter_number()    
    # loop over the inputted nums, reference the index of the key, return the word
    for i in range(len(secret_code)):
        revealed_word = revealed_word + key[int(secret_code[i])]
    return revealed_word
    

print(crack_the_code())