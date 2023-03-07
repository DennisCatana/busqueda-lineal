def imprimir_arreglo(arreglo):
  tamanio = len(arreglo)
  for i in range(tamanio):
    print(f'[{arreglo[i]}]',end="")

def algoritmo_Busqueda_lineal(arreglo,sueldo):
  resultado = False
  tamanio = len(arreglo)
  for i in range(tamanio):
    if (arreglo[i]==sueldo):
      resultado=True
      return resultado
      return resultado

listaSueldos=[20.8,150.5,170.5,180.8,190,30,75.6,200]
imprimir_arreglo(listaSueldos)
sueldo = float(input("\n\nIngrese el sueldo a encontrar: "))
respuesta = algoritmo_Busqueda_lineal(listaSueldos,sueldo)
if respuesta:
  print("\n\nEl sueldo fue encontrado en nuestro servicio")
else:
  print("\nEl sueldo no se pudo encontrar :(")
