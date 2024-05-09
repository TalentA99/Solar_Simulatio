#Author: Talent
#Date: 25/10/2023
#Purpose: Solar assignment Part 2 System

from body import Body
from math import *
class System:
    def __init__(self, body_list):
        self.body_list = body_list



    def update(self, timestep):
        for body in self.body_list:
            body.update_position(timestep)
            #body.update_velocity(0.001, 0.001,timestep) This was from Part 1 assignment
        for i in range(len(self.body_list)):
            ax,ay = self.acceleration(i)
            self.body_list[i].update_velocity(ax,ay,timestep)


    def draw(self, cx, cy, pixel_per_meter):
        for body in self.body_list:
            body.draw(cx, cy, pixel_per_meter)

    def acceleration(self, n):
        ax = 0
        ay = 0
        G = 6.6738e-11

        for i in range(len(self.body_list)):
            if i != n:
                dx = self.body_list[i].x - self.body_list[n].x
                dy = self.body_list[i].y - self.body_list[n].y
                r = sqrt(dx**2 + dy**2)
                a = G * (self.body_list[i].mass / (r**2))
                ax = ax + (a * (dx / r))
                ay = ay + (a * (dy / r))

        return ax, ay