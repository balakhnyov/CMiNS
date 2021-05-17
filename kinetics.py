import numpy as np
import scipy.constants as sc
import matplotlib.pyplot as plt


class Electron:
    def __init__(self, energy, m_to_eff):
        self.m_to_eff = m_to_eff
        self.energy = energy
        self.x = 0
        self.y = 0
        self.fi = 0
        self.t = 0

    def transfer(self, dx, dy, dt, fi):
        self.x += dx
        self.y += dy
        self.t += dt
        self.fi = fi

    def add_energy(self, energy):
        self.energy += energy

    def velocity(self):
        v = np.sqrt(2 * sc.e * self.energy / (self.m_to_eff * sc.m_e))
        return v
