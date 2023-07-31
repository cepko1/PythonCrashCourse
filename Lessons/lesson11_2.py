import unittest
from city import country_city

class CityTestCase(unittest.TestCase):
	
	def test_city_country(self):
		self.assertEqual(country_city('New-York','USA'),'New-York, USA')
		
	def test_city_country_pipulation(self):
		self.assertEqual(country_city('Kyiv','Ukraine', '3000000'),'Kyiv, Ukraine - population 3000000')

if __name__ == '__main__':
	unittest.main()