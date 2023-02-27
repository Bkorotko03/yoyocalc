#IMPORTS
import yoyofunc
from datetime import datetime
#ASK FOR OR CALCULATE INERTIA
knowin = input('Do you know the moment of inertia for the rotating body [Y/N]:')
if knowin == 'Y':
    i = float(input('Enter moment of inertia (kg*m^2) here:'))
    M = float(input('Enter mass (kg) of rotating body:'))
    r = float(input('Enter radius (m) of rotating body'))
elif knowin == 'N':
    sameyoyo = input('Are you working with the same rotating body as PHYS 126F-04E? [Y/N]:')
    if sameyoyo == 'Y':
        r = (float(input('Enter radius (mm) of radius extender here:')))/1000
        m = (float(input('Enter mass (g) of one radius extender here:')))/1000
        M = 0.818 + m
        i = yoyofunc.intertia_calc(r,m)
    elif sameyoyo == 'N':
        print('Please calculate the moment of inertia and restart, also what are you using this for?')
    else:
        print('Please enter either Y or N')
else:
    print('Please enter either Y or N')
#CALC ACCEL AND CHANGE IN FORCE/WEIGHT
A = yoyofunc.acceleration(r,M,i)
FF = yoyofunc.ftare(r,M,i)
newweight = 101.9716212978 * FF
#OPEN AND WRITE TO FILE
with open('yoyocalcdata.txt', 'a') as file:
    file.write(f'\n{datetime.now()} \nMass (kg): {M} \nRadius (m): {r} \nMoment of Inertia(kg*m^2): {i}')
    file.write(f'\nAcceleration (m/s^2): {A} \nChange in Apparent weight (g): {newweight} \nChange in force exerted (N): {FF}')
#testing commits