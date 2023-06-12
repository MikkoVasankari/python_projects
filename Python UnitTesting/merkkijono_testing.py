import unittest
import merkkijono


class kiviSaksetPaperiTest(unittest.TestCase):
    
    def test_IfEmptyInputReturn0(self):
        # Arrange
        Input1 = ""

        # Act
        result = merkkijono.laske(Input1)

        # Assert
        self.assertEqual(0,result)

    def test_If0returns0(self):
        # Arrange
        Input1 = "0"

        # Act
        result = merkkijono.laske(Input1)

        # Assert
        self.assertEqual(0,result)

    def test_If1returns1(self):
        # Arrange
        Input1 = "1"

        # Act
        result = merkkijono.laske(Input1)

        # Assert
        self.assertEqual(1,result)
    
    def test_If1Plus1Is2(self):
        # Arrange
        Input1 = "1,1"

        # Act
        result = merkkijono.laske(Input1)

        # Assert
        self.assertEqual(2,result)

    def test_If3Plus4Is7(self):
        # Arrange
        Input1 = "3,4"

        # Act
        result = merkkijono.laske(Input1)

        # Assert
        self.assertEqual(7,result)    

    def test_If2Plus7Plus4Is13(self):
        # Arrange
        Input1 = "2,7,4"

        # Act
        result = merkkijono.laske(Input1)

        # Assert
        self.assertEqual(13,result)

    def test_If5Plus5Plus5PLus4Is19(self):
        # Arrange
        Input1 = "5,5,5,4"

        # Act
        result = merkkijono.laske(Input1)

        # Assert
        self.assertEqual(19,result)

    def test_IfValueGreaterThan1000DontAdd(self):
        # Arrange
        Input1 = "3,1001"

        # Act
        result = merkkijono.laske(Input1)

        # Assert
        self.assertEqual(3,result)

    def test_IfValueIsNegative(self):
        # Arrange
        Input1 = "-1"

        # Act
        result = merkkijono.laske(Input1)

        # Assert
        self.assertEqual("EI",result)

    def test_If3Minus1IsError(self):
        # Arrange
        Input1 = "3,-1"

        # Act
        result = merkkijono.laske(Input1)

        # Assert
        self.assertEqual("EI",result)

    def test_IfKauttaNtoimiiKuinPilkku(self):
        # Arrange
        Input1 = "1\n2,3"

        # Act
        result = merkkijono.laske(Input1)

        # Assert
        self.assertEqual(6,result)                 

if __name__ == '__main__':
    unittest.main()
