#Control flow statement 18th Oct, 2022
# name = input ("Enter the name of person at the door: ")
# if (name == "Tiny"):
#    print(f"Hello {name}")
# elif (name =="Bunmi"):
#     print (f"Hello {name}!")
# else:
#     print (f"Go back {name}")

    #Write a simple program to accept two inputs, username and password, 
    #Condition: the username must be admin and the password 1234@admin,
    #Action: True  Hello, you're logged in {username}
    #Action:False Invalid username/password

username = input ("Enter your username:")
password = input ("Enter your password")
if (username == "Admin" and password == "1234@admin"):
    print (f"Hello, you're now logged in as an admin")
else:
    print (f"Invalid username/password")    



