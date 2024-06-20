'''This program is called The Planetarium and its intention is to draw a
canvas with the planet selected by the user. It works as intended in a
400 x 400 canvas, but couldn't figure out a way to adjust the size of
the planets to make it work independent of the size of the canvas. Some
planets that needed some details, like Earth, Saturn and Jupiter, also were a
bit difficult to port to another size canvas. Althoug i had some progress
trying to figure it out, i was beaten by the deadline.'''
from graphics import Canvas
import random
import time

CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400


def main():
    # Here, in order, we create a canvas, use the function draw_space
    # to create a black screen and the function draw_stars to fill
    # that blackspace with random placed stars. Then we show a intro
    # to the user.
    # We invite the user to type the name of the planet that he want to see,
    # and, after the first planet is shown, he has the option to leave by
    # typing 'exit'.
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    draw_space(canvas)
    draw_stars(canvas)
    opening_screen(canvas)
    print('Welcome to the planetarium!')
    answer = input('Wich planet of our solar system do you want to see? ').lower().strip()

    while answer != "exit":
        if answer not in planet_dict:
            answer = input('Please, enter a valid planet: ')
        else:
            draw_space(canvas)
            draw_stars(canvas)
            planet_dict[answer](canvas)
            answer = input(
                'Do you want to see another planet? Enter it\'s name or type exit to leave: ').lower().strip()


def draw_space(canvas):
    # create a black screen to simulate the space
    canvas.create_rectangle(0, 0, CANVAS_WIDTH, CANVAS_HEIGHT, 'black')


def draw_stars(canvas):
    # fill the space with stars in random positions.I tried to use the
    # canvas size as a parameter of how many star should be drawn.
    for i in range(int((CANVAS_HEIGHT + CANVAS_WIDTH) / 8)):
        x = random.randint(0, CANVAS_WIDTH)
        y = random.randint(0, CANVAS_HEIGHT)
        size = random.randint(1, 2)
        canvas.create_oval(x, y, x + size, y + size, 'white')


# Bellow we define the functions that create the planets and draw
# its names on the canvas
def draw_mercury(canvas):
    planet = 'Mercury'
    size = 20
    x = CANVAS_WIDTH / 2 - size / 2
    y = CANVAS_HEIGHT / 2 - size / 2
    canvas.create_oval(x, y, x + size, y + size, 'darkgoldenrod')
    canvas.create_text(10, 10, planet, font_size=40, color='white')


def draw_venus(canvas):
    planet = 'Venus'
    size = 50
    x = CANVAS_WIDTH / 2 - size / 2
    y = CANVAS_HEIGHT / 2 - size / 2
    canvas.create_oval(x, y, x + size, y + size, 'goldenrod')
    canvas.create_text(10, 10, planet, font_size=40, color='white')


def draw_earth(canvas):
    planet = 'Earth'
    size = 50
    x = CANVAS_WIDTH / 2 - size / 2
    y = CANVAS_HEIGHT / 2 - size / 2
    canvas.create_oval(x, y, x + size, y + size, 'royalblue')
    canvas.create_text(10, 10, planet, font_size=40, color='white')
    canvas.create_polygon(CANVAS_WIDTH / 2 - CANVAS_WIDTH / 38, CANVAS_HEIGHT / 2, CANVAS_WIDTH / 2 + CANVAS_WIDTH / 41,
                          CANVAS_HEIGHT / 2, CANVAS_WIDTH / 2 - CANVAS_WIDTH / 100,
                          CANVAS_HEIGHT / 2 + CANVAS_HEIGHT / 20, color='forestgreen')
    canvas.create_rectangle(CANVAS_WIDTH / 2, CANVAS_HEIGHT / 2 - size / 4, CANVAS_WIDTH / 2 + size / 2.5,
                            CANVAS_HEIGHT / 2 + size / 8, 'forestgreen')


def draw_mars(canvas):
    planet = 'Mars'
    size = 20
    x = CANVAS_WIDTH / 2 - size / 2
    y = CANVAS_HEIGHT / 2 - size / 2
    canvas.create_oval(x, y, x + size, y + size, 'red')
    canvas.create_text(10, 10, planet, font_size=40, color='white')


def draw_jupiter(canvas):
    planet = 'Jupiter'
    size = 300
    x = CANVAS_WIDTH / 2 - size / 2
    y = CANVAS_HEIGHT / 2 - size / 2
    canvas.create_oval(x, y, x + size, y + size, 'burlywood')
    canvas.create_text(10, 10, planet, font_size=40, color='white')
    canvas.create_line((CANVAS_WIDTH - size) / 2, CANVAS_HEIGHT / 2, size + (CANVAS_WIDTH - size) / 2,
                       CANVAS_HEIGHT / 2, 'crimson')
    canvas.create_line((CANVAS_WIDTH - size - 10), CANVAS_HEIGHT * 0.75, CANVAS_WIDTH - size / 4 - 10,
                       CANVAS_HEIGHT * 0.75, 'crimson')
    canvas.create_oval(CANVAS_WIDTH / 1.7, CANVAS_HEIGHT / 1.7, CANVAS_WIDTH / 1.4, CANVAS_HEIGHT / 1.5, 'crimson')


def draw_saturn(canvas):
    planet = 'Saturn'
    size = 300
    x = CANVAS_WIDTH / 2 - size / 2
    y = CANVAS_HEIGHT / 2 - size / 2
    canvas.create_oval(x, y, x + size, y + size, 'tan')
    canvas.create_text(10, 10, planet, font_size=40, color='white')
    # Here we create a loop to draw 7 white lines to simulate the planet rings:
    start_y = CANVAS_HEIGHT
    start_x = CANVAS_WIDTH
    for i in range(7):
        canvas.create_line(0, start_y + 9, start_x + 9, 0, 'white')
        start_y -= 3
        start_x -= 3


def draw_uranus(canvas):
    planet = 'Uranus'
    size = 230
    x = CANVAS_WIDTH / 2 - size / 2
    y = CANVAS_HEIGHT / 2 - size / 2
    canvas.create_oval(x, y, x + size, y + size, 'cyan')
    canvas.create_text(10, 10, planet, font_size=40, color='white')


def draw_neptune(canvas):
    planet = 'Neptune'
    size = 230
    x = CANVAS_WIDTH / 2 - size / 2
    y = CANVAS_HEIGHT / 2 - size / 2
    canvas.create_oval(x, y, x + size, y + size, 'dodgerblue')
    canvas.create_text(10, 10, planet, font_size=40, color='white')


# i added the sun as an easter egg, but didn't had time to use it :(
def draw_sun(canvas):
    planet = 'Sun'
    size = 1000
    x = CANVAS_WIDTH / 2 - size / 2
    y = CANVAS_HEIGHT / 2 - size / 2
    canvas.create_oval(x, y, x + size, y + size, 'yellow')
    canvas.create_text(10, 10, planet, font_size=40, color='white')


def draw_pluto(canvas):
    canvas.create_text(10, 10, 'Pluto', font_size=40, color='white')
    time.sleep(0.5)
    canvas.create_text(10, 60, 'is', font_size=40, color='white')
    time.sleep(0.5)
    canvas.create_text(10, 110, 'NOT', font_size=40, color='white')
    time.sleep(0.5)
    canvas.create_text(10, 160, 'a', font_size=40, color='white')
    time.sleep(0.5)
    canvas.create_text(10, 210, 'Planet!', font_size=40, color='white')
    time.sleep(0.5)
    canvas.create_text(10, 260, '(ノಠ益ಠ)ノ彡┻━┻', font_size=40, color='white')


def opening_screen(canvas):
    # Draws a title screen for the program.
    canvas.create_text(15, 180, 'THE PLANETARIUM', 'arial', int((CANVAS_WIDTH + CANVAS_HEIGHT / 2) / 15), 'aliceblue')


# the dictionary bellow was a way i used to avoid the use of lots of
# 'if's and 'elif's conditions to analyze the user inputs.
planet_dict = {'mercury': draw_mercury,
               'venus': draw_venus,
               'earth': draw_earth,
               'mars': draw_mars,
               'jupiter': draw_jupiter,
               'saturn': draw_saturn,
               'uranus': draw_uranus,
               'neptune': draw_neptune,
               'pluto': draw_pluto,
               'sun': draw_sun
               }
if __name__ == '__main__':
    main()