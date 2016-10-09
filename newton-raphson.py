 #from math import *
from pylab import *
from sympy import diff
from sympy.abc import x

def newton(funcion, df, vi, TOL, N,vectorx,vectory):

    i = 0
    while i<N:

        vectorx[i] = vi
        x = vi
        f = eval(funcion)
        df_val = eval(df)
        vectory[i] = f

        if df_val == 0:
            print ("La evaluacion de la derivada de la funcion dio 0")
            return 1

        p1 = vi - (f / df_val)

        if fabs(vi-p1) < TOL:
            print ("La raiz buscada es: ", vi, "con", i + 1, "iteraciones")
            return 1

        i += 1
        vi = p1

    return 0
def dibujar(funcion, vi,vectorx,vectory):
    x = arange(vi - 5, vi + 5, 0.1)

    subplot(211)
    plot(x, eval(funcion), linewidth=1.0)
    xlabel('X')
    ylabel('Y')
    title(' f(x)=' + funcion)
    grid(True)
    axhline(linewidth=1, color='r')
    axvline(linewidth=1, color='r')

    subplot(212)
    plot(vectorx, vectory, 'k.')
    xlabel('X')
    ylabel('Y')
    grid(True)
    axhline(linewidth=1, color='r')
    axvline(linewidth=1, color='r')

    show()


print (" Metodo de Newton-Raphson\n")
while True:git
    vectorx = zeros(100, float)
    vectory = zeros(100, float)

    funcion = input("Introduce la funcion \n")
    df= str(diff(funcion,x))
    print(df)
    vi = float(input("Introduce el valor inicial\n"))
    TOL = float(input("Introduce la tolerancia del metodo\n"))
    r =newton(funcion, df, vi, TOL, 100,vectorx,vectory)

    if r==0:
        print("La funcion no toca el eje X")
    dibujar(funcion, vi,vectorx,vectory)

    exit = input("¿Quieres calcular otra vez? yes/no :  ")
    if exit == "no":
        break
