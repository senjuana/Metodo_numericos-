import math as mt
n=int(input('Numero de puntos que se tienen: '))

x=[0]*n
y=[0]*n

for i in range(n):
    x[i]=float(input('Dame los valores de x:'))
for i in range(n):
    y[i]=float(input('Dame los valores de Fx:'))

#print("X:",x)
#print("FX:",y)

matriz = [0.0] * n
for i in range(n):
    matriz[i] = [0.0] * n

vector = [0.0] * n

#x = [50,60,70,80,90,100]
#y = [24.94,30.11,36.05,42.84,50.57,59.30]
#x = [1,5,20,40]
#y = [56.5,113,181,214.5]
#x=[-2,-1,0,2,3,6]
#y=[-18,-5,-2,-2,7,142]


for i in range(n): #vacio a los nuevos vectores
    vector[i]=x[i]
    matriz[i][0]=y[i] #matriz del demonio

for i in range(1,n):
    for j in range(i,n):
        result= ((matriz[j][i-1]-matriz[j-1][i-1]))
        matriz[j][i] = result
        print("Nivel[",i,"] = ",result)
    print("\n")


punto_a_evaluar = int(input('Dame el punto a evaluar: '))

#evaluacion del punto
i=0
while(punto_a_evaluar>vector[i]):
    i+=1

#multiplicacion por el polinomio
c=0
mul=matriz[0][0]
s=(punto_a_evaluar-vector[0])/10
while(c<i):
    print("[", c, "]", "=", matriz[c][c])
    if(c!=0):
        mul+=s*matriz[c][c]
    c+=1

print("El valor interpolado hacia enfrente primer forma: "+str(mul))
print("\n")


#multiplicacion por el polinomio2 factorial
c=1
mul=matriz[0][0]
print("[", 0, "]", "=", matriz[0][0])
while(c<i+1):
    print("[", c, "]", "=", matriz[c][c])
    if(c==1):
        mul+=s*matriz[c][c]
    mul+=(s*(s-1))/mt.factorial(i+1)
    c+=1


print("El valor interpolado hacia enfrente segunda forma: "+str(mul))
print("\n")






#evaluacion del punto
i=n-1
while(punto_a_evaluar<vector[i]):
    i-=1

#multiplicacion por el polinomio
c=n-1
j=0
mul=matriz[c][j]
s=(punto_a_evaluar-vector[c])/20
print(punto_a_evaluar)
print(vector[c])
print(punto_a_evaluar-vector[c])
q=punto_a_evaluar-vector[c]
print (q)
print(2/10)
print(s)
f=float(q/10)
print(f)

while(c>i-1):
    print("[", c, "]", "=", matriz[c][j])
    if(c!=n-1):
        mul-=s*matriz[c][j]
    c-=1
    j+=1

print("El valor interpolado hacia atras primer forma: "+str(mul))
print("\n")

