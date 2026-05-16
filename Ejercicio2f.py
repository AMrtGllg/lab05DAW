from interpreter import draw
from chessPictures import *

fila1 = square.join(square.negative()).horizontalRepeat(4)
fila2 = square.negative().join(square).horizontalRepeat(4)

figura_f = fila1.under(fila2).verticalRepeat(2)
draw(figura_f)