from interpreter import draw
from chessPictures import *

b = square
n = square.negative()

# tablero vacío
filaA = b.join(n).horizontalRepeat(4)
filaB = n.join(b).horizontalRepeat(4)

tablero = (
    filaA
    .under(filaB)
    .under(filaA)
    .under(filaB)
    .under(filaA)
    .under(filaB)
    .under(filaA)
    .under(filaB)
)

# piezas negras
fila8 = (
    n.overlay(rock.negative())
    .join(b)
    .join(n.overlay(bishop.negative()))
    .join(b.overlay(queen.negative()))
    .join(n.overlay(king.negative()))
    .join(b.overlay(bishop.negative()))
    .join(n.overlay(knight.negative()))
    .join(b.overlay(rock.negative()))
)

fila7 = (
    b.overlay(pawn.negative())
    .join(n.overlay(pawn.negative()))
    .join(b.overlay(pawn.negative()))
    .join(n.overlay(pawn.negative()))
    .join(b)
    .join(n.overlay(pawn.negative()))
    .join(b.overlay(pawn.negative()))
    .join(n.overlay(pawn.negative()))
)

fila6 = (
    n
    .join(b)
    .join(n.overlay(knight.negative()))
    .join(b)
    .join(n)
    .join(b)
    .join(n)
    .join(b)
)

fila5 = (
    b
    .join(n)
    .join(b)
    .join(n)
    .join(b.overlay(pawn.negative()))
    .join(n)
    .join(b)
    .join(n)
)

fila4 = (
    n
    .join(b)
    .join(n.overlay(bishop))
    .join(b)
    .join(n.overlay(pawn))
    .join(b)
    .join(n)
    .join(b)
)

fila3 = (
    b
    .join(n)
    .join(b)
    .join(n)
    .join(b)
    .join(n.overlay(knight))
    .join(b)
    .join(n)
)

fila2 = (
    n.overlay(pawn)
    .join(b.overlay(pawn))
    .join(n.overlay(pawn))
    .join(b.overlay(pawn))
    .join(n)
    .join(b.overlay(pawn))
    .join(n.overlay(pawn))
    .join(b.overlay(pawn))
)

fila1 = (
    b.overlay(rock)
    .join(n.overlay(knight))
    .join(b.overlay(bishop))
    .join(n.overlay(queen))
    .join(b.overlay(king))
    .join(n)
    .join(b)
    .join(n.overlay(rock))
)

tablero = (
    fila8
    .under(fila7)
    .under(fila6)
    .under(fila5)
    .under(fila4)
    .under(fila3)
    .under(fila2)
    .under(fila1)
)

draw(tablero)