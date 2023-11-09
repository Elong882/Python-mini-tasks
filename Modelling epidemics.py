import math   # formula uses exponent, import math for accuracy
n = float(input('n? '))  # peak number of patients in hospital
mu = float(input('mu? '))   # mean of n
sigma = float(input('sigma? '))  # standard deviation 
x = int(input('x? '))   # integer 0-56 (up to 8 weeks)

# f (x) is pdf of the normal distribution
while x >= 0 and x < 57:
    formula =  - ((x - mu) ** 2) / (2 * (sigma ** 2))
    formula2 = n * math.exp(formula)
    result = round(formula2)  # round the result up or down
    print(f'Estimated number of cases on day {x} is {result}')       
    break  # while loop used for break 