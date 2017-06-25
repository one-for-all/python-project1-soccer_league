import csv

def read_data():
    '''
    return a list of dicts of players
    '''
    with open('soccer_players.csv', 'r') as csvfile:
         soccer_players = list(csv.DictReader(csvfile))
         return soccer_players

def divide_into_teams(players):
    '''
    Create variables and programming logic to divide the 18 players into three teams: Sharks, Dragons and Raptors.
    Make sure the teams have the same number of players on them,
    and that the experience players are divided equally across the three teams.
    '''
    sharks = []
    dragons = []
    raptors = []
    experienced  = []
    non_exp = []

    # Divide players into experienced and not experienced
    for player in players:
        if player['Soccer Experience'] == 'YES':
            experienced.append(player)
        else:
            non_exp.append(player)
    # Assign experienced players evenly
    total_exp = len(experienced)
    sharks.extend(experienced[:int(total_exp/3)])
    dragons.extend(experienced[int(total_exp/3):int(total_exp*2/3)])
    raptors.extend(experienced[int(total_exp*2/3):])

    # Assign non_experienced players evenly
    total_non_exp = len(non_exp)
    sharks.extend(non_exp[:int(total_non_exp / 3)])
    dragons.extend(non_exp[int(total_non_exp / 3):int(total_non_exp * 2 / 3)])
    raptors.extend(non_exp[int(total_non_exp * 2 / 3):])

    return sharks, dragons, raptors

def save_teams(sharks, dragons, raptors):
    player_output = '{}, {}, {}\n'
    with open('teams.txt', 'w') as file:
        file.write('Sharks\n')
        for player in sharks:
            file.write(player_output.format(player['Name'], player['Soccer Experience'], player['Guardian Name(s)']))
        file.write('Dragons\n')
        for player in dragons:
            file.write(player_output.format(player['Name'], player['Soccer Experience'], player['Guardian Name(s)']))
        file.write('Raptors\n')
        for player in raptors:
            file.write(player_output.format(player['Name'], player['Soccer Experience'], player['Guardian Name(s)']))

def write_welcome_letters(sharks, dragons, raptors):
    '''
    Make sure that each file begins with the text "Dear" followed by the guardian(s) name(s). Also include the additional required information:
    player's name, team name, and date & time of first practice.
    '''
    letter = 'Dear {guardians},\n\n{name} is assigned to team {team}.\nFirst day of practice is June 26th at 1 pm.\nHave a wonderful summer!\n'
    for player in sharks:
        with open('_'.join(player['Name'].lower().split())+'.txt', 'w') as welcome_letter:
            welcome_letter.write(letter.format(guardians=player['Guardian Name(s)'], name=player['Name'], team='Sharks'))
    for player in dragons:
        with open('_'.join(player['Name'].lower().split())+'.txt', 'w') as welcome_letter:
            welcome_letter.write(letter.format(guardians=player['Guardian Name(s)'], name=player['Name'], team='Dragons'))
    for player in raptors:
        with open('_'.join(player['Name'].lower().split())+'.txt', 'w') as welcome_letter:
            welcome_letter.write(letter.format(guardians=player['Guardian Name(s)'], name=player['Name'], team='Raptors'))

def main():
    players = read_data()
    teams = divide_into_teams(players)
    save_teams(*teams)
    write_welcome_letters(*teams)


if __name__ == '__main__':
    main()
