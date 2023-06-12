import random

print("Kivi, paperi, sakset? (Valitse/kirjoita joko kivi, paperi tai sakset)")
#käyttäjä = input()

mahdolliset_valinnat = ["kivi", "paperi", "sakset"]

robotti = random.choice(mahdolliset_valinnat)

def peli(käyttäjä, robotti):
    if (käyttäjä == robotti):
        return ("Tasapeli")
    
    elif (käyttäjä == "kivi" and robotti == "sakset"):
        return ("Voitit pelin")

    elif (käyttäjä == "sakset" and robotti == "paperi"):
        return ("Voitit pelin")

    elif (käyttäjä == "paperi" and robotti == "kivi"):
        return ("Voitit pelin")

    elif (käyttäjä != "kivi" or käyttäjä != "paperi" or käyttäjä != "sakset"):
        return("Vääränlainen syöte (Valitse/kirjoita joko kivi, paperi tai sakset)")

    else:
        return ("Hävisit pelin")
       
#peli(käyttäjä,robotti)


# Mikko Vasankari