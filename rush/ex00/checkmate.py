def checkmate(board):
    board = board.splitlines()
    size = len(board)
    if len(board) == 0:
        return
    for row in board:
        if len(row) != size:
            print("error")
            return
    piece = "KRBQP"
    for row in range(len(board)):
        newrow = ""
        for col in range(len(board[row])):
            if board[row][col] in piece:
                newrow = newrow + board[row][col]
            else:
                newrow = newrow+"."
        board[row] = newrow
    kingrow = -1
    kingcol = -1
    kingcount = 0

    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == 'K':
                kingcount = kingcount+1
                kingrow = row
                kingcol = col
    if kingcount !=1:
        print("error")
        return
    if kingrow == -1:
        return

    for i in range(kingrow - 1, -1, -1):
        if board[i][kingcol] != '.':
            if board[i][kingcol] == 'R' or board[i][kingcol] == 'Q':
                print("Success")
                return
            break

    for i in range(kingrow + 1, len(board)):
        if board[i][kingcol] != '.':
            if board[i][kingcol] == 'R' or board[i][kingcol] == 'Q':
                print("Success")
                return
            break

    for i in range(kingcol - 1, -1, -1):
        if board[kingrow][i] != '.':
            if board[kingrow][i] == 'R' or board[kingrow][i] == 'Q':
                print("Success")
                return
            break

    for i in range(kingcol + 1, len(board[kingrow])):
        if board[kingrow][i] != '.':
            if board[kingrow][i] == 'R' or board[kingrow][i] == 'Q':
                print("Success")
                return
            break

    r = kingrow - 1
    c = kingcol - 1

    while r >= 0 and c >= 0:
        if board[r][c] != '.':
            if board[r][c] == 'B' or board[r][c] == 'Q':
                print("Success")
                return
            break
        r = r - 1
        c = c - 1

    r = kingrow - 1
    c = kingcol + 1

    while r >= 0 and c < len(board[r]):
        if board[r][c] != '.':
            if board[r][c] == 'B' or board[r][c] == 'Q':
                print("Success")
                return
            break
        r = r - 1
        c = c + 1

    r = kingrow + 1
    c = kingcol - 1

    while r < len(board) and c >= 0:
        if board[r][c] != '.':
            if board[r][c] == 'B' or board[r][c] == 'Q':
                print("Success")
                return
            break
        r = r + 1
        c = c - 1

    r = kingrow + 1
    c = kingcol + 1

    while r < len(board) and c < len(board[r]):
        if board[r][c] != '.':
            if board[r][c] == 'B' or board[r][c] == 'Q':
                print("Success")
                return
            break
        r = r + 1
        c = c + 1

    if kingrow + 1 < len(board):
        if kingcol - 1 >= 0:
            if board[kingrow + 1][kingcol - 1] == 'P':
                print("Success")
                return

        if kingcol + 1 < len(board[kingrow + 1]):
            if board[kingrow + 1][kingcol + 1] == 'P':
                print("Success")
                return

    print("Fail")