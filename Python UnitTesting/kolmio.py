
def tarkistaKolmio(value1, value2, value3):
    if (value1 == value2 == value3):
        return("Tasasivuinen kolmio")
    if (value1 == value2 or value1 == value3 or value2 == value3):
        return("Tasakylkinen kolmio")
    else:
        return("Epäsäännöllinen kolmio!")


# Mikko Vasankari