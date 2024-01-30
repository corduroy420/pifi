#!/usr/bin/env python3
import os
import subprocess
from simple_term_menu import TerminalMenu

def get_wifi_networks():
    try:
        # Command to list available Wi-Fi networks
        cmd_result = subprocess.check_output(['sudo', 'iwlist', 'wlan0', 'scan'])
        networks = []
        for line in cmd_result.decode('utf-8').split('\n'):
            if "ESSID:" in line:
                ssid = line.split('"')[1]
                networks.append(ssid)
        return networks
    except subprocess.CalledProcessError as e:
        print("Failed to get Wi-Fi networks:", e)
        return []

def network_options_menu(network_name):
    # Placeholder for options within a network
    network_options = ["Connect to Network", "View Network Details", "Back"]
    network_menu = TerminalMenu(network_options, title=f"Network: {network_name}")
    while True:
        network_menu_index = network_menu.show()
        if network_menu_index is None or network_options[network_menu_index] == "Back":
            break
        # Here you can add actions for each option
        # For example, if network_menu_index == 0: # connect to network

# Clear the screen
os.system('clear')
quitting = False

# MENUS
options1 = ['Hacking Tools', 'Quit']
menu1 = TerminalMenu(options1, title='Pifi')

options2 = ['Show Networks', 'Back']
menu2 = TerminalMenu(options2, title='Hacking Tools')

while not quitting:
    menu1_index = menu1.show()
    if menu1_index is None:  # Handle the escape key
        break
    choice1 = options1[menu1_index]

    if choice1 == "Hacking Tools":
        while True:
            menu2_index = menu2.show()
            if menu2_index is None or options2[menu2_index] == "Back":  # Handle the back option
                break
            choice2 = options2[menu2_index]

            if choice2 == "Show Networks":
                networks = get_wifi_networks()
                if networks:
                    networks.append("Back")  # Add a back option to the network list
                    networks_menu = TerminalMenu(networks, title="Available\nNetworks")
                    network_menu_index = networks_menu.show()
                    if network_menu_index is None or networks[network_menu_index] == "Back":
                        continue  # Go back to the previous menu
                    network_options_menu(networks[network_menu_index])
                else:
                    print("No networks found.")

    elif choice1 == "Quit":
        quitting = True
