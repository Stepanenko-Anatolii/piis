def getEvaluation(board):
    i = 0
    evaluation = 0
    x = True
    try:
        x = bool(board.piece_at(i).color)
    except AttributeError as e:
        x = x
    while i < 63:
        i += 1
        pieceValue = getPieceValue(str(board.piece_at(i)))
        evaluation = evaluation + (pieceValue if x else -pieceValue)
    return evaluation


def getPieceValue(p):
    if p in ["P", "p"]:
        return 1
    if p in ["N", "n", "B", "b"]:
        return 3
    if p in ["R", "r"]:
        return 4
    if p in ["Q", "q"]:
        return 8
    if p in ["K", "k"]:
        return 100
    return 0


def maxDepth():
    return 4