from sympy import *
from sympy.plotting import plot
from sympy.solvers.inequalities import solve_univariate_inequality

# Данный код я запускал на https://colab.research.google.com
# Было интересно посмотреть как это будет на VSC.

x = Symbol('x')
y = Symbol('y')
# x = -1.038
# y = 3**0.5
t = (2*x + 3*y)**2 - 3*x*(4/3*x+4*y)
print(simplify(t))

f = (x+2)**0.5*(x**2+3*x-4)
print(solve(f))
plot(f)

f = 2*x**2+x+10

plot(f)

f = 6*x/(3*x**2-2*x+5)+5*x/(3*x**2-3*x+5)-2
print(solve(f))
plot(f)
