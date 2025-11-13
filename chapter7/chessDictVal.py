STARTING_PIECES = {'a8': 'bR', 'b8': 'bN', 'c8': 'bB', 'd8': 'bQ',
'e8': 'bK', 'f8': 'bB', 'g8': 'bN', 'h8': 'bR', 'a7': 'bP', 'b7': 'bP',
'c7': 'bP', 'd7': 'bP', 'e7': 'bP', 'f7': 'bP', 'g7': 'bP', 'h7': 'bP',
'a1': 'wR', 'b1': 'wN', 'c1': 'wB', 'd1': 'wQ', 'e1': 'wK', 'f1': 'wB',
'g1': 'wN', 'h1': 'wR', 'a2': 'wP', 'b2': 'wP', 'c2': 'wP', 'd2': 'wP',
'e2': 'wP', 'f2': 'wP', 'g2': 'wP', 'h2': 'wP'}

def chessVal(board):
    valid = True
    piece_values = ['bK', 'wK', 'bQ', 'wQ', 'bB', 'wB', 'bN', 'wN', 'bR', 'wR', 'bP', 'wP']
    valid_spaces = []
    

    # loop for adding the proper spaces to the valid list
    for x in 'abcdefgh':
        for y in '12345678':
            valid_spaces.append(x + y)

    # loop through the keys in the valid spaces to make sure they're all valid
    for x in board.keys():
        if x not in valid_spaces:
            valid = False
            return valid
            
    
    values_list = list(board.values())
    
    # validate total pieces
    if len(values_list) > 32:
        valid = False
        return valid
    
    # validate all pieces are valid names
    for v in board.values():
        if v not in piece_values:
            valid = False
            return valid
    
    # validate number of pieces is correct for each colour
    bK_count = values_list.count(piece_values[0])
    wK_count = values_list.count(piece_values[1])
    bQ_count = values_list.count(piece_values[2])
    wQ_count = values_list.count(piece_values[3])
    bB_count = values_list.count(piece_values[4])
    wB_count = values_list.count(piece_values[5])
    bN_count = values_list.count(piece_values[6])
    wN_count = values_list.count(piece_values[7])
    bR_count = values_list.count(piece_values[8])
    wR_count = values_list.count(piece_values[9])
    bP_count = values_list.count(piece_values[10])
    wP_count = values_list.count(piece_values[11])

    # validate king count
    if bK_count > 1 or wK_count > 1:
        valid = False
        return valid
    
    # validate queen count
    if bQ_count > 1 or wQ_count > 1:
        valid = False
        return valid
    
    # validate rook count
    if bB_count > 2 or wB_count > 2:
        valid = False
        return valid
    
    # validate knight count
    if bN_count > 2 or wN_count > 2:
        valid = False
        return valid
    
    # validate rook count
    if bR_count > 2 or wR_count > 2:
        valid = False
        return valid
    
    # validate pawn count
    if bP_count > 8 or wP_count > 8:
        valid = False
        return valid
    
    return valid
    

print(chessVal(STARTING_PIECES))


