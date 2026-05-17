from interpreter import draw
from chessPictures import *

b = square
n = square.negative()

#negras
fila8 = (
    n.overlay(rock.negative())
    .join(b.overlay(knight.negative()))
    .join(n.overlay(bishop.negative()))
    .join(b.overlay(queen.negative()))
    .join(n.overlay(king.negative()))
    .join(b.overlay(bishop.negative()))
    .join(n.overlay(knight.negative()))
    .join(b.overlay(rock.negative()))
)

#peones negros
fila7 = (
    b.overlay(pawn.negative())
    .join(n.overlay(pawn.negative()))
    .join(b.overlay(pawn.negative()))
    .join(n.overlay(pawn.negative()))
    .join(b.overlay(pawn.negative()))
    .join(n.overlay(pawn.negative()))
    .join(b.overlay(pawn.negative()))
    .join(n.overlay(pawn.negative()))
)


fila6 = b.join(n).horizontalRepeat(4)

fila5 = n.join(b).horizontalRepeat(4)

fila4 = b.join(n).horizontalRepeat(4)

fila3 = n.join(b).horizontalRepeat(4)

#peones blancos
fila2 = (
    n.overlay(pawn)
    .join(b.overlay(pawn))
    .join(n.overlay(pawn))
    .join(b.overlay(pawn))
    .join(n.overlay(pawn))
    .join(b.overlay(pawn))
    .join(n.overlay(pawn))
    .join(b.overlay(pawn))
)

#blancas
fila1 = (
    b.overlay(rock)
    .join(n.overlay(knight))
    .join(b.overlay(bishop))
    .join(n.overlay(queen))
    .join(b.overlay(king))
    .join(n.overlay(bishop))
    .join(b.overlay(knight))
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