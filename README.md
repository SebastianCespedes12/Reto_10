# Reto_10
>#### 1.Desarrollar un algoritmo que calcule el promedio de un arreglo de reales.

```python
reales=[1.0,2.0,3.0] # Arreglo de reales 
sum: int =0 # inicializar suma en 0

for i in reales: #Recorre la lista
  sum+=i    #Se almacena la sumatoria de los elementos del arreglo
Promedio= sum/len(reales)  #Se divide la suma total por la cantidad de elementos del arreglo
print(Promedio)   #Se imprime el promedio, (2.0)
```
>#### 2.Desarrollar un algoritmo que calcule el producto punto de dos arreglos de números enteros (reales) de igual tamaño.

```python
Vector1=[1.0,2.0,3.0] # Arreglo de reales
Vector2=[2.0,5.0,7.0] # Arreglo de reales de igual tamaño
sum:int =0 #Inicializa la suma en 0

if len(Vector1)== len(Vector2): #Se verifica que los arreglos sean de igual tamaño, si lo son:
  for i in Vector1: #Se recorre el primer arreglo
    for j in Vector2: #Se recorre el segundo arreglo 
      if Vector1.index(i)==Vector2.index(j): # Se verifica que los indices de los arreglos coincidan
        sum+=i*j     #Si coinciden, se multiplican y se suman a la varibale sum
  print(f"El producto punto es igual a: {sum}") # Se imprime el producto punto final
else: #Si los arreglos son de diferente tamaño:
  print("Los arreglos son de diferente tamaño")  # Se imprime que son de diferente tamaño

```
>#### 3.Hacer un algoritmo que deje al final de un arreglo de números todos los ceros que aparezcan en dicho arreglo.

```python
Arreglo1= [1,5,0,3,0,1,2,0] # Arreglo original
ceros=[i for i in Arreglo1 if i==0] #Lista con ceros del arreglo original
Final= Arreglo1 + ceros #Concatenamos el arreglo original y despues la lista de solo ceros que aparecen en dicho arreglo
print(Final) # Imprimimos la lista final
```
>#### 4.Revisar que son los algoritmos de sorting, entender bubble-sort (enlace a implementación).
