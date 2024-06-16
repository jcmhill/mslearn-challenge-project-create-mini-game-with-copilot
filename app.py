from random import randint 

player_score = 0
computer_score = 0

while True:
    print('Rock...')
    print('Paper...')
    print('Scissors...')

    player = input('Player, make your move: ').lower()
    rand_num = randint(0, 2)

    if player == 'rock':
        if rand_num == 0:
            print('Computer chose rock. It\'s a tie!')
        elif rand_num == 1:
            print('Computer chose paper. Computer wins this round!')
            computer_score += 1
        else:
            print('Computer chose scissors. You win this round!')
            player_score += 1
    elif player == 'paper':
        if rand_num == 0:
            print('Computer chose rock. You win this round!')
            player_score += 1
        elif rand_num == 1:
            print('Computer chose paper. It\'s a tie!')
        else:
            print('Computer chose scissors. Computer wins this round!')
            computer_score += 1
    else:
        print('Invalid move. Please choose rock, paper, or scissors.')

    play_again = input('Do you want to play again? (yes/no): ').lower()
    if play_again != 'yes':
        print(f'Final score: Player {player_score}, Computer {computer_score}')
        break