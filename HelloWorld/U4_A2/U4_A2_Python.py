teams = 0
players = 0
menu_option = 0
team_name = ""
player_name = ""
teams_list = []
individual_players_list = ["Duncan", "Mark", "Cher"]


def menu():
    global menu_option
    menu_option = int(input("1. Add Player\t\t 2. Add Team \n"
                            "3. View Player\t\t 4. View Team \n"
                            "4. Delete Player\t\t 5. Delete Team \n"
                            "6. Add Player Score\t 7. Add Team Score \n"
                            "0. Exit"))


def select_option(menu_option):
    if menu_option == 1:
        add_player()

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
        add_score_to_individual_players_list()
    elif menu_option == 7:
        pass
    elif menu_option == 8:
        pass
    elif menu_option == 0:
        pass
    else:
        print("Something went horribly wrong")
        menu()


def add_player():
    for j in range(1, 5):
        player_name = input("Name to be added: ")
        individual_players_list.append(player_name)
        j += 1


def view_player():
    for player in individual_players_list:
        print(player)


def add_score_to_individual_players_list():
    i = 0 # i sets the position in the list, remember data structures start at 0 not 1
    for player in individual_players_list: # for each player in the list, the following will run
        points = input("Enter points for " + player)
        individual_players_list[i] += " " + points  # at position i, the points will be appended to player
        i += 1                                      # i.e. on the first loop, it will update position 0
                                                    # on the second loop it will update position 1

def delete_player():
    i = 0
    print("These are your current players")
    for player in individual_players_list: # prints current list with a number next to it. The number is the player's index
        print(i, ". ", player)             # with the end, we can pop elements out of the list 
        i += 1


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


# menu()
delete_player()