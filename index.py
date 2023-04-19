new_board = [["_", "_", "_"], ["_", "_", "_"], ["_", "_", "_"]]


plays = 0

def render(board):
    print(" ", 0, 1, 2)
    print("------------------")
    for i in range(len(board)):
        print(i, "|", board[i][0], board[i][1], board[i][2], "|")
    print("------------------")

def get_move(player):
    x = int(input("Enter your move's X coordinate" + " (player 1):"))
    y = int(input("Enter your move's Y coordinate" + " (player 2):"))
 
    return [x, y]
    
def make_move(old_board, move_coords, player):
    x = move_coords[0]
    y = move_coords[1]
    
    old_board[x][y] = "X" if player == 1 else "O"
    
    return old_board

def main:
    isPlaying = true
    player = 0
    
    render(new_board)
    
    game_board = [["_", "_", "_"], ["_", "_", "_"], ["_", "_", "_"]]

    
    while isPlaying:
        coords = get_move(player)
        
        if game_board[coords[0]][coords[1]] == "_":
            print("Please try again")
        else
            game_board = make_move(game_board, coords, player)
            
        render(game_board)
