import os
from os import system


def mainUser():
    print("Please press 1 to view teams and there players!")
    print("Please press 2 to view upcoming matches!")
    print("Please press 3 to view previous matches results!")

    userMainInput = input("Please enter your choice: ")

    if userMainInput == "1":
        viewTeamsAndPlayers()
    elif userMainInput == "2":
        upcomingMatches()
    elif userMainInput == "3":
        previousMatchResults()
    else:
        print("Please enter a correct number next time!")
        system("Clear")
        mainUser()
        
    
    
    
    
    
    
    
    

# ****************************************************************
# ********************** All FUNCTIONS ***************************
# ****************************************************************
    

# Remove player function (Called inside of remove team or player function)
    # They are able view view the teams and upon entry of a team they will be able to
    # view the players.
def viewTeamsAndPlayers():
    system("clear")
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

    choice = input("Enter the number of the team to view team players: ")
        
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
    system("clear")
    print(f"Players in '{os.path.splitext(selected_team_file)[0]}':")
    
    with open(team_filename, 'r') as team_file:
        players = team_file.readlines()
        for idx, player in enumerate(players, start=1):
            print(f"{idx}. {player.strip()}")
            
        print("Press 1 to go back to view Teams")
        print("Press 2 to go back to main menu")
        
        inputBack = input("Press anything to go back: ")
        system("clear")
        if inputBack == "1":
            viewTeamsAndPlayers()
        else:
            mainUser()
            
            
            
            
            
# upcoming matches function being called in mainUser
def upcomingMatches():
    f = open("DB/UpcomingMatches.txt", "r")
    print(f.read())


# previous matches results function being called in mainUser
def previousMatchResults():
    f = open("DB/destination.txt", "r")
    print(f.read())


