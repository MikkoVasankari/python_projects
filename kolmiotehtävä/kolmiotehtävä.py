import random

import matplotlib.pyplot as plt


def toimii():

    a = [10, 10]
    b = [100, 10]
    c = [50, 100]

    plt.plot(a[0], a[1], 'ro')
    plt.plot(b[0], b[1], 'ro')
    plt.plot(c[0], c[1], 'ro')

    plt.axis([0, 120, 0, 120])

    arvottuX = random.randint(1, 100)
    arvottuY = random.randint(1, 100)

    coor = [arvottuX, arvottuY]

    def onko_kolmiossa(a, b, c, coor):
        a1 = a[0]
        a2 = a[1]
        b1 = b[0]
        b2 = b[1]
        c1 = c[0]
        c2 = c[1]

        x = coor[0]
        y = coor[1]

        if (a1 == x and a2 == y) or (b1 == x and b2 == y) or (c1 == x and c2 == y):
            print("kulmapiste")
            return False

        d1 = (b1-a1)*(y-a2)-(b2-a2)*(x-a1)
        d2 = (c1-b1)*(y-b2)-(c2-b2)*(x-b1)
        d3 = (a1-c1)*(y-c2)-(a2-c2)*(x-c1)
        if (d1 < 0 and d2 < 0 and d3 < 0) or (d1 > 0 and d2 > 0 and d3 > 0):
            return True
        else:
            return False

    if onko_kolmiossa(a, b, c, coor) == True:
        plt.plot(arvottuX, arvottuY, 'ko')

        # print(coor)

        # Kulman arvonta
        kulma = random.randint(1, 3)

        def mika_kulma(kulma):
            if kulma == 1:
                return 1
            if kulma == 2:
                return 2
            if kulma == 3:
                return 3

        arvottu = mika_kulma(kulma)
        # print(arvottu)

        # Arvotun pisteen ja arvotun kulman puoliväli
        def puolivali(arvottu):

            if arvottu == 1:
                x = (coor[0] + a[0])/2
                y = (coor[1] + a[1])/2

                uusipiste = [x, y]
                if onko_kolmiossa(a, b, c, uusipiste) == True:
                    plt.plot(uusipiste[0], uusipiste[1], 'ko')
                    return uusipiste

            if arvottu == 2:
                x = (coor[0] + b[0])/2
                y = (coor[1] + b[1])/2

                uusipiste = [x, y]
                if onko_kolmiossa(a, b, c, uusipiste) == True:
                    plt.plot(uusipiste[0], uusipiste[1], 'ko')
                    return uusipiste

            if arvottu == 3:
                x = (coor[0] + c[0])/2
                y = (coor[1] + c[1])/2

                uusipiste = [x, y]
                if onko_kolmiossa(a, b, c, uusipiste) == True:
                    plt.plot(uusipiste[0], uusipiste[1], 'ko')
                    return uusipiste


toistojenmaara = 0

while toistojenmaara < 200:
    toistojenmaara += 1
    toimii()

plt.show()
