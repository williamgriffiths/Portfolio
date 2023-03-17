import tkinter as tk

# Sudoku solver using backtracking
def solve_sudoku(board):
    empty_cell = find_empty_cell(board)
    if not empty_cell:
        return True

    row, col = empty_cell

    for num in range(1, 10):
        if is_valid(board, num, (row, col)):
            board[row][col] = num

            if solve_sudoku(board):
                return True

            board[row][col] = 0

    return False

def find_empty_cell(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return (i, j)
    return None

def is_valid(board, num, pos):
    row, col = pos

    # Check row
    for i in range(9):
        if board[row][i] == num and i != col:
            return False

    # Check column
    for i in range(9):
        if board[i][col] == num and i != row:
            return False

    # Check 3x3 subgrid
    subgrid_row = (row // 3) * 3
    subgrid_col = (col // 3) * 3
    for i in range(3):
        for j in range(3):
            if board[subgrid_row + i][subgrid_col + j] == num and (i, j) != (row, col):
                return False

    return True

# GUI
def on_key(event, entry, row, col):
    key = event.char
    if key.isdigit() and 0 < int(key) <= 9:
        board[row][col] = int(key)
        entry.delete(0, tk.END)
        entry.insert(0, key)
    else:
        entry.delete(0, tk.END)

def solve_button_click():
    solve_sudoku(board)
    for row in range(9):
        for col in range(9):
            entries[row][col].delete(0, tk.END)
            entries[row][col].insert(0, board[row][col])

root = tk.Tk()
root.title("Sudoku Solver")

board = [[0 for _ in range(9)] for _ in range(9)]
entries = [[None for _ in range(9)] for _ in range(9)]

for row in range(9):
    for col in range(9):
        entry = tk.Entry(root, width=3, font=('Arial', 16))
        entry.grid(row=row, column=col, padx=(1, 1) if col % 3 != 2 else (1, 4),
                   pady=(1, 1) if row % 3 != 2 else (1, 4))
        entry.bind('<KeyRelease>', lambda event, e=entry, r=row, c=col: on_key(event, e, r, c))
        entries[row][col] = entry

solve_button = tk.Button(root, text='Solve', command=solve_button_click)
solve_button.grid(row=9, column=0, columnspan=9, pady=(10, 1))

root.mainloop()