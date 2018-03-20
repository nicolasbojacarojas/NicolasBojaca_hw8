import numpy as np
#Funcion que genera y retorna numeros aleatorios
def sample_1(N):
	return np.random.choice(a = [-10, -5, 3, 9], size = N, p = [0.1, 0.4, 0.2, 0.3]) 
	
#Funcion que genera y retorna numeros aleatorios bajo la distribución de probabilidad con beta = 0.5
def sample_2(N):
	return np.random.exponential(0.5, N)
#Funcion que genera  y retorna primedios dada una funcion de sampleo, le entran parametros de la funcion, el tamaño del arreglo que devuelve y la cantidad de promedios a generar que se muestran en un array
def get_mean(sampling_fun, N, M):
	a = []
	for i in range(M):
		a.append(np.mean(sampling_fun(N)))
	return (np.array(a))
#m es una variable que representa la cantidad de promedios que quiero que arroje la funcion get_mean
m = 1000
#Tamaño del arreglo que deben arrojar las funciones sample_1 y sample_2
N =[10, 100, 1000]
#Iteraciones realizadas para generar los archivos txt, que contienen los promedios dados un N. 
for i in range(len(N)):
	np.savetxt('sample_1_'+str(N[i]), get_mean(sample_1, N[i], m))
	np.savetxt('sample_2_'+str(N[i]), get_mean(sample_2, N[i], m))

