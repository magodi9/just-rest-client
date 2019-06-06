# n = int(input('Primer numero >>'))
# m = int(input('Segundo numero >>'))
# True and False
# print (n == m )#¿Son iguales?
# print (n != m )#¿Son diferentes?
# print (n > m )#¿El primero es mayor que el segundo?
# print (n <= m )#¿El segundo es mayor o igual que el primero?

## 1 EJERCICIO
 def menu():
      n1 = int(input("Introduce un número: ") )
      n2 = int(input("Introduce otro número: ") )
      opcion = int(input("""Que quieres hacer      1 Sumar 
      2 Restar
      3 Multiplicar
      Responda 1,2,3 segun corresponda>>>"""))
    
      if opcion == 1:
          print(f"el Resultado es {n1 + n2}")
      elif opcion == 2:
          print(f"el Resultado es {n1 - n2}")   
      elif opcion == 3:
          print(f"el Resultado es {n1 * n2}")  
      else:
          print("Responda correctamente")
          menu()


# menu()

# 2 EJERCICIO
# numero = 0
# while numero % 2 == 0:
#     numero = int(input("Introduce un numero impar>>"))

# 3 EJERCICIO
# x = range(0 ,101,2)
# s = sum(x)
# print (s)


# 4 EJERCICIO
# suma = 0     
# numeros = int(input("Cuantos numero vas a introducir>>"))
# for x in range (numeros):
#     suma += int(input("Introduce un numero>>")) 
# print(f"""Se ha introducido {numeros} numeros que en total ha sumado 
# {suma} y la media es {suma/ numeros}""") 

# 5 EJERCICIO
# numeros = (1,3,6,9)
# while (True):
#     valor = int(input("Introduce un numero entre 0 y 9>>"))
#     if valor in numeros:
#       print(f"El numero {valor} esta en esta lista {numeros}")
#       break
#     else:
#       print("El número", valor, "no se encuentra en la lista", numeros)

# # 6 Ejercicio
# print(list(range(0,11)))
# print(list(range(-10,1)))
# print(list(range(0,21,2)))
# print(list(range(-19,0,2)))
# print(list(range(0,51,5)))

# 7 Ejercicicio
# lista_1 = ["h",'o','l','a',' ', 'm','u','n','d','o']
# lista_2 = ["h",'o','l','a',' ', 'l','u','n','a']
# lista_3 = []
# for letra in lista_1:
#     if letra in lista_2 and letra not in lista_3:
#         lista_3.append(letra)

# print(lista_3)