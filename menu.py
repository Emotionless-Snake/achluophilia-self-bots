from turtle import color
from termcolor import colored
from colorama import init
from colorama import Fore
def run(runfile):
  with open(runfile,"r") as rnf:
    exec(rnf.read())
init()

print(colored("{                  Welcome To Achluophile Self Bots!                    }" ,"white" , "on_blue"))
print ("                       You Can Choose Your Self-bot ^^")
print ("                        Program By Emotionless-Snake ©")

print ("                       ---------------------------------------------")
print ("                                      {  Help  }")
print (colored("                           Green Texts : Enabled Self-Bots" , "green"))
print (colored("                           Yellow Texts : Coming Soon Self-Bots" , "yellow"))
print (colored("                           Red Texts : Disabled Self-Bots" , "red"))
print ("                       ---------------------------------------------")
print(colored("                            1.Spammer Self-bot" , "green"))
print(colored("                            2.Portable Clock" , "green"))
print(colored("                            3.Online Until Close Program" , "green"))
print(colored("                            4.24/7 Voice Self-bot" , "yellow"))
print(colored("                            5.Set Your Status With Command" , "red"))
print(colored("{                                                                        }" ,"white" , "on_blue"))
choosevar = input ("Put The Your Choice As a Number : ")


if choosevar == "4":
  print(colored("This Self Bot Is Coming Soon..." , "yellow"))
  print("Re-open Program To Resest")

if choosevar == "5":
  print(colored("This Self Bot Is Disabled Yet..." , "red"))
  print("Re-open Program To Resest")


if choosevar == "1":
 print(colored("\033[4m!!Warning!! : Your account may be banned if you use this tool. We have no responsibility for this issue and we recommend that you do not use this tool on your main account and use it on your multi account." , "yellow" , "on_red")) 
 continue1 = input("Do You Want To Continue? (Y/N) : ")
 if continue1 == "y" or "Y":
    run("bots/1.py")
   
  
if choosevar == "2":
  print(colored("!!Warning!! : Dont Spam This Command! We have no responsibility for this issue." , "yellow" , "on_red")) 
  continue2 = input("Do You Want To Continue? (Y/N) : ") 
  if (continue2 == "y" or "Y"):
    run("bots/2.py")   

if choosevar == "3":
  print(colored("!!Warning!! : No Warning For This Command Just Enjoy <:" , "yellow" , "on_red")) 
  continue2 = input("Do You Want To Continue? (Y/N) : ") 
  if (continue2 == "y" or "Y"):
    run("bots/3.py")   




