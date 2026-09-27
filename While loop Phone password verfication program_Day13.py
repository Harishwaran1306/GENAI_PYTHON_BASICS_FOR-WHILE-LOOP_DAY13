#While Loop
#Phone Password Verification using While Loop

Phone_password = 12302
password = 0
attempt = 0
while attempt < 5:
    password = int(input('Enter Password:'))

    if password == Phone_password:
        print('Unlocked')
        break    
             
    

    else:
        attempt +=1
        print("Incorrect password. Attempts left:", 5 - attempt)
        

else:
    if attempt == 5 and password != Phone_password:
        print("Too many wrong attempts. Phone Blocked!")
    
  
