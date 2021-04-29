import numpy as np
import scipy.constants as sc
import matplotlib.pyplot as plt


def wave_vector(kin_energy):            #Функция определения волнового вектора по энергии
    return kin_energy ** 0.5


def velocity(E, e, m):     #скорость электрона с энергией E в м/c
    return ( 2 * e * E / m )**0.5


def io_sc_angle(E1, E2):      #Функция для угла рассеяния при impact ionisation
    X = (E1 + E2) / (E1 * E2) ** 0.5   #При условии, что нет примесей
    r = np.random.random()
    cos_theta = (1 + X * (1 - 2 * r)) / (X + 3 - 2 * r)
    return np.arccos(cos_theta)

def impact_ionization(i_energy, threshold, field_angle, sec_energies, sec_field_angles, n):
    r = np.random.random()
    sec_energy = r * (i_energy - threshold)
    f_energy = i_energy - threshold - sec_energy
    rdir = np.random.choice([-1, 1])
    field_angle += rdir * io_sc_angle(f_energy, i_energy)
    sec_field_angles = np.append([sec_field_angles], [np.random.random()*2*np.pi])
    sec_energies = np.append([sec_energies], [sec_energy])
    return f_energy, field_angle, sec_energies, sec_field_angles, n+1