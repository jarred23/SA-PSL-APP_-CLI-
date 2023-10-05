
import os
import time
from os import system
# add the system("clear where all needed")

# main admin script
def adminMain():
    print("Please press 1 to add a new soccer team!")
    print("Please press 2 to add players to a team")
    print("Please press 3 to remove a player or a team")
    print("Please press 4 to view all users on SA PSL")
    print("Please press 5 to add upcoming match")
    print("Please press 6 to add previous match results")
    
    adminInput = input("Please enter a number: ")
    
    if adminInput == "1":
        addTeam()
    elif adminInput == "2":
        addPlayer()
    elif adminInput == "3":
        removeTeamOrPlayer()
    elif adminInput == "4":
        viewUsers()
    elif adminInput == "5":
        upcomingMatches()
    elif adminInput == "6":
        previous_Match_Results()
    else:
        print("Admin, please enter a correct number!")
        adminMain()







# ****************************************************************
# ********************** All FUNCTIONS ***************************
# ****************************************************************


# add team script
def addTeam():
    team_name = input("Enter the name of the new team: ")
    team_filename = f"DB/teams/{team_name}.txt"
    
    if os.path.exists(team_filename):
        print(f"The team '{team_name}' already exists.")
        return
    
    with open("team_list.txt", 'a') as team_list_file:
        team_list_file.write(f"{team_name}\n")
    
    with open(team_filename, 'w') as team_file:
        team_file.write(f"Team: {team_name}\n")
        input(f"Team '{team_name}' has been created.")
        system("clear")
        adminMain()
        

# add player script
def addPlayer():
    team_list = []

    with open("team_list.txt", 'r') as team_list_file:
        team_list = [line.strip() for line in team_list_file]
    
    if not team_list:
        print("No teams exist. Please create a team first.")
        return
    
    print("Teams:")
    for idx, team in enumerate(team_list, start=1):
        print(f"{idx}. {team}")
    
    choice = input("Enter the number of the team to which you want to add a player: ")
    
    try:
        choice = int(choice)
        if choice < 1 or choice > len(team_list):
            print("Invalid choice. Please enter a valid number.")
            return
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return
    
    selected_team = team_list[choice - 1]
    team_filename = f"DB/teams/{selected_team}.txt"
    
    player_name = input("Enter the name of the player: ")
    with open(team_filename, 'a') as team_file:
        team_file.write(f"Player: {player_name}\n")
        print(f"Player '{player_name}' has been added to '{selected_team}'.")
        system("clear")
        adminMain()



# remove team or player main function
def removeTeamOrPlayer():
    print("Please press 1 to remove players")
    print("Please press 2 to remove a team")
    
    rTOP = input("Please enter a number: ")
    
    if rTOP == "1":
        removePlayer()
    elif rTOP == "2":
        removeTeam()
    else:
        print("Please enter the correct number!")
        removeTeamOrPlayer()


# view users script
def viewUsers():
    user_data = [] 

    with open('DB/users/user_data.txt', 'r') as file:
        lines = file.readlines()

    for i in range(0, len(lines), 5):
        name = lines[i].split(': ')[1].strip()
        email = lines[i + 1].split(': ')[1].strip()
        phone_number = lines[i + 2].split(': ')[1].strip()
        user_data.append((name, email, phone_number))

    num_users = len(user_data)
    print(f"Number of users: {num_users}")

    for i, (name, email, phone_number) in enumerate(user_data, start=1):
        print(f"User {i}:")
        print(f"Name: {name}")
        print(f"Email: {email}")
        print(f"Phone Number: {phone_number}")
        print()
    
    input("press anything to go back: ")
    system("clear")
    adminMain()
    

# Remove player function (Called inside of remove team or player function)
def removePlayer():

    db_folder = "DB/teams"

    if not os.path.exists(db_folder):
        print(f"The '{db_folder}' folder does not exist. Please create it and add team files.")
        return

    team_files = [filename for filename in os.listdir(db_folder) if filename.endswith(".txt")]

    if not team_files:
        print("No team files found in the 'DB' folder. Please add team files.")
        return

    print("Teams:")
    for idx, team_file in enumerate(team_files, start=1):
        print(f"{idx}. {os.path.splitext(team_file)[0]}")

    choice = input("Enter the number of the team from which you want to remove a player: ")

    try:
        choice = int(choice)
        if choice < 1 or choice > len(team_files):
            print("Invalid choice. Please enter a valid number.")
            return
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return

    selected_team_file = team_files[choice - 1]
    team_filename = os.path.join(db_folder, selected_team_file)

    print(f"Players in '{os.path.splitext(selected_team_file)[0]}':")
    with open(team_filename, 'r') as team_file:
        players = team_file.readlines()
        for idx, player in enumerate(players, start=1):
            print(f"{idx}. {player.strip()}")

    player_choice = input("Enter the number of the player to remove: ")

    try:
        player_choice = int(player_choice)
        if player_choice < 1 or player_choice > len(players):
            print("Invalid choice. Please enter a valid number.")
            return
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return

    print("Players before removal:")
    for idx, player in enumerate(players, start=1):
        print(f"{idx}. {player.strip()}")

    removed_player = players.pop(player_choice - 1)

    print("Players after removal:")
    for idx, player in enumerate(players, start=1):
        print(f"{idx}. {player.strip()}")

    with open(team_filename, 'w') as team_file:
        team_file.writelines(players)

    print(f"Player '{removed_player.strip()}' has been removed from '{os.path.splitext(selected_team_file)[0]}'.")
    system("clear")
    adminMain()


# Remove team function (Called inside of remove team or player function)
def removeTeam():
    db_teams_folder = "DB/teams"

    if not os.path.exists(db_teams_folder):
        print(f"The '{db_teams_folder}' folder does not exist. Please create it and add team files.")
        return

    team_files = [filename for filename in os.listdir(db_teams_folder) if filename.endswith(".txt")]

    if not team_files:
        print("No team files found in the 'DB/teams' folder. Please add team files.")
        return

    print("Teams:")
    for idx, team_file in enumerate(team_files, start=1):
        print(f"{idx}. {os.path.splitext(team_file)[0]}")

    choice = input("Enter the number of the team to remove: ")

    try:
        choice = int(choice)
        if choice < 1 or choice > len(team_files):
            print("Invalid choice. Please enter a valid number.")
            return
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return

    selected_team_file = team_files[choice - 1]
    removed_team = os.path.splitext(selected_team_file)[0]
    team_filename = os.path.join(db_teams_folder, selected_team_file)

    if os.path.exists(team_filename):
        os.remove(team_filename)
    else:
        print(f"Team file '{team_filename}' does not exist.")

    with open("team_list.txt", 'r') as team_list_file:
        team_list = [line.strip() for line in team_list_file]

    if removed_team in team_list:
        team_list.remove(removed_team)

        with open("team_list.txt", 'w') as team_list_file:
            team_list_file.writelines('\n'.join(team_list))
    else:
        print(f"Team '{removed_team}' not found in team list.")

    input(f"Team '{removed_team}' has been removed.")
    system("clear")
    adminMain()
    

# For the admin to add upcoming matches so that users will know who is playing and what time
# user will be able to see who is playing against who 
# and what time will be playing 

def select_team_upcoming_match(team_list):
    if not team_list:
        print("No teams exist. Please create a team first.")
        return None

    print("Teams:")
    for idx, team in enumerate(team_list, start=1):
        print(f"{idx}. {team}")

    choice = input("Please choose a team: ")

    try:
        choice = int(choice)
        if 1 <= choice <= len(team_list):
            return team_list[choice - 1]
        else:
            print("Invalid choice. Please enter a valid number.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

    return None

def write_game_data_to_upcoming_matches(Team1, Team2):
    data = f"\n{Team1} VS {Team2}\n"
    file_path = "DB/UpcomingMatches.txt" 
    with open(file_path, "a") as file:
        file.write(data + "\n")

def upcomingMatches():
    team_directory = "DB/teams"
    team_list = os.listdir(team_directory)
    Team1 = select_team_upcoming_match(team_list)
    if Team1 is None:
        return
    system("clear")
    Team2 = select_team_upcoming_match(team_list)
    if Team2 is None:
        return
    system("clear")

    write_game_data_to_upcoming_matches(Team1, Team2)


























# User will be able to check previous matches results will display
# Teams , Location , Team 1 , Team 2 and the scores 

source_file = "DB/source.txt"
destination_file = "DB/destination.txt"


def select_team(team_list):
    if not team_list:
        print("No teams exist. Please create a team first.")
        return None

    print("Teams:")
    for idx, team in enumerate(team_list, start=1):
        print(f"{idx}. {team}")

    choice = input("Please choose a team: ")

    try:
        choice = int(choice)
        if 1 <= choice <= len(team_list):
            return team_list[choice - 1]
        else:
            print("Invalid choice. Please enter a valid number.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

    return None

def get_game_data():
    date_played = input("Enter Date Played: ")
    system("clear")
    location_played = input("Enter Location Played At: ")
    system("clear")
    team_directory = "DB/teams"
    team_list = os.listdir(team_directory)
    team1_name = select_team(team_list)
    if team1_name is None:
        return None
    system("clear")
    team2_name = select_team(team_list)
    if team2_name is None:
        return None
    system("clear")
    team1_score = input("Enter Team 1 Score: ")
    system("clear")
    team2_score = input("Enter Team 2 Score: ")
    system("clear")
    return date_played, location_played, team1_name, team2_name, team1_score, team2_score

def write_game_data_to_source(date, location, team1, team2, team1_score, team2_score):
    data = f"\nDate Played: {date}\nLocation Played At: {location}\nTeam 1: {team1}\nTeam 2: {team2}\nTeam 1 Score: {team1_score}\nTeam 2 Score: {team2_score}"
    with open(source_file, "a") as file:
        file.write(data + "\n")

def move_data_to_destination():
    with open(source_file, "r") as source, open(destination_file, "a") as destination:
        for line in source:
            destination.write(line)
    with open(source_file, "w"):
        pass

def previous_Match_Results():
    game_data = get_game_data()
    
    if game_data is not None:
        date_played, location_played, team1_name, team2_name, team1_score, team2_score = game_data
        write_game_data_to_source(date_played, location_played, team1_name, team2_name, team1_score, team2_score)
        print("Game data has been saved to source file.")
        input("Please press any key to continue back ")
    
        seconds_in_1_minute = 60
        time.sleep(seconds_in_1_minute)
        move_data_to_destination()
        print("Game data has been moved to the destination file.")

