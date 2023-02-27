import yoyofunc
import PySimpleGUI as sg
def main():
    sg.theme('light grey')
    layout = [[sg.Text("Enter parameters here:")],
              [sg.Input("Enter Radius (mm):", key='-RMM-')],
              [sg.Input("Enter mass of ONE radius extender (g):", key='-MG-')],
              [sg.Button('Find Acceleration'), sg.Button('Find Moment of Inertia')], 
              [sg.Button('Find Change in Percieved Weight'), sg.Button('Print Dump to File')],
              [sg.Button('Exit')]]
    window = sg.Window('PHYS126F-04E Program', layout)
    while True:
        event, values = window.read()
        if event 