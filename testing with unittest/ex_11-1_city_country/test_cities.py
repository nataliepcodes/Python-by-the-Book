# write a method called test_city_country() to verify that calling the function 
# with the with givem values (e.g. santiago, chile) will result in the correct string
# run test_cities.py and ensure test_city_country() passes

import unittest
from city_functions import get_city_country

class CityCountryTestCase(unittest.TestCase):
    """Test for 'city_functions.py' """

    def test_city_country(self):
        """Does the string return this format for city and country 'Santiago, Chile'."""
        string = get_city_country('santiago', 'chile')
        self.assertEqual(string, 'Santiago, Chile')

# variable 'name' is set when the program is executed
# if this file is run as the main program then the 'name' is set to 'main'
# in that case, a call is made to unittest.main() that runs the test
# if the file is imported with the testing framework then the value of 'name' is not 'main' and this block will not be executed
if __name__ == '__main__':
    unittest.main()