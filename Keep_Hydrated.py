'''
Description:

    Nathan loves cycling.

    Because Nathan knows it is important to stay hydrated, he drinks 0.5 litres of water per hour of cycling.

    You get given the time in hours and you need to return the number of litres Nathan will drink, rounded to the smallest value.

For example:

    time = 3 ----> litres = 1

    time = 6.7---> litres = 3

    time = 11.8--> litres = 5

'''
import math

def litres(time):
    return math.floor(time * 0.5)

print(litres(3))
print(litres(6.7))

'''
This problem can actually use floor division which in python its is just //

return time // 2

'''
