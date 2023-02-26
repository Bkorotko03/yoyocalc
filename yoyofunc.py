#FUNCTIONS TO CAll IN YOYOCALC.PY
#UNIVERSAL IMPORTS
import numpy as np
import scipy.constants as constant
#SET CONSTANTS
g = constant.g
#DEFINE FUNCTIONS
def acceleration(r,m,i):
    a = (g)/(1+(i/(m * r**2)))
    return a

def ftare(r,m,i):
     f = (-1)*((m*g)/(1+(i/(m * r**2))))
     return f

def intertia_calc(r,m):
     i = 0.0014 + 2*(0.5*m*(0.0045**2 + r**2))
     return i