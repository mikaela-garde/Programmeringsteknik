import numpy as np

#UPPGIFT 5

def f(x):
    return x/((x**2)+4)**(1/3)

def g(x):
    return x**(1/2)*np.log(x)


def riemann_sum(a, b, function, n):
    dx = (b-a)/n
    sum = 0
    for i in range(n):
        sum += function(a+dx*i)*dx
    return sum

def error(integral, riemann):
    print("Felet blir:" + str(integral-riemann))

integral_f = 3-3/(2**(2/3))
integral_g = (16*np.log(4))/3-28/9

riemann_f = riemann_sum(0, 2 , f, 100)
print("Riemannsumma f:" + str(riemann_f))
error(integral_f, riemann_f)

riemann_g = riemann_sum(1, 4, g, 100)
print("Riemannsumma g:" + str(riemann_g))
error(integral_g, riemann_g)

