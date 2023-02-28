import yoyofunc
import PySimpleGUI as sg
from datetime import datetime
def main():
    sg.theme('light grey')
    layout = [[sg.Text('Enter radius (mm) below')],
              [sg.Input(key='-RMM-')],
              [sg.Text('Enter mass of ONE radius extender (g) below')],
              [sg.Input(key='-MG-')],
              [sg.Text(key='-OUTPUT-')],
              [sg.Button('Find Acceleration'), sg.Button('Find Moment of Inertia')], 
              [sg.Button('Find Change in Percieved Weight'), sg.Button('Print Dump to File')],
              [sg.Text('Enter filepath for dump below')],
              [sg.Input(key='fpath')],
              [sg.Button('Exit')]]
    window = sg.Window('PHYS126F-04E Program', layout)
    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED or event == 'Exit':
            break
        if event == 'Find Acceleration':
            rm = float(values['-RMM-'])/1000
            mkg = 0.818 + float(values['-MG-'])/500
            i = yoyofunc.inertia_calc(rm,mkg)
            window['-OUTPUT-'].update(f"Acceleration = {yoyofunc.acceleration(rm,mkg,i)} (m/s^2)")
        if event == 'Find Moment of Inertia':
            rm = float(values['-RMM-'])/1000
            mkg = 0.818 + float(values['-MG-'])/500
            i = yoyofunc.inertia_calc(rm,mkg)
            window['-OUTPUT-'].update(f"Moment of Inertia = {i} (kg*m)")
        if event == 'Find Change in Percieved Weight':
            rm = float(values['-RMM-'])/1000
            mkg = 0.818 + float(values['-MG-'])/500
            i = yoyofunc.inertia_calc(rm,mkg)
            FF = yoyofunc.ftare(rm,mkg,i)
            newweight = 101.9716212978 * FF
            window['-OUTPUT-'].update(f'Percieved Change in Mass = {newweight} (g)')
        if event == 'Print Dump to File':
            fpath = values['fpath']
            rm = float(values['-RMM-'])/1000
            mkg = 0.818 + float(values['-MG-'])/500
            i = yoyofunc.inertia_calc(rm,mkg)
            FF = yoyofunc.ftare(rm,mkg,i)
            newweight = 101.9716212978 * FF
            A = yoyofunc.acceleration(rm,mkg,i)
            with open(f'{fpath}\yoyocalcdata.txt', 'a') as file:
                file.write(f'\n{datetime.now()} \nMass (kg): {mkg} \nRadius (m): {rm} \nMoment of Inertia(kg*m): {i}')
                file.write(f'\nAcceleration (m/s^2): {A} \nChange in Apparent weight (g): {newweight} \nChange in force exerted (N): {FF}')
            window['-OUTPUT-'].update(f'File Saved at {fpath}\yoyocalcdata.txt') #ADD INPUT FOR FILEPATH AND MAKE EVERYTHING NICE PLEASE

    window.close()
main()