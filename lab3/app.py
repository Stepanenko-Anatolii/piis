import time
import chess
import eval
import negamax as nmax
import negascout as nscout


def userMove(board):
    move = input("Enter move: ")
    move = chess.Move.from_uci(str(move))
    board.push(move)

def main():
    depth = 3
    board = chess.Board()
    board.legal_moves
    n = 0
    print(board)
    while n < 100:
        if n % 2 == 0:
            print("Negascout turn:")
            move = nscout.controller(depth, board)
            move = chess.Move.from_uci(str(move))
            board.push(move)
        else:
            print("Negamax turn:")
            move = nmax.controller(depth, board)
            move = chess.Move.from_uci(str(move))
            board.push(move)
        print(board)
        n += 1
        #time.sleep(5)


if __name__ == "__main__":
    main()
