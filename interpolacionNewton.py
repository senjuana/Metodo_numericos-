n=int(input('Numero de puntos que se tienen: '))

x=[0]*n
y=[0]*n

for i in range(n):
    x[i]=float(input('Dame los valores de x:'))
for i in range(n):
    y[i]=float(input('Dame los valores de Fx:'))

print("X:",x)
print("FX:",y)

matriz = [0.0] * n
for i in range(n):
    matriz[i] = [0.0] * n

vector = [0.0] * n

#x = [0,1,3,6]
#y = [-3,0,5,7]
#x = [1,5,20,40]
#y = [56.5,113,181,214.5]
#x=[-2,-1,0,2,3,6]
#y=[-18,-5,-2,-2,7,142]


for i in range(n): #vacio a los nuevos vectores
    vector[i]=x[i]
    matriz[i][0]=y[i] #matriz del demonio

for i in range(1,n):
    for j in range(i,n):
        result= ((matriz[j][i-1]-matriz[j-1][i-1]) / (vector[j]-vector[j-i]))
        matriz[j][i] = result
        print("Nivel[",i,"] = ",result)
    print("\n")


punto_a_evaluar = int(input('Dame el punto a evaluar: '))

aprx = 0
mul = 1.0
for i in range(n):
    print("[",i,"]","=",matriz[i][i])
    mul = matriz[i][i];
    #print("mul antes del ciclo j=",mul)
    for j in range(1,i+1):
        mul = mul * (punto_a_evaluar - vector[j-1])
        #print("mul en el ciclo j=",mul)
    aprx = aprx + mul


print("\n")
print("El valor aproximado de f(",punto_a_evaluar,") es: ", aprx)