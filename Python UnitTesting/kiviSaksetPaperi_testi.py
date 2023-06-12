import unittest
import kiviSaksetPaperi

# Mikko Vasankari

class kiviSaksetPaperiTest(unittest.TestCase):
    
    def test_IfInputIsntRockPaperOrScissors(self):
        # Arrange
        Input1 = "testi"
        Input2 = "kivi" 

        # Act
        result = kiviSaksetPaperi.peli(Input1,Input2)

        # Assert
        self.assertEqual("Vääränlainen syöte (Valitse/kirjoita joko kivi, paperi tai sakset)",result)

    def test_IfInputIsANumber(self):
        # Arrange
        Input1 = 5
        Input2 = "kivi" 

        # Act
        result = kiviSaksetPaperi.peli(Input1,Input2)

        # Assert
        self.assertEqual("Vääränlainen syöte (Valitse/kirjoita joko kivi, paperi tai sakset)",result)

    def test_IfRockwinsScissors(self):
        # Arrange
        Input1 = "kivi"
        Input2 = "sakset" 

        # Act
        result = kiviSaksetPaperi.peli(Input1,Input2)

        # Assert
        self.assertEqual("Voitit pelin",result)
        
    def test_IfScissorsWinsPaper(self):
        # Arrange
        Input1 = "sakset"
        Input2 = "paperi" 

        # Act
        result = kiviSaksetPaperi.peli(Input1,Input2)

        # Assert
        self.assertEqual("Voitit pelin",result)

    def test_IfPaperWinsRock(self):
        # Arrange
        Input1 = "paperi"
        Input2 = "kivi" 
        
        # Act
        result = kiviSaksetPaperi.peli(Input1,Input2)

        # Assert
        self.assertEqual("Voitit pelin",result)

    def test_IfGameIsATie(self):
        # Arrange
        Input1 = "kivi"
        Input2 = "kivi" 

        # Act
        result = kiviSaksetPaperi.peli(Input1,Input2)

        # Assert
        self.assertEqual("Tasapeli",result)            

if __name__ == '__main__':
    unittest.main()

    # Mikko Vasankari
