
print("Welcome to NTEM Sales, select from the following options or 0. to exit")

menu = {}
menu['1'] = "Option 1"
menu['2'] = "Option 2"
menu['3'] = "Option 3"
menu['0'] = SystemExit


menu_options = menu.keys() # returns the dictionary keys
sorted(menu_options)

for menu_option in menu_options:
    print(menu_option, menu[menu_option])
