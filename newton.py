import math

def funcao (x):
	return pow(x,2) + x - 6

def derivada(x):
	return 2*x + 1

def newton(xo,limite):	
	f = funcao(xo)

	f_aux = f
	if(f_aux < 0): f_aux = f * - 1

	while(f_aux > limite):
		x = xo - (funcao(xo)/derivada(xo))

		f = funcao(x)
		f_aux = f
		if(f_aux < 0): f_aux = f * - 1
		xo = x
	
	return x