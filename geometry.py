import numpy as np
import scipy.constants as sc

from kinetics import *


class Cluster:
    def __init__(self, d, m_to_eff, height, field, electron):
        self.m_to_eff = m_to_eff
        self.field = field
        self.acceleration = sc.e * self.field / (self.m_to_eff * sc.m_e)
        self.d = d
        self.r = d/2
        self.electron = electron
        self.height = height
        # self.electron.transfer(-5, -6, -7, -8)

    def random_point_on_barrier(self, orient):
        #     radius of the circle
        circle_r = self.r
        orient_case = {'right': [1, np.sqrt(3) / 2, 3],
                       'left': [-1, np.sqrt(3) / 2, -1],
                       'down': [0, -np.sqrt(3) / 2, 1]}
        #     center of the circle (x, y)
        circle_x = circle_r * orient_case[orient][0]
        circle_y = circle_r * orient_case[orient][1]
        #     random angle
        alpha = (np.pi / 3) * orient_case[orient][2] + \
                (np.pi / 3) * np.random.random()
        #     calculating coordinates
        x = circle_r * np.cos(alpha) + circle_x
        y = circle_r * np.sin(alpha) + circle_y

        return x, y

    def random_barrier_width2d_naive(self):
        vec = np.array([self.random_point_on_barrier(np.random.choice(['left', 'right']))]) - \
              np.array([self.random_point_on_barrier('down')])
        width = np.sqrt((vec * vec).sum(axis=1))
        return float(width)

    def barrier_tunneling(self):
        k = self.m_to_eff * sc.m_e * sc.e / sc.hbar ** 2
        width = self.random_barrier_width2d_naive()
        height = self.height
        energy = self.electron.energy
        coefficient = abs(height / (4 * energy * (height - energy)))

        if energy < height:
            tunneling_coefficient = 1 / (1 + coefficient * np.sinh(width * np.sqrt(2 * k * (height - energy))))
        else:
            tunneling_coefficient = 1 / (1 + coefficient * np.sin(width * np.sqrt(2 * k * (energy - height))))
        if np.random.random() < tunneling_coefficient:
            angle_with_field = self.electron.fi
            x = width * np.cos(angle_with_field)
            y = width * np.sin(angle_with_field)
            self.electron.transfer(x, y, 0, angle_with_field)
            return True
        else:
            return False

    def random_point_on_circle(self):
        #     radius of the circle
        circle_r = self.r
        #     random angle
        alpha = 2 * np.pi * np.random.random()
        #     calculating coordinates
        x = circle_r * np.cos(alpha)
        y = circle_r * np.sin(alpha)

        return x, y

    def fly(self, forward=True):
        # TODO учесть поле при не прохождении через барьер
        initial_velocity = self.electron.velocity()
        length = np.array([self.random_point_on_circle()]) - \
                 np.array([self.random_point_on_circle()])
        length = np.sqrt((length * length).sum(axis=1))

        if forward:
            angle_with_field = self.electron.fi
        else:
            angle_with_field = np.pi / 2 + np.pi * np.random.random()
        x = length * np.cos(angle_with_field)
        y = length * np.sin(angle_with_field)
        energy_shift = self.field * x
        self.electron.add_energy(energy_shift)

        final_velocity = self.electron.velocity()
        t = 2 * length / abs(initial_velocity - final_velocity)
        self.electron.transfer(x, y, t, angle_with_field)

    def iteration(self):
        self.barrier_tunneling()
        self.fly()

