def isValid(password):
    valid = True
    if(len(password) < 6 or len(password) > 10):
        print("Password must be between 6 and 10 characters")
        valid = False
    countOfDigits = 0
    wrong = 0
    
    for i in password:
        if(int(ord(i)) < 65 or int(ord(i)) > 90 and int(ord(i)) < 97 or int(ord(i)) > 122):
            if(int(ord(i)) >= 48 and int(ord(i)) <= 57):
                countOfDigits += 1
            else:
                if(wrong == 0):
                    wrong += 1
                    print("Password must consist only of letters and digits")
                    valid = False
        
    if(countOfDigits < 2):
        print("Password must have at least 2 digits")
        valid = False
    if(valid):
        print("Password is valid")

password = input()
isValid(password)