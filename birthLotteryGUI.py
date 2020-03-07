# TO DO - Build listbox that appends consecutive results
# build menu/dropdown with search params (billionaire, gender, continent etc.)


import PySimpleGUI as sg
import PyInstaller, random

sg.theme('Dark')

layout = [[sg.Text('Welcome to The Birth Lottery!\n\n\
Click "Go" to initiate metempsychosis.\n')],
    [sg.Button('Go'), sg.Button('Exit')]

]

window = sg.Window("Birth Lottery", layout)

# these values will become a webscraped dictionary
worldPop = 7770000000
billionPop = 2153
popRatio = billionPop / worldPop

while True: # main program loop
    event, values = window.read()
    print(event, values)
    if event in (None, 'Exit'):
        break
    if event == 'Go':
        # code goes here - values[0] references first user input
        result = random.randint(0, worldPop)
        if result in range(0, billionPop):
            sg.Popup('you are number %s of %s' % (result, billionPop))
        else:
            sg.Popup('Not a billionaire this time!')
    
window.close()
del window
