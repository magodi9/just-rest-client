# Ejercicio 
# Usuarios = {"Marta","David","Elvira","Juan","Marcos"}
# Administradores = {"Juan","Marta"}
# Administradores.discard("Juan")
# Administradores.add("Marcos")
# for a in Usuarios:
#    if a in Administradores:
#       print (f"El Usuario {a} es un Administrador ")
#    else:
#         print (f"El Usuario {a} no es Administrador ")

# 2 Ejercicio
# Caballero = { 'Vida':2, 'Defensa':2, 'Ataque':2,'Alcance':2 }
# Guerrero  =  { 'Vida':2, 'Defensa':2, 'Ataque':2,'Alcance':2 }
# Arquero   =   { 'Vida':2, 'Defensa':2, 'Ataque':2, 'Alcance':2 } 

# Caballero['Vida'] = Guerrero ['Vida'] * 2
# Caballero['Defensa'] = Guerrero ['Defensa'] * 2

# Guerrero['Ataque'] = Caballero['Ataque'] * 2
# Guerrero['Alcance'] = Caballero['Alcance'] * 2

# Arquero['Vida']     = Guerrero['Vida']
# Arquero['Ataque']   = Guerrero['Ataque']
# Arquero['Defensa'] = Guerrero['Defensa'] /2
# Arquero['Alcance'] = Guerrero['Alcance'] * 2

# Personajes = {'Caballero' :Caballero,'Guerrero' :Guerrero,'Arquero':Arquero}
# print (Personajes)

# 3 Ejercicio
tareas = [ 
    [6, 'Distribución'],
    [2, 'Diseño'],
    [1, 'Concepción'],
    [7, 'Mantenimiento'],
    [4, 'Producción'],
    [3, 'Planificación'],
    [5, 'Pruebas']
]

print("==Tareas desordenadas==")
for tarea in tareas:
    print(tarea[0], tarea[1])

print("==Tareas ordenadas==")
tareas.sort()
for tarea in tareas:
    print( tarea[1])
    

