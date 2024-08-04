class Team:
    def __init__(self, name, participants_count, coach, captain):
        self.name = name
        self.participants_count = participants_count
        self.coach = coach
        self.captain = captain

    def display_info(self):
        print(f"Jamoa nomi: {self.name}")
        print(f"Soni: {self.participants_count}")
        print(f"Murabbiy: {self.coach}")
        print(f"Kapitan: {self.captain}")
        print()

def sort_teams_by_name(teams):
    sorted_teams = sorted(teams, key=lambda team: team.name)
    for team in sorted_teams:
        team.display_info()

def find_team_by_name(teams, new_team_name):
    found = False
    for team in teams:
        if team.name == new_team_name:
            team.display_info()
            found = True
            break
    if not found:
        print("Bunday jamoa mavjud emas.")

team1 = Team("Eagles", 20, "John Smith", "Mike Johnson")
team2 = Team("Tigers", 18, "Alice Brown", "Chris Green")
team3 = Team("Sharks", 22, "Emma Wilson", "David White")

teams = [team1, team2, team3]

sort_teams_by_name(teams)

find_team_by_name(teams, "Sharks")

find_team_by_name(teams, "Wolves")
