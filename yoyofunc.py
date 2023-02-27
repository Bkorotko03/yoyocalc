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

def inertia_calc(r,m):
     i = 0.0014 + 2*(0.5*m*(0.0045**2 + r**2))
     return i
def loop_plot():
    r = np.arange(4.5,25.5,0.5)
    m = 0.818 + #INSERT MASS RADIUS RELATION FOR RADIUS EXTENDERS HERE
    i = inertia_calc(r,m)
    a = acceleration(r,m,i)
    f = ftare(r,m,i)
    #PLOT RELATIONS BETWEEN FORCE,ACCELERATION AND RADIUS HEREEEEEEE
    