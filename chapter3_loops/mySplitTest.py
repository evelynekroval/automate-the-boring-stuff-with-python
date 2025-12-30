while True:
    player_move = str(input('>')).lower()[:1]
    if player_move == "q":
        break
    else:
        print(player_move)