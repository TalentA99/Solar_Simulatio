#Author: Talent
#Date: 25/10/2023
#Purpose: Solar assignment Part 2 Solar

from cs1lib import *
from system import System
from body import Body

WINDOW_WIDTH = 400
WINDOW_HEIGHT = 400

TIME_SCALE = 3.0e6
PIXELS_PER_METER = 7 / 1e10

FRAMERATE = 30
TIMESTEP = 1.0 / FRAMERATE  # time passed between drawing each frame

def main():

    set_clear_color(0, 0, 0)    # black background
    clear()
    solar_system.draw(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2, PIXELS_PER_METER)
    # Update the system for its next state.
    solar_system.update(TIMESTEP * TIME_SCALE)

sun = Body(1.98892e30, 0, 0, 0, 0, 30, 0.5, 1, 0)
mercury = Body(	0.33e24,-57.9e9,0,0,47890,8,0.5, 0.5, 0.4)
venus = Body(4.87e24,-108.2e9,0,0,35040,12,1,0.8,0)
earth = Body(5.97e24, -149.6e9, 0, 0, 29790, 9, 0.5, 0.4, 1)
mars = Body(0.642e24,-227.9e9,0,0,24140,14,0.9,0.3,0.1)

solar_system = System([sun, mercury, venus, earth, mars])


start_graphics(main, 2400, framerate=FRAMERATE)