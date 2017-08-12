import pygame
import sys
import time
from pygame.locals import *

import displayRenderer
import switchRequestor
import inputReader

MENU_STRUCTURE = [
    ["main menu",
     "",
     "1 - toggle outlet 1: {}",
     "2 - toggle outlet 2: {}",
     "3 - toggle outlet 3: {}",
     "4 - toggle outlet 4: {}",
     "",
     "ESC - exit application"]
]


def terminate():
    """terminate the program"""
    pygame.quit()
    sys.exit()


def check_for_input():
    """process termination request"""
    result = ""
    for event in pygame.event.get(QUIT):
        terminate()
    for event in pygame.event.get(KEYUP):
        if event.key == K_ESCAPE:
            result = "exit"
        elif event.key == K_1:
            result = "1"
        elif event.key == K_2:
            result = "2"
        elif event.key == K_3:
            result = "3"
        elif event.key == K_4:
            result = "4"
    return result


def format_main_menu(switch_states):
    menu = list()
    menu.append(MENU_STRUCTURE[0][0])
    menu.append(MENU_STRUCTURE[0][1])
    menu.append(MENU_STRUCTURE[0][2].format(str(switch_states[0])))
    menu.append(MENU_STRUCTURE[0][3].format(str(switch_states[1])))
    menu.append(MENU_STRUCTURE[0][4].format(str(switch_states[2])))
    menu.append(MENU_STRUCTURE[0][5].format(str(switch_states[3])))
    menu.append(MENU_STRUCTURE[0][6])
    menu.append(MENU_STRUCTURE[0][7])
    return menu


# main application loop
if __name__ == '__main__':
    pygame.init()
    switch_states = [False] * 4
    input_states = [False] * 4
    debug_log = dict()
    display = displayRenderer.DisplayRenderer(debug_log)
    fullscreen = False
    show_menu = True
    menu_select = 0
    menu_page = format_main_menu(switch_states)
    display.open(fullscreen)
    inputs = inputReader.InputReader(debug_log)
    inputs.setup_pins()
    requestor = switchRequestor.SwitchRequestor()
    requestor.open("http://192.168.178.108", "1")
    requestor.login()
    while True:
        time.sleep(0.01)
        input_value = check_for_input()
        if show_menu:
            if menu_select == 0:
                if input_value == "1":
                    switch_states[0] = not switch_states[0]
                    requestor.toggle_switches(switch_states, 0)
                    menu_page = format_main_menu(switch_states)
                elif input_value == "2":
                    switch_states[1] = not switch_states[1]
                    requestor.toggle_switches(switch_states, 1)
                    menu_page = format_main_menu(switch_states)
                elif input_value == "3":
                    switch_states[2] = not switch_states[2]
                    requestor.toggle_switches(switch_states, 2)
                    menu_page = format_main_menu(switch_states)
                elif input_value == "4":
                    switch_states[3] = not switch_states[3]
                    requestor.toggle_switches(switch_states, 3)
                    menu_page = format_main_menu(switch_states)
                elif input_value == "exit":
                    requestor.logout()
                    terminate()
            display.render_menu(menu_page)
        # input_states = inputs.read_inputs()
        display.update()
