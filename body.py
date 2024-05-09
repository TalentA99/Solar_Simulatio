#Author: Talent
#Date: 25/10/2023
#Purpose: Solar assignment Part 2 Body

from cs1lib import *
class Body:
    def __init__(self, mass, x, y, vx, vy, pixel_radius,r,g,b):
        self.mass = mass
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.pixel_radius = pixel_radius
        self.r = r
        self.g = g
        self.b = b

    def update_position(self, timestep):
        self.x = self.x + self.vx * timestep
        self.y = self.y + self.vy * timestep

    def update_velocity(self, ax,ay,timestep):
        self.vx = self.vx + ax * timestep
        self.vy = self.vy + ay * timestep

    def draw(self,cx,cy,pixel_per_meter):
        set_fill_color(self.r, self.g, self.b)
        mx = cx + self.x * pixel_per_meter
        my = cy + self.y * pixel_per_meter
        # print(mx, my) used it to debug my code
        draw_circle(mx, my, self.pixel_radius)