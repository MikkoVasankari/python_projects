import unittest
import calculator

class MyTest(unittest.TestCase):
    
    def test_CalculatesSumOfIntegers_Value1_and_Value2_And_AssingValueToResult(self):
        # Arrange
        val1 = int(4)
        val2 = int(3)

        # Act
        result = calculator.addition(val1,val2)

        # Assert
        self.assertEqual(8,result)
    
    def test_CalculateRemainderOfIntegers_Value1_and_Value2_And_AssingValueToResult(self):
        # Arrange
        val1 = int(8)
        val2 = int(3)

        # Act
        result = calculator.subtraction(val1,val2)

        # Assert
        self.assertEqual(2,result)

    def test_CalculateMultiplicationOfIntegers_Value1_and_Value2_And_AssingValueToResult(self):
        # Arrange
        val1 = int(8)
        val2 = int(3)

        # Act
        result = calculator.multiplication(val1,val2)

        # Assert
        self.assertEqual(2,result)

    def test_CalculateDivisionOfIntegers_Value1_and_Value2_And_AssingValueToResult(self):
        # Arrange
        val1 = int(8)
        val2 = int(6)

        # Act
        result = calculator.division(val1,val2)

        # Assert
        self.assertEqual(2,result)
    
if __name__ == '__main__':
    unittest.main()