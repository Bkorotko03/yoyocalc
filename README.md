# yoyocalc
Interactive Python program that will spit parameters of the rotating object from PHYS 126F-04E SPR23 into a text file

Dependendent on NumPy, SciPy, MatPlotLib, and DateTime (all available on PiP)

# yoyofunc.py functions:

(All values in SI unless stated or noted otherwise)

acceleration(r,m,i): Calculates magnitude of acceleration of rotating body
r = radius of rotating body at point of contact with the string (m)
m = nass of rotating body (kg)
i = moment of inertia of rotating body (kg*m^2)

ftare(r,m,i): Calculates the change in the scale's percieved force
r = radius of rotating body at point of contact with the string (m)
m = nass of rotating body (kg)
i = moment of inertia of rotating body (kg*m^2)

intertia_calc(r,m): Calculates moment of inertia of the rotating body
r = radius of rotating body at point of contact with the string (m)
m = mass of ONE radius extender
