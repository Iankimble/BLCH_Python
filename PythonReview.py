import random

def play():
    user = input("whats your choice? rock , paper , scissors")
    user = user.lower()

    computer = random.choice([  'rock',  'paper', 'scissors'])

    if user == computer:
        return "you and the computer have both chosen paper. its a tie"
    
    if is_win(user, computer):
        return "you have chosen scissors and the computer has chosen paper You won!"
    return "you have chosen rock and the computer has chose paper you lost :("


def is_win(player, opponent):
        # return is true the player beats the opponent
        # winning conditions: rock  > scissors, scissors > paper, paper > rock
        if (player == 'rock' and opponent == 'scissors') or (player == 'scissors' and opponent == 'paper') or (player == 'paper' and opponent == 'rock'):
            return True
        return False

if __name__ == '__main__':
     print(play())