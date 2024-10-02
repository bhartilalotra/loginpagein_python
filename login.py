#program to construct login page
username=input("enter the username") 
email=input("enter the mail")
password=int(input("enter the password"))
cpassword=int(input("enter the cpass"))
age=int(input("enter the age"))
max_attempts=3
chance=1
if (password==cpassword):
    print("logged in")
else:
    print("try again ")


while chance<=max_attempts:
    password=int(input("enter the password"))
    cpassword=int(input("enter the cpass"))
    if (password==cpassword):
     print("logged in")
     break
          
    else:
        
        print(f" You have {max_attempts-chance } chance left")
        chance+=1
      
# CALCULATE PROFIT  AND LOSS         
print("...........CALCULATE LOSS AND PROFIT ..........")
       
SP=float(input("enter the SP"))
CP=float(input("enter the CP"))

if(SP>CP):
    profit=SP-CP
    print(f"profit is {SP-CP}") 
elif(SP<CP):
    loss=CP-SP 
    print(f"loss is {CP-SP}")
else:
    print("NO PROFIT OR LOSS")
