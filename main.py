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
  def __init__ (self, modelo, marca, asientos, precio, motor,  registro):
    self.modelo=modelo
    self.asientos=asientos
    self.registro=registro
    self.marca=marca
    self.precio=precio
    self.motor=motor

    Auto.cantidadCreados+=1

  def cantidadAsientos(self):
    c=0
    prueba=Asiento("verde", 22,0)
   
    for i in self.asientos:
      
      if type(prueba)==type(i):
        c+=1
    return("Numeros de asientos", + c)


  def verificarIntegridad(self):
    l=[]
    r=0
    a=self.asientos[0]
    for i in self.asientos:
      l.append(i.registro)
      if l.count(a.registro)==len(l):
        r=a.registro
        
    if self.motor.registro==self.registro and self.registro == r:
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
  asiento1= Asiento("rojo", 36, 2)
  asiento2= Asiento("rojo", 36, 2)
  asiento3=Motor("rojo", 36, 4)
  motor1=Motor(1, "gasolina", 2)
  motor2=Motor(1, "gasolina", 2)
  a1= Auto("a", "bw", [asiento1,asiento2, asiento3], 32, motor1, 2)
  a2= Auto("a", "bw", [asiento1,asiento2], 32, motor2, 2)
  motor1.asignarTipo("electrico")
  print(motor1.tipo)
  print(a1.cantidadAsientos())
  print(a1.verificarIntegridad())
  asiento1.cambiarColor("rosa")
  print(asiento1.color)
  print(a1.cantidadCreados)
  
  
  

  
    
    
    
    
    

    
      

    