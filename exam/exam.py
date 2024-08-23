profile = input("Do you want to Register or login? ")
if profile == "Register" or "register":
   reg11 = input("Enter username :")
   reg12 = input("Enter Display name:")
   reg1  = input("Enter Password:")
   reg13 = int(input("Enter card number:"))
   reg14 = int(input("Enter card date:"))
   reg15 = int(input("Enter card CVC:"))
   fin = input("Are you entered correct information?:")
if fin == "Yes" or "yes":
   print("Account information:")
   print("Username:" + " " + reg11)
   print("Display name:" + " " + reg12)
   print("Password:" + " " + reg1)
   print("Card Number:" + " " + reg13)
   print("Card date:" + " " + reg14)
   print("Card CVC:" + " " + reg15)
   print("Your account successfuly created (Please Save in your device this information!!!) ")
   do  =  input("Write: (Done) to fully success")
   
if profile == "Login" or "login":
         reg11 = input("Enter username :")
         reg12 = input("Enter Display name:")
         reg1  = input("Enter Password:")
         reg13 = int(input("Enter card number:"))
         reg14 = int(input("Enter card date:"))
         reg15 = int(input("Enter card CVC:"))
         do1 = input("Write: (Done) to fully success")
         






if do == "Done" or do1 == "Done":

 bank = int(input("How much do you want to deposit?"))
 bank2 = int(input("How much do you want to witdraw?"))
 bank3 = input("Are you sure?")

if bank3 == "Yes" or bank3 == "yes":
    print("Please wait")
out = bank - bank2
if out < bank:
 print("You dont have enough money to witdhraw")



 




