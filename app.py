def prompt_player_names():
    return [
        input("Player 1, please provide your name: "),
        input("Player 2, please provide your name: ")
    ]

def main():
    for index, player_name in enumerate(prompt_player_names(), 1):
        print(f"Player {index}: {player_name}")

if __name__ == '__main__':
    main()
