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
