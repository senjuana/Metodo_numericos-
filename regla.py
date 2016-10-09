import sys
import random
sys.setrecursionlimit(100000)

def f(x):
	return (2*x**2)-(10*x)-20
def regula(a,b,mi,eps):
	a = float(a)
	b = float(b)
	c =((f(b)*a)-(f(a)*b))/(f(b)-f(a))

	if(abs(f(c)) >= eps and mi > 0):
		mi = mi-1
		if((f(c)*f(a))<0):
			return regula(a,c,mi,eps)
		if((f(c)*f(b))<0):
			return(c,b,mi,eps)
	if((abs(f(c)))<0):
		return [c,mi]

if __name__=="__main__":
	r=regula(random.random(),random.random(),100,10**-3)
	if(r!=None):
		#print("se emplearon "+str(1000-r[1])+ "iteraciones\n")
		print("tr= "+str(r[0])+"\t")
		print("tf= ("+str(r[0])+")  = "+ str(f(r[0])) +"\t")
