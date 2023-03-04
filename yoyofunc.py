#FUNCTIONS TO CALL IN YOYOCALC.PY
#UNIVERSAL IMPORTS
import numpy as np
import scipy.constants as constant
import matplotlib.pyplot as plt
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
     i = 0.00161109 + 2*(0.5*m*(0.0045**2 + r**2))
     return i
def loop_plot(rmm1 = 4.5, rmm2 = 25.5, stepmm = 0.5): #NOT SI UNITS
    rmm = np.arange(rmm1,rmm2,stepmm)
    r = rmm/1000
    m = 0.818 #REMEMBER TO ADD MASS RADIUS RELATION FOR RADIUS EXTENDER, ALSO MULT BY 2 BECAUSE THERES 2 RAD EXTENDERS
    i = inertia_calc(r,m)
    a = acceleration(r,m,i)
    f = ftare(r,m,i)
    accelgraph = plt.plot(a,rmm)
    fgraph = plt.plot(f,rmm)
    plt.show()
    