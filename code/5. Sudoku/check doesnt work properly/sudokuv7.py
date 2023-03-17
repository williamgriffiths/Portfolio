import tkinter as tk

class SudokuCell(tk.Frame):
    def __init__(self, master, row, col, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.entry = tk.Entry(self, width=2, font=('Arial', 16), justify='center', borderwidth=0)
        self.entry.pack(padx=1, pady=1)
        self.entry.bind('<KeyRelease>', lambda event, r=row, c=col: on_key(event, r, c))
        self.entry.bind('<Up>', lambda event, r=row, c=col: on_arrow_key(event, r, c))
        self.entry.bind('<Down>', lambda event, r=row, c=col: on_arrow_key(event, r, c))
        self.entry.bind('<Left>', lambda event, r=row, c=col: on_arrow_key(event, r, c))
        self.entry.bind('<Right>', lambda event, r=row, c=col: on_arrow_key(event, r, c))
        entries[row][col] = self.entry


def on_key(event, row, col):
    ch = event.char
    if ch.isdigit():
        number = int(ch) if ch != '0' else None
        entries[row][col].delete(0, tk.END)
        if number is not None:
            entries[row][col].insert(0, str(number))
        board[row][col] = number
        check_error(row, col)
    elif ch == '\x08':  # Backspace key
        entries[row][col].delete(0, tk.END)
        board[row][col] = 0
        check_error(row, col)
    entries[row][col].config(bg='#D3EAF8')


def on_arrow_key(event, row, col):
    direction = event.keysym
    if direction == 'Up':
        row = (row - 1) % 9
    elif direction == 'Down':
        row = (row + 1) % 9
    elif direction == 'Left':
        col = (col - 1) % 9
    elif direction == 'Right':
        col = (col + 1) % 9
    entries[row][col].focus()


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


def find_empty_cell(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return (i, j)
    return None


def solve_button_click():
    reset_cell_colors()
    solve_sudoku(board)
    for row in range(9):
        for col in range(9):
            entries[row][col].delete(0, tk.END)
            entries[row][col].insert(0, board[row][col])
    stop_timer()


def clear_button_click():
    for row in range(9):
        for col in range(9):
            board[row][col] = 0
            entries[row][col].delete(0, tk.END)


def update_timer():
    global elapsed_time
    elapsed_time += 1
    minutes, seconds = divmod(elapsed_time, 60)
    timer_label.config(text=f"Time: {minutes:02d}:{seconds:02d}")
    global timer_id
    timer_id = root.after(1000, update_timer)


def stop_timer():
    global timer_id
    root.after_cancel(timer_id)
    minutes, seconds = divmod(elapsed_time, 60)
    timer_label.config(text=f"Solved! In {minutes:02d}:{seconds:02d}.")


def reset_error_colors(row, col):
    number = board[row][col]
    
    # Reset row colors
    for c in range(9):
        if c != col:
            entries[row][c].config(bg='#D3EAF8')
    
    # Reset column colors
    for r in range(9):
        if r != row:
            entries[r][col].config(bg='#D3EAF8')
    
    # Reset 3x3 box colors
    box_row = row // 3 * 3
    box_col = col // 3 * 3
    for r in range(box_row, box_row + 3):
        for c in range(box_col, box_col + 3):
            if r != row or c != col:
                entries[r][c].config(bg='#D3EAF8')


def check_error(row, col):
    reset_error_colors(row, col)

    number = board[row][col]

    if number == 0:
        return

    # Check row
    if number in board[row][:col] + board[row][col + 1:]:
        entries[row][col].config(bg='#F6B8B8')
        return

    # Check column
    for r in range(9):
        if r != row and board[r][col] == number:
            entries[row][col].config(bg='#F6B8B8')
            return

    # Check 3x3 square
    box_row = row // 3 * 3
    box_col = col // 3 * 3
    for r in range(box_row, box_row + 3):
        for c in range(box_col, box_col + 3):
            if (r != row or c != col) and board[r][c] == number:
                entries[row][col].config(bg='#F6B8B8')
                return

    # No error found
    entries[row][col].config(bg='#D3EAF8')


def check_button_click():
    for row in range(9):
        for col in range(9):
            check_error(row, col)


def reset_cell_colors():
    for row in range(9):
        for col in range(9):
            entries[row][col].config(bg='#D3EAF8')


root = tk.Tk()
root.title("Sudoku Solver")

board = [[0 for _ in range(9)] for _ in range(9)]
entries = [[None for _ in range(9)] for _ in range(9)]

for row in range(9):
    for col in range(9):
        cell = SudokuCell(root, row, col, bd=1, relief=tk.SUNKEN, bg='#D3EAF8')
        cell.grid(row=row, column=col, padx=(0, 0) if col % 3 != 2 else (0, 4),
                  pady=(0, 0) if row % 3 != 2 else (0, 4))

solve_button = tk.Button(root, text='Solve', command=solve_button_click)
solve_button.grid(row=9, column=0, columnspan=3, pady=(10, 1), sticky='ew')

clear_button = tk.Button(root, text='Clear', command=clear_button_click)
clear_button.grid(row=9, column=3, columnspan=3, pady=(10, 1), sticky='ew')

check_button = tk.Button(root, text='Check', command=check_button_click)
check_button.grid(row=9, column=6, columnspan=3, pady=(10, 1), sticky='ew')

# Timer
elapsed_time = 0
timer_id = None
timer_label = tk.Label(root, text="Time: 00:00", font=("Arial", 12))
timer_label.grid(row=10, column=0, columnspan=9, pady=(10, 0))
update_timer()

root.mainloop()