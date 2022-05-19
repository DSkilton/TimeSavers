teams = 0
players = 0
menu_option = 0
team_name = ""
player_name = ""
teams_list = []


def menu():
    menu_option = int(input("1. Add Player\t\t 2. Add Team \n"
          "3. View Player\t\t 4. View Team \n"
          "5. Delete Player\t 6. Delete Team \n"
          "0. Exit"))

menu()

def select_option(menu_option):
    if menu_option == 1:
        pass
    elif menu_option == 2:
        add_players_to_teams()
    elif menu_option == 3:
        pass
    elif menu_option == 4:
        pass
    elif menu_option == 5:
        pass
    elif menu_option == 6:
        pass
    elif menu_option == 0:
        pass
    else:
        print("Something went horribly wrong")


def add_players_to_teams():
    for i in range(1, 4):
        list_string = ""
        team_name = input("Enter team name")
        list_string += "Team Name: " + team_name + " "
        i += 1

        for j in range(1, 5):
            player_name = input("Enter a player name")
            list_string += "Player: " + player_name + " "
            j += 1


        teams_list.append(list_string)

