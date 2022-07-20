# write a method called test_city_country() to verify that calling the function 
# with given values (e.g. santiago, chile) will result in the correct string
# run test_cities.py and ensure test_city_country() passes
# write a second test called test_city_country_population that verifies that test passes with values
# 'Santiago, Chile, population=5000000'

import unittest
from city_functions import get_city_country

class CityCountryPopulationTestCase(unittest.TestCase):
    """Test for 'city_functions.py' """

    def test_city_country(self):
        """Does the string return this format: 'Santiago, Chile'?"""
        string = get_city_country('santiago', 'chile')
        self.assertEqual(string, 'Santiago, Chile')
    
    def test_city_country_population(self):
        """Does the string return this format: 'Santiago, Chile - population 5000000'?"""
        string = get_city_country('santiago', 'chile', 5000000)
        self.assertEqual(string, 'Santiago, Chile - population 5000000')
    

# variable 'name' is set when the program is executed
# if this file is run as the main program then the 'name' is set to 'main'
# in that case, a call is made to unittest.main() that runs the test
# if the file is imported with the testing framework then the value of 'name' is not 'main' and this block will not be executed
if __name__ == '__main__':
    unittest.main()