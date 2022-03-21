class Asiento:
  def __init__ (self, color, precio, registro):
    self.color=color
    self.precio=precio
    self.registro=registro

  def cambiarColor(self, color):
    colores=["rojo", "verde", "amarillo", "negro", "blanco"]
    if color in colores:
      self.color=color

class Auto:
  cantidadCreados=0
  def __init__ (self, modelo, precio, asientos, marca, motor,  registro):
    self.modelo=modelo
    self.asientos=asientos
    self.registro=registro
    self.marca=marca
    self.precio=precio
    self.motor=motor

    Auto.cantidadCreados+=1

  def cantidadAsientos(self):
    c=0
    l=[]
    prueba=Asiento("verde", 22,0)
   
    for i in self.asientos:
      if i != None:
        l.append(i)
      if type(prueba)==type(i):
        c+=1
    return(c)


  def verificarIntegridad(self):
    l=[]
    r=0
    c=0
    for i in self.asientos:
      if i != None:
        c+=1
        if i.registro==self.registro and i.registro==self.motor.registro:
          l.append(i.registro)
          if len(l)==c:
            return("Auto original")
          else:
            return("Las piezas no son originales")
          
    
    

class Motor:
  def __init__ (self, numerosCilindros, tipo, registro):
    self.numerosCilindros=numerosCilindros
    self.tipo=tipo
    self.registro=registro

  def cambiarRegistro(self,registro):
    self.registro=registro

  def asignarTipo(self,tipo):
    o=["gasolina", "electrico"]
    if tipo in o:
      self.tipo=tipo
  

if __name__ == "__main__":
  a = Auto("model 3", 33000, list(),"tesla", Motor(4, "electrico", 142), 341)
  a.asientos = [Asiento("blanco", 5000, 435),None, None, Asiento("blanco", 5000, 435), None]
  
  
  a1 = Auto("model 3", 33000, [Asiento("blanco", 5000, 32),None, None, Asiento("blanco", 5000, 32), None], "tesla", Motor(4, "electrico", 32), 32)
  print(a1.verificarIntegridad())
  print(a1.cantidadAsientos())
  #print(a1.motor)
  a2 = Auto("model 3", 33000, [Asiento("blanco", 5000, 40),None, None, Asiento("blanco", 5000, 32), None], "tesla", Motor(4, "electrico", 32), 32)
  print(a2.verificarIntegridad())

  
    
    
    
    
    

    
      

    