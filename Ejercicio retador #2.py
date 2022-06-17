municipios=[]
numero_habitantes=[]
n=int(input("Cuantos municipios son:"))
for i in range(n):
  municipio=input("Municipio:")
  municipios.append(municipio)
  NumeroDeHabitantes=float(input("Numero de habitantes:"))
  numero_habitantes.append(NumeroDeHabitantes)
def sumar(numero_habitantes):
  suma=0
  for elemento in numero_habitantes:
    suma+=elemento
  return suma
total_habitantes=sumar(numero_habitantes)
print("El total de habitantes es: ",total_habitantes)
promedio_habitantes=total_habitantes/n
print("El promedio de habitantes es: ",promedio_habitantes)