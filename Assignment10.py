import pandas as pd

all_data = pd.read_csv("cfb.csv")

print("Welcome to your CFB analyzer!")

analyze = True

#game loop
while analyze == True:

    #input validation
    season = input("Enter the season you would like to analyze (yyyy): ").strip()
    
    if len(season) != 4 or not season.isdigit():
        print("Invalid input. Please enter a 4 digit year in (yyyy) form.")
        continue

    elif season not in all_data["Season"].astype(str).values:
        print("Season not found. Please try again.")
        continue

    selected_data = all_data.loc[all_data["Season"] == int(season)]

    #dictionary
    win_categories = {
        "10+ wins": [],
        "8-9 wins": [],
        "6-7 wins": [],
        "Fewer than 6 wins": []
    }

    #sort the teams into categories
    for _, row in selected_data.iterrows():
        wins = row["Win"]
        team = row["Team"]

        if wins > 9:
            win_categories["10+ wins"].append(team)
        elif wins > 7:
            win_categories["8-9 wins"].append(team)
        elif wins > 5:
            win_categories["6-7 wins"].append(team)
        else:
            win_categories["Fewer than 6 wins"].append(team)

    #print out the results
    print(f"College Football Records for {season}")

    print("\nTeams with a record of 10+ wins:")
    for team in win_categories["10+ wins"]:
        print(team)

    print("\nTeams with a record of 8-9 wins:")
    for team in win_categories["8-9 wins"]:
        print(team)
    
    print("\nTeams with a record of 6-7 wins:")
    for team in win_categories["6-7 wins"]:
        print(team)

    print("\nTeams with 5 wins or less:")
    for team in win_categories["Fewer than 6 wins"]:
        print(team)

    #analyze other season loop
    if input("Enter Y to analyze a different season. " \
    "Else, enter anything to quit. ").lower().strip() != "y":
        break
