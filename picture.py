from colors import *
class Picture:
  def __init__(self, img):
    self.img = img;

  def __eq__(self, other):
    return self.img == other.img

  def _invColor(self, color):
    if color not in inverter:
      return color
    return inverter[color]

  def verticalMirror(self):
    """ Devuelve el espejo vertical de la imagen """
    return Picture([fila[::-1] for fila in self.img])

  def horizontalMirror(self):
    """ Devuelve el espejo horizontal de la imagen """
    return Picture(self.img[::-1])

  def negative(self):
    """ Devuelve un negativo de la imagen """
    nueva = []
    for fila in self.img:
      nuevaFila = ""
      for c in fila:
        nuevaFila += self._invColor(c)
      nueva.append(nuevaFila)
    return Picture(nueva)

  def join(self, p):
    """ Devuelve una nueva figura poniendo la figura del argumento al lado derecho de la figura actual """
    nueva = []
    for i in range(len(self.img)):
      nueva.append(self.img[i] + p.img[i])
    return Picture(nueva)

  def up(self, p):
    return Picture(p.img + self.img)

  def under(self, p):
    return Picture(self.img + p.img)
  
  def horizontalRepeat(self, n):
    """ Devuelve una nueva figura repitiendo la figura actual al costado la cantidad de veces que indique el valor de n """
    nueva = []
    for fila in self.img:
      nueva.append(fila * n)
    return Picture(nueva)

  def verticalRepeat(self, n):
    nueva = []
    for i in range(n):
      nueva += self.img
    return Picture(nueva)
