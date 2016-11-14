import scipy
#import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

n=int(input('Numero de puntos que se tienen: '))
x =[0]*n
y =[0]*n
for i in range(n):
    x[i]=float(input('Dame los valores de x:'))
for i in range(n):
    y[i]=float(input('Dame los valores de y:'))

#x = scipy.array([-1.5,-0.75,0,0.75,1.5])
#y = scipy.array([-14.1014,-0.931596,0,0.931596,14.1014])
result = scipy.poly1d([0.0])  # setting result = 0

for i in range(0, n):
    temp_numerator = scipy.poly1d([1.0])
    denumerator = 1.0
    for j in range(0, n):
        if i != j:
            temp_numerator *= scipy.poly1d([1.0, -x[j]])
            denumerator *= x[i] - x[j]
    result += (temp_numerator / denumerator) * y[i]

print("The result is: ")
print(result)

x_val = np.arange(min(x), max(x) + 1, 0.1)
plt.xlabel('x');
plt.ylabel('p(x)')
plt.grid(True)
for i in range(0, len(x)):
    plt.plot([x[i]], [y[i]], 'ro')  # plot the points
plt.plot(x_val, result(x_val))
plt.axis([min(x) - 1, max(x) + 1, min(y) - 1, max(y) + 1])
plt.show()