import tkinter as tk

class SudokuCell(tk.Frame):
    def __init__(self, master, row, col, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        validate_command = self.register(self.validate_input)
        self.entry = tk.Entry(self, width=2, font=('Arial', 16), justify='center', borderwidth=0,
                              validate='key', validatecommand=(validate_command, '%P'))
        self.entry.pack(padx=1, pady=1)
        self.entry.bind('<KeyRelease>', lambda event, r=row, c=col: on_key(event, r, c))
        self.entry.bind('<Up>', lambda event, r=row, c=col: on_arrow_key(event, r, c))
        self.entry.bind('<Down>', lambda event, r=row, c=col: on_arrow_key(event, r, c))
        self.entry.bind('<Left>', lambda event, r=row, c=col: on_arrow_key(event, r, c))
        self.entry.bind('<Right>', lambda event, r=row, c=col: on_arrow_key(event, r, c))
        entries[row][col] = self.entry

    def validate_input(self, value):
        if not value:
            return True
        if len(value) == 1 and value.isdigit() and 0 < int(value) <= 9:
            return True
        return False


class Timer:
    def __init__(self, root):
        self.root = root
        self.elapsed_time = 0
        self.timer_id = None
        self.timer_label = tk.Label(root, text="Time: 00:00", font=("Arial", 12))
        self.update_timer()

    def update_timer(self):
        self.elapsed_time += 1
        minutes, seconds = divmod(self.elapsed_time, 60)
        self.timer_label.config(text=f"Time: {minutes:02d}:{seconds:02d}")
        self.timer_id = self.root.after(1000, self.update_timer)

    def stop_timer(self):
        self.root.after_cancel(self.timer_id)
        minutes, seconds = divmod(self.elapsed_time, 60)
        self.timer_label.config(text=f"Solved! In {minutes:02d}:{seconds:02d}.")


def on_key(event, row, col):
    if event.keysym in ('Up', 'Down', 'Left', 'Right'):
        return

    key = event.char
    if key.isdigit() and 0 < int(key) <= 9:
        board[row][col] = int(key)
    else:
        entries[row][col].delete(0, tk.END)

    if len(entries[row][col].get()) > 1:
        entries[row][col].delete(1)


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
    solve_sudoku(board)
    for row in range(9):
        for col in range(9):
            entries[row][col].delete(0, tk.END)
            entries[row][col].insert(0, board[row][col])
    timer.stop_timer()


def clear_button_click():
    for row in range(9):
        for col in range(9):
            board[row][col] = 0
            entries[row][col].delete(0, tk.END)


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
solve_button.grid(row=9, column=0, columnspan=4, pady=(10, 1), sticky='ew')

clear_button = tk.Button(root, text='Clear', command=clear_button_click)
clear_button.grid(row=9, column=5, columnspan=4, pady=(10, 1), sticky='ew')

timer = Timer(root)  # Add this line to create the timer object
timer.timer_label.grid(row=10, column=0, columnspan=9, pady=(10, 0))


root.mainloop()