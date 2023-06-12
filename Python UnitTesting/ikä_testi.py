import unittest
import ikä

class ikä_testaaja(unittest.TestCase):

    def test_IkäLapsi(self):
         # Arrange
        val1 = int(10)

        # Act
        result = ikä.ikäTarkistaja(val1)

        # Assert
        self.assertEqual("Olet lapsi",result)

    def test_IkäAikuinen(self):
         # Arrange
        val1 = int(25)

        # Act
        result = ikä.ikäTarkistaja(val1)

        # Assert
        self.assertEqual("Olet aikuinen",result)

    def test_IkäEläkeläinen(self):
         # Arrange
        val1 = int(80)

        # Act
        result = ikä.ikäTarkistaja(val1)

        # Assert
        self.assertEqual("Eläkeläinen!!!",result)


if __name__ == '__main__':
    unittest.main()        


    # Mikko Vasankari