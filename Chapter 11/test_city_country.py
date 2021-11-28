import city_functions
import unittest

class CountryNameTest(unittest.TestCase):
    """Tests for 'city_functions.py'"""

    def test_first_formatting_name(self):
        """Tests formatted_city_info without population"""
        city_info = city_functions.formatted_city_info('santiago', 'chile')
        self.assertEqual(city_info, 'Santiago, Chile')
    
    def test_second_formatting_name(self):
        """Tests formatted_city_info with population"""
        city_info = city_functions.formatted_city_info('santiago', 'chile', 5000000)
        self.assertEqual(city_info, 'Santiago, Chile - population 5000000')

if __name__ == '__main__':
    unittest.main()