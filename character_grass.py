from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

def character_draw():
    clear_canvas_now()
    grass.draw_now(400, 30)
    character.draw_now(x, y)
    delay(0.01)

while True:
# Rectangle Move
    x = 400
    y = 90
    while ( x < 750 ):
        character_draw()
        x += 10
    while ( y < 550 ):
        character_draw()
        y += 10
    while ( x > 50 ):
        character_draw()
        x = x - 10
    while ( y > 90 ):
        character_draw()
        y = y - 10
    while ( x < 400 ):
        character_draw()
        x += 10
        
# Circle Move
    cnt = -90
    x = 400
    y = 90
    while cnt < 270:
        character_draw()
        x = 400 + math.cos(cnt / 360 * 2 * math.pi) * 360
        y = 300 + math.sin (-(cnt / 360 * 2 * math.pi)) * 220
        cnt += 1
