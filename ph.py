"""This is a tic tac toe game."""


XGUESS: str = "\U0000274C"
OGUESS: str = "\U00002B55"
SQUARE: str = "\U00002B1C"


grid = [[1 + i + 3 * j for i in range(3)] for j in range(3)]
grid_size: int = 3
def game_board(grid) -> None:
    """Make a grid."""
    row_counter: int = 0
    column_counter: int = 0
    while row_counter < grid_size:
        emoji_row: str = ""
        column_counter: int = 0
        while column_counter < grid_size:
              if grid[row_counter][column_counter] == 'X':
                  emoji_row += XGUESS
              elif grid[row_counter][column_counter] == 'O':
                  emoji_row += OGUESS
              else:
                  emoji_row += SQUARE
              column_counter += 1
        print(emoji_row)
        row_counter += 1
    
    
def turn(XO):
    row:  int = int(input("Enter the row: "))
    col: int = int(input("Enter the column: "))
    while grid[row - 1][col - 1] == 'X' or grid[row - 1][col - 1] =='O':
        print("Sorry, that spot is taken. Try again.")
        row:  int = int(input("Enter the row: "))
        col: int = int(input("Enter the column: "))
    grid[row - 1][col - 1] = XO
    game_board(grid)

    
def check_win():
    if grid[0][0] == grid[0][1] == grid[0][2]:
        return True
    if grid[1][0] == grid[1][1] == grid[1][2]:
        return True
    if grid[2][0] == grid[2][1] == grid[2][2]:
        return True
    if grid[0][0] == grid[1][0] == grid[2][0]:
        return True
    if grid[0][1] == grid[1][1] == grid[2][1]:
        return True
    if grid[0][2] == grid[1][2] == grid[2][2]:
        return True
    if grid[0][0] == grid[1][1] == grid[2][2]:
        return True
    if grid[2][0] == grid[1][1] == grid[0][2]:
        return True
    return False


def main():
    p1_turn = 1
    p2_turn = 1
    p1_win = False
    p2_win = False
    game_board(grid)
    while p1_win == False and p2_win == False:
        print(f"Turn { p1_turn } of Player 1. Enter 'X' or 'O': ")
        turn('X')
        p1_win = check_win()
        if p1_win:
            print("Player 1 wins!")
            break
        p1_turn += 1
        if p1_turn == 6:
            break
        print(f"Turn { p2_turn } of Player 2. Enter 'X' or 'O': ")
        turn('O')
        p2_win = check_win()
        p2_turn += 1
        if p2_win:
            print("Player 2 wins!")
            break
    
    if p1_win == False and p2_win == False:
        print("The game ended in a draw.")


if __name__ == "__main__":
   main()