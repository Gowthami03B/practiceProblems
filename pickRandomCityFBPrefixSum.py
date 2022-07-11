"""
Given a list of city names and their corresponding populations, write a program to output a random city name subject to the following constraint: the probability of the program to output a city's name is based on its population divided by the sum of all cities' population. Assume the program will be repeatedly called many times.

For example:

NY: 7
SF: 5
LA: 8
The probability to generate NY is 7/20, SF is 1/4, LA - ⅖

Prefix sum array
7	5	8
7	12	20
NY	SF	LA
"""
#BRUTEFORCE
import random
def getRandomCity(city_map)-> str:
    city_sample_set = []
    for city, population in city_map.items():
        for i in range(population):
            city_sample_set.append(city)#creating a sample set resembling the probability
    print(city_sample_set)
    return random.choice(city_sample_set)
    
city_map = {'NY':7,'SF':5,'LA':8}
# print(getRandomCity(city_map))

#Optimized - Prefix sum, instead of creating a sample set, we can assign ranges, say pick a random no betwee
#sum of total population and if you pick < 7, NY, 8-12, SF and 13-20,LA
def getRandomCityOptimal(city_map) -> str:
    prev = 0
    inverse_city_map = {}
    
    for city, population in city_map.items():
        population += prev
        city_map[city] = population
        prev = population
    for city, population in city_map.items():
        inverse_city_map[population] =city
    print(inverse_city_map)
    random_int = random.randint(1, 20)
    for population, city in inverse_city_map.items():
        if random_int <= population:
            print(random_int,city)
            return city
city_map = {'NY':7,'SF':5,'LA':8}
print(getRandomCityOptimal(city_map))
