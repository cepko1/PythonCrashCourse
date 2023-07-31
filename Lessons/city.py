def country_city(city, country, population = ''):
	if population:
		return city +', ' + country + ' - population '+ population
	else:
		return city +', ' + country