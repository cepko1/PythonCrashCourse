import unittest
from city import country_city

class CityTestCase(unittest.TestCase):
	def test_city_country(self):
		self.assertEqual(country_city('New-York','USA'),'New-York, USA')

if __name__ == '__main__':
	unittest.main()