from stockfish import Stockfish
import random


player_white = bool(random.getrandbits(1))

stockfish = Stockfish(path="./stockfish")

moves = []
count = 0
print(stockfish.get_board_visual(player_white))

blind = False
while not (stockfish.get_evaluation()['type'] == "mate") & (( stockfish.get_evaluation()['value'] == 1) or  (stockfish.get_evaluation()['value'] == -1)):


    if (player_white) & (count<1):
        move = input("you are white. \ntype in your first move:\n")
        while not stockfish.is_move_correct(move):
            print("your move is invalid\n")
            move = input("\n type in your  move:\n")


        stockfish.make_moves_from_current_position([move])
        moves.append(move)
        if not blind:
            print(stockfish.get_board_visual(player_white))
        count+=1

    bm = stockfish.get_best_move()
    stockfish.make_moves_from_current_position([bm])
    moves.append(bm)
    print(f"stockfish made move {bm}")
    if not blind:
        print(stockfish.get_board_visual(player_white))
    move = input("\n type in your  move:\n")
    while not stockfish.is_move_correct(move):
        move = input("invalid move. type in your  move:\n")

    stockfish.make_moves_from_current_position([move])
    moves.append(move)
    if not blind:
        print(stockfish.get_board_visual(player_white))
    print(f"you made move {bm} \n")

if stockfish.get_evaluation()['value'] == -1:
    print("\n \nblack won!!! \n \n")
else:
    print("\n \nwhite won!!! \n \n")
print(f"\n \n game over! here were the moves \n \n {moves}\n \n" )
print(stockfish.get_board_visual(plater_white))
