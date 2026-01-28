import random 


def roll_die():
    return random.randint(1, 6)


def play_turn(player_name):
    turn_score = 0
    
    print(f"\n{player_name}'s turn")

    while True:
        roll = roll_die()
        print(f"you rolled a {roll}")

        if roll == 1:
            return 0
        turn_score += roll

        choice = input('roll again? (y/n) ').lower()
        if choice != 'y':
            return turn_score


def main():
    scores = [0, 0]
    current_palyer = 0 # it's index

    while True:
        player_name = f'player {current_palyer + 1}'
        turn_score = play_turn(player_name)
        scores[current_palyer] += turn_score

        print(f"\nyou scored {turn_score} points this turn.")
        print(f"current scores: player 1: {scores[0]}, player 2: {scores[1]}")

        if scores[current_palyer] >= 100:
            print(f'{player_name} wins!')
            break 

        current_palyer = 1 if current_palyer == 0 else 0


if __name__ == '__main__':
    main()