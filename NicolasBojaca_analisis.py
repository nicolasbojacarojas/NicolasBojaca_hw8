import numpy as np
import matplotlib.pyplot as plt
#Variables que guarada la primera parte de los nosmbres de los archivos para cargarlos, 
d = "sample_1_"
e = "sample_2_"
#Funcion que devuelve un arreglo con los valores del arreglo de los archivos cargados, la media de estos datos y su desviacion estandar, ambas normalizadas
def normal_dist (x, mean, sigma):
	a = x/np.std(x)*sigma
	b = (x-np.mean(x))+mean
	return (np.array([x, a, b]))
#Funcion quecarga los archivos y a la vez genera los histogramas para cada uno de estos. 
def get_fit():
	N = [10, 100, 1000]
	for i in range(len(N)):
		files = np.loadtxt(d+str(N[i])+".txt")
		files2 = np.loadtxt(e+str(N[i])+".txt")
		np.histrogram(files)

