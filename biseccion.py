import math as mt
from pylab import*

def main():

    biseccion();


def biseccion():

	A=C=I=G=Cp=B=0;
	f=input('Digite la función: ');
	graficar(f);
	A=float(input('Digita el valor de A: '));
	C=float(input('Digita el valor de C: '));
	#N=float(input('Digita el numero de iteraciones: '));
	Cp=float(input('Digite el error: '));


	Er=float(Cp+1);
	N=int((mt.log(B-A)-mt.log(Cp))/mt.log(2))
	x=A;
	fA=eval(f);

	x=C;
	fC=eval(f);

	if(fA*fC>0):

		print('No existen Raíces en esta Ecuación');
	else:
		while(Er>Cp and I<N):
			I=I+1;
			Ant=B;
			G=A+C;
			B=G/2;

			x=B;
			fB=eval(f);

			if(fA*fB<=0):

				C=B;

				fC=fB;

			else:

				A=B;
				fA=fB;

			Er=abs(((B-Ant) /B)*100);
			print('xi= %.6f\txd= %.6f\txm= %.7f\tfxm= %.6f\ttEr= %.4f%%'%(A,B,C,fB,Er));
		print('\n\nLa Raíz es: %.8f'%B);






def graficar(f):
    	datos=[0]*12
    	datosy=[0]*12
    	i=0
    	for y in range(0,12):
    		x = y
    		datos[i]=float( eval(f))
    		datosy[i]=i
    		i+=1

    	plt.plot(datosy,datos)
    	plt.title("Funcion "+str(f))   # Establece el título del gráfico
    	plt.xlabel("X")   # Establece el título del eje x
    	plt.ylabel("Y")   # Establece el título del eje y
    	plt.ioff()        #quita la iteractividad de la grafica
    	plt.axis([-12, 12, -4, 4])
    	plt.grid(True)    #crea el gridpane
    	plt.show()        #aparece el gridpane

if __name__=="__main__":

    main();
