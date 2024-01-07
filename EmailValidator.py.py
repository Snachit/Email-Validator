import re
from pyfiglet import *



entre = True
while entre:
    text = "menu"

    fig = Figlet(font="rounded" )


    ascii_art = fig.renderText(text)

    print(ascii_art)
    print("""
1- USE PROGRAMME
2-QUITTE THE PROGRAMME!
""")
    choice = int(input("Enter your choice:"))
    choice = str(choice)
    if choice == '1': 
        txt = input("Entry Your Email:")

        x =re.findall("^[A-z0-9\.]+@(gmail|hotmail|Outlook|Yahoo)+\.(com|ma)$", txt)

        if x:
            text = "Email Valide"
            ascii_art = Figlet().renderText(text)
            print(ascii_art)
            print("----------------------------------------------------")
            print("----------------------------------------------------")

        else:
            text = "Invalide Email!"
            ascii_art = Figlet().renderText(text)
            print(ascii_art)
            print("----------------------------------------------------")
            print("----------------------------------------------------")

    elif choice == '2' :
        text = "GOOD BY!"
        ascii_art = Figlet().renderText(text)
        print(ascii_art)
        entre = False
    else:
       text = "INVALIDE CHOICE!"
       ascii_art = Figlet().renderText(text)
       print(ascii_art)
       print("----------------------------------------------------")
       print("----------------------------------------------------")