import unittest
import kolmio

# Mikko Vasankari

class kolmio_Testaus(unittest.TestCase):
    
    def test_IfTriangleAllSidesAreEqual(self):
        # Arrange
        val1 = int(1)
        val2 = int(2)
        val3 = int(3)
                
        # Act
        result = kolmio.tarkistaKolmio(val1,val2,val3)

        # Assert
        self.assertEqual("Tasasivuinen kolmio",result)

    def test_IfTriangleTwoSidesAreEqual(self):
        # Arrange
        val1 = int(1)
        val2 = int(4)
        val3 = int(2)
        
        # Act
        result = kolmio.tarkistaKolmio(val1,val2,val3)

        # Assert
        self.assertEqual("Tasakylkinen kolmio",result)

    def test_IfTriangleAllSidesAreDifferent(self):
        # Arrange
        val1 = int(2)
        val2 = int(2)
        val3 = int(2)
        
        # Act
        result = kolmio.tarkistaKolmio(val1,val2,val3)

        # Assert
        self.assertEqual("Epäsäännöllinen kolmio!",result)

if __name__ == '__main__':
    unittest.main()

    # Mikko Vasankari