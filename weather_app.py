from sign_up import signup
from login import login_user
print("Welcome to De Weather!!")
user=input("Please insert [User] to use the app [Programmer] to edit the weather: ")
if user=="User" or user=="user":
   print("Please log in or sign up to continue")
   while True:
    option=input("Press l for login , s for sign up")
    if option=="L" or option=="l":
      login_user()
    elif option=="s" or option=="S":
       signup()
    elif option=="quit" :
        break
    else:
        print("Please Press l for login , s for sign up,q for quit my app!")

