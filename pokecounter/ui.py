"""
UI Component of PokeCounter

Opens the configuration window and allows the
user to set the config values and start/stop
the server.
"""

from fileinput import filename
import PySimpleGUI as sg
from pokecounter.pokedex import POKEDEX
from pokecounter.config import ICON_PATH, STANDARD_SPRITES

poke_list = [f"{poke['id']}:  {poke['name']}" for poke in POKEDEX]


def start_window():
    layout = [
        [
            sg.Text("Pokemon Choice: "),
            sg.Combo(poke_list, readonly=True, enable_events=True, key="-POKE_CHOICE-"),
            sg.Button("OK"),
        ],
        [sg.HSeparator()],
        [
            sg.Push(),
            sg.Column([[sg.Image(key="-IMAGE_BOX-")]], element_justification="c"),
            sg.Push(),
        ],
    ]
    window = sg.Window(
        title="PokeCounter Configuration UI", icon=ICON_PATH, layout=layout
    )
    printed = False
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        if event == "-POKE_CHOICE-":
            poke_num = values["-POKE_CHOICE-"][0:3]
            sprite_path = STANDARD_SPRITES / f"{poke_num}.png"
            window["-IMAGE_BOX-"].update(filename=sprite_path)
    window.close()
