import amazon

n = eval(input('(n) Number of times that the experiment has been made: '))
n0 = eval(input('(n0) Number of times that the experiment has resulted favorable: '))
p0 = n0 / n

p = (n0 + 1) / (n + 2)

print('The probability that the next experiment results favorable is: ' + str(p) + ' or ' + str("{:.2%}".format(p)))