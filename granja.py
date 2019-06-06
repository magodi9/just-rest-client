class Animal:
    def __init__(self, color,tipo,numerodepatas):
        self.color = color
        self.tipo = tipo
        self.numerodepatas = numerodepatas
        print(f"Soy un {self.tipo} de color {self.color}")
        print(f"Tengo {numerodepatas} patas")
a = Animal("rojo","pajaro",2)


class Animal_2:
  def __init__(self,color,tipo,numerodepatas,ruido):
     Animal.__init__(self,color,tipo,numerodepatas)
     self.ruido = ruido
     print(f"Y hago  {ruido} jajaja")
a = Animal_2("negro","perro",4,"guau")
