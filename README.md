# Conductivity Modeling in Nanoparticle Structures

## Table of contents
* [General info](#general-info)
* [Methods](#methods)
* [Modules](#modules)
    * [Geometry](#geometry)
    * [Kinetics](#kinetics)
    * [Scattering rates](#scattering-rates)

## General info
This project made mainly for investigate processes of conductors' scattering in some nanoparticles film samples, basing on experimental data.
	
## Methods
In this project I will use following techniques:
* Quantum mechanics
* Solid state physics
* Stochastic methods (like Monte Carlo method)

## Modules
### Geometry
### Kinetics
Here we will start with an assumption, that wave vector and kinetic energy of electron are parabolic connected:
```python
def wave_vector(kin_energy): 
    return kin_energy ** 0.5
```
### Scattering rates