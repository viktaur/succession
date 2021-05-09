import math

p0 = eval(input('(p0) Percentage of positive ratings (please express it over 1): '))
n = eval(input('(n) Number of reviews: '))
n0 = n * p0

p = (n0 + 1) / (n + 2)

print('The probability that you will have a positive experience is: ' + str(p) + ' or ' + str("{:.2%}".format(p)))