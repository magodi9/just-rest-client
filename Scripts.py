import sys
if len(sys.argv) == 3:
   texto = sys.argv[1]
   repeticiones = int(sys.argv[2])
   for r in range (repeticiones):
     print(texto)
else:
    print("Error, introduce los argumentos correctos")
    print("Ejemplo: Scripts.py 'Texto' 5 ")

# print("Hola, bienvenido a tu primer script")
# print(sys.argv)