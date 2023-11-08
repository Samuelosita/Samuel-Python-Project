""" 
formulas
simple interest: p(1+rt)
compound interest: p (1+r/n)^nt
"""

p = float(input('Enter Initial principal'))
r = float(input('Enter interest rate'))
t = float(input('Enter number of time periods elapsed'))
n = float(input('Enter number of times interest applied per time period'))

si = p*(1 + r * t)
ci = p*(1 + r/n) ** n*t

# print(f"Yusuf & Sons {si}")
print(f"Yusuf & Sons {ci}")
