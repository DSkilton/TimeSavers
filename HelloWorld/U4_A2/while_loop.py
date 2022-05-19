teams = 0
players = 0
menu_option = 0
team_name = ""
player_name = ""
teams_list = []
individual_players_list = []


def menu():
    global menu_option
    menu_option = int(input("1. Add Player\t\t 2. Add Team \n"
                            "3. View Player\t\t 4. View Team \n"
                            "5. Delete Player\t 6. Delete Team \n"
                            "0. Exit"))


def select_option(menu_option):
    if menu_option == 1:
        pass
    elif menu_option == 2:
        add_players_to_teams()

    elif menu_option == 3:
        if not individual_players_list:
            print("No saved players, run menu option 1 first")

    elif menu_option == 4:
        if not teams_list:
            print("No saved teams, run menu option 2 first")
        view_teams()

    elif menu_option == 5:
        pass
    elif menu_option == 6:
        pass
    elif menu_option == 0:
        pass
    else:
        print("Something went horribly wrong")
    menu()


def add_player():
    player_name = input("Name to be added: ")
    individual_players_list.append(player_name)


def view_player():
    for player in individual_players_list:
        print(player)


def delete_player():
    pass


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


def view_teams():
    for team in teams_list:
        print(team)


def delete_team():
    pass



