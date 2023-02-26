# yoyocalc
Interactive Python program that will spit parameters of the rotating object from PHYS 126F-04E SPR23 into a text file
\nDependendent on NumPy, SciPy, and DateTime (all available on PiP)
\nPossibly will compile to a portable version, and also may implement a GUI
\nyoyofunc.py functions:
\n
\nacceleration(r,m,i): Calculates magnitude of acceleration of rotating body
\nr = radius of rotating body at point of contact with the string (m)
\nm = nass of rotating body (kg)
\ni = moment of inertia of rotating body (kg*m^2)
\n
\nftare(r,m,i): Calculates the change in the scale's percieved force
\nr = radius of rotating body at point of contact with the string (m)
\nm = nass of rotating body (kg)
\ni = moment of inertia of rotating body (kg*m^2)
\n
\nintertia_calc(r,m): Calculates moment of inertia of the rotating body
\nr = radius of rotating body at point of contact with the string (m)
\nm = mass of ONE radius extender
