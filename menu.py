import requests
import os
import time 
r = requests.get("http://c3166bbd.ngrok.io/subjects")
respuesta = r.json()

def lista():
  print("Cargando...")
  time.sleep(3)  
  os.system("cls")  
  contador = 0
  for resultado in respuesta:
    print (f"El estudiante Santiago a obtenido  {respuesta[contador]['mark']['$numberDecimal']} en {respuesta[contador]['name']} ")
    contador += 1
  menu2()


def Promedio():
  print("Cargando...")
  time.sleep(3)
  os.system("cls")
  r = requests.get("http://c3166bbd.ngrok.io/subjects/average")
  respuesta = r.json()
  print (f"El promedio del estudiante es {respuesta['studentAvg']}")
  menu2()


  

def menu():
    os.system("cls")
    resp = int(input("""Oprime segun corresponda 
     1 Obtener Lista completa de materias
     2 Obtener Promedio
     >>"""))
    if resp == 1:
      lista()
    elif resp == 2:
      Promedio() 
    else:
      print("Responda 1 o 2 segun lo desee")
      time.sleep(2)
      menu()
      



def menu2():
    resp2 = int(input("""Oprime segun corresponda
     1 Salir
     2 Menu
     >>"""))
    if resp2 == 1:
        os.system("exit")
    elif resp2 == 2:
        print("Cargando...")
        time.sleep(3)
        menu()
    else:
        print("Responda 1 o 2 segun desee")
        time.sleep(2)
        os.system("cls") 
        menu2()   
                

menu() 
       
