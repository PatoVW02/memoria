from random import *
from turtle import *
import string

from freegames import path

car = path('car.gif')
# Genera una lista de letras aleatorias y sus duplicados.
letters = list(string.ascii_uppercase) * 2
state = {'mark': None}
hide = [True] * 64

# Inicializamos el contador de taps
tap_count = 0


def square(x, y):
    """Draw white square with black outline at (x, y)."""
    up()
    goto(x, y)
    down()
    color('black', 'white')
    begin_fill()
    for count in range(4):
        forward(50)
        left(90)
    end_fill()


def index(x, y):
    """Convert (x, y) coordinates to tiles index."""
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)


def xy(count):
    """Convert tiles count to (x, y) coordinates."""
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200


def tap(x, y):
    """Update mark and hidden tiles based on tap."""
    global tap_count  # Acceder a la variable tap_count

    # Asegurarse de que las coordenadas estén dentro del rango [-200, 200]
    x = max(min(x, 200), -200)
    y = max(min(y, 200), -200)

    spot = index(x, y)
    mark = state['mark']
    tap_count += 1  # Incrementar el contador de taps

    if mark is None or mark == spot or letters[mark] != letters[spot]:
        state['mark'] = spot
    else:
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None


def draw():
    """Draw image and tiles."""
    clear()
    goto(0, 0)
    shape(car)
    stamp()

    for count in range(64):
        if hide[count]:
            x, y = xy(count)
            square(x, y)

    mark = state['mark']

    if mark is not None and hide[mark]:
        x, y = xy(mark)
        up()
        goto(x + 25, y + 5)
        color('black')
        write(letters[mark], align='center', font=('Arial', 30, 'normal'))

    up()
    goto(-180, 180)
    color('black')
    write(f'Taps: {tap_count}', font=('Arial', 16, 'normal'))
    update()

    # Verificar si todos los cuadros se han descubierto
    if all(not hidden for hidden in hide):
        goto(-180, 150)
        write('¡Todos los cuadros han sido descubiertos!', font=('Arial', 16, 'normal'))

    ontimer(draw, 100)


shuffle(letters)
setup(420, 420, 370, 0)
addshape(car)
hideturtle()
tracer(False)
onscreenclick(tap)
draw()
done()
