reales=[1.0,2.0,3.0] # Arreglo de reales, (promedio:6.0/3.0=2.0)
sum: int =0 # inicializar suma en 0

for i in reales: #Recorre la lista
  sum+=i    #Se almacena la sumatoria de los elementos del arreglo
Promedio= sum/len(reales)  #Se divide la suma total por la cantidad de elementos del arreglo
print(Promedio)   #Se imprime el promedio, (2.0)