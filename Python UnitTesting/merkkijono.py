
import re

def laske(value):

    if value == "":
        return int (0)
    if value == "0":
        return int (0)

    if len(value) > 1:
        
        summ = 0
        luku = re.split(",|\n", value)

        for x in luku:
            summ = summ + int(x)

            if int(x) < 0:
                return "EI"

            if int(x) >= 1000:
                summ = summ - int(x)
               
        return summ

    return  int(value)

   