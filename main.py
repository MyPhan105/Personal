# My Phan
# PSID 2176210
# lab 10.15

if __name__ == '__main__':
    class team:
        def __init__(self):
            self.team_name = 'none'
            self.team_wins = 0.0
            self.team_losses = 0.0

        def get_win_percentage(self):
            return self.team_wins / (self.team_wins + self.team_losses)


    student_team = team()
    # take input from user
    input_name = input()
    input_wins = int(input())
    input_losses = int(input())

    student_team.team_name = input_name
    student_team.team_wins = input_wins
    student_team.team_losses = input_losses

    win_percentage = student_team.get_win_percentage()
    if win_percentage > 0.5:
        print(f'Congratulations, Team {input_name} has a winning average!')
    else:
        print(f'Team {input_name} has a losing average.')
