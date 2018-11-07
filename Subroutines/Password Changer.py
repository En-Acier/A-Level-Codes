def getPword(attempt):
    if attempt == 1:
        temp = input("Please enter your password")
        if len(temp) <= 8 and len(temp) >= 6:
            password = temp
            return(password)
        else:
            print("Error, the password should be between 6 & 8 characters")
    else:
        temp = input("Please re-enter your password")
        if len(temp) <= 8 and len(temp) >= 6:
            password = temp
            return(password)
        else:
            print("Error, the password should be between 6 & 8 characters")



attempt = 1
password = getPword(attempt)

attempt = 2
password2 = getPword(attempt)
if password2 == password:
    print("Password change successful")
else:
    print("Error, passwords do not match")



