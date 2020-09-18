import math

# input funcao
def funcao (x):
	return pow(x,3) - (9 * x) + 3

def bisseccao(inter_1,inter_3, limite):
	k = 1
	inter_2 = float((inter_1 + inter_3) / 2)

	value_1 = float(funcao(inter_1))
	value_3 = float(funcao(inter_3))
	value_2 = float(funcao(inter_2))
 
	if(value_1 < 0 and value_3 < 0):
		print("Impossivel Calcular")
		return 

	aux_2 = value_2
	if(aux_2 < 0): aux_2 = aux_2 * -1
	
	while(aux_2 >= limite):
     
		if(value_2 > 0):
			inter_1 = inter_2
		else:
			inter_3 = inter_2

		value_1 = float(funcao(inter_1))
		value_3 = float(funcao(inter_3))

		inter_2 = float((inter_1 + inter_3) / 2)

		value_2 = float(funcao(inter_2))
		if(value_2 < 0): aux_2 = value_2 * -1
	return(value_2)
