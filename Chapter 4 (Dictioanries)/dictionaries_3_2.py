people_one = {'Frank' : 'football', 'Eric' : 'programing', 'Jesica' : 'sex'}
people_two = {'Garry' : 'films', 'Elon' : 'robotics', 'Edmond' : 'hight technology'}
people_three = {'Kamila' : 'dance', 'Lucy' : 'brain traning', 'Patric' : 'cartoons'}

people = [people_one, people_two, people_three]
for p in people:
	for d in p:
		print(d + ' : ' + p[d])
		
favorite_countries = {'Joahn' : ['Scotland', 'Switzerland'], 'Jack' : ['Croatia', 'Ukraine'], 'Jahn' : ['France', 'Grece']}
for n in favorite_countries:
	for p in favorite_countries[n]:
		print(n + " wants to invite " + p)
	
cities = {'London' : {'country' : 'Great Britan', 'population' : '8 millions', 'founded' : '43 a.c'}, 'Madrid' : {'country' : 'Spain', 'population' : '3 miilions', 'founded' : '10 century'}, 'Rome' : {'country' : 'Italy', 'population' : '4 millions', 'founded' : '753 a.c'}}
for city, city_info in cities.items():
	print('City : ' + city)
	print('Country : ' + city_info['country'])
	print('Population : ' + city_info['population'])
	print('Founded : ' + city_info['founded'])
	print('----------------')
