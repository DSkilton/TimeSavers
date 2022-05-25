teams = 0
players = 0
menu_option = 0
team_name = ""
player_name = ""
teams_list = ['Team Name: Team1 Player: Name1 Player: Name2 ', 'Team Name: Team2 Player: Name1 Player: Name2 ']
individual_players_list = []


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
        delete_team()

    elif menu_option == 6:
        add_score_to_individual_players_list()

    elif menu_option == 7:
        add_team_score_to_teams_list()

    elif menu_option == 0:
        exit()

    else:
        print("Something went horribly wrong")
        menu()


def add_player():
    for j in range(1, 20):
        player_name = input("Name to be added: ")
        individual_players_list.append(player_name)
        j += 1


def view_player():
    i = 0
    for player in individual_players_list:
        print(i, ". ", player)
        i += 1


def add_score_to_individual_players_list():
    i = 0  # i sets the position in the list, remember data structures start at 0 not 1
    for player in individual_players_list:  # for each player in the list, the following will run
        points = input("Enter points for " + player)
        individual_players_list[i] += " " + points  # at position i, the points will be appended to player
        i += 1  # i.e. on the first loop, it will update position 0
        # on the second loop it will update position 1


def delete_player():
    print("These are your current players")
    view_player()

    player_index = int(input("Input the number of the player you would like to delete "))
    individual_players_list.pop(player_index)

    print("Your new list of players")
    view_player()


def add_players_to_teams():
    for i in range(1, 3):
        list_string = ""
        team_name = input("Enter team name ")
        list_string += "Team Name: " + team_name + " "
        i += 1

        for j in range(1, 3):
            player_name = input("Enter a player name ")
            list_string += "Player: " + player_name + " "
            j += 1
        teams_list.append(list_string)


def view_teams():
    i = 0
    for team in teams_list:
        print(i, ". ", team)
        i += 1


def delete_team():
    print("These are your current teams")
    view_teams()

    team_index = int(input("Input the number of the team you would like to delete "))
    teams_list.pop(team_index)

    print("Your new list of players")
    view_teams()


def add_team_score_to_teams_list():
    i = 0  # i sets the position in the list, remember data structures start at 0 not 1
    for team in teams_list:  # for each player in the list, the following will run
        prefix_trim = team.replace("Team Name: ", "")
        suffix_trim = prefix_trim.replace(" Player: Name1 Player: Name2 ", "")
        points = input("Enter points for " + suffix_trim)
        teams_list[i] = points + " for team " + team  # at position i, the points will be appended to player
        i += 1  # i.e. on the first loop, it will update position 0
        # on the second loop it will update position 1


# menu()
add_team_score_to_teams_list()
print(teams_list)