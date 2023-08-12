import tkinter as tk
import random
from tkinter import messagebox

def initialize_board():
    return [[' ' for _ in range(3)] for _ in range(3)]

def draw_board():
    canvas.delete("all")
    canvas.create_line(0, 100, 300, 100, fill="black")
    canvas.create_line(0, 200, 300, 200, fill="black")
    canvas.create_line(100, 0, 100, 300, fill="black")
    canvas.create_line(200, 0, 200, 300, fill="black")

    for row in range(3):
        for col in range(3):
            cell_value = board[row][col]
            x = col * 100 + 50
            y = row * 100 + 50
            canvas.create_text(x, y, text=cell_value, font=("Helvetica", 48))

def check_win():
    for check_func in [check_win_horizontal, check_win_vertical, check_win_diagonal]:
        winner = check_func()
        if winner != '-':
            return winner
    return '-'

def check_win_horizontal():
    for row in board:
        if row[0] == row[1] == row[2] != ' ':
            return row[0]
    return '-'

def check_win_vertical():
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != ' ':
            return board[0][col]
    return '-'

def check_win_diagonal():
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return board[0][2]
    return '-'

def reset_game():
    global board, player, winner
    board = initialize_board()
    player = 1
    winner = '-'
    draw_board()

def check_draw():
    for row in board:
        if ' ' in row:
            return False
    return True

def on_cell_click(row, col):
    global winner, player
    if board[row][col] == ' ' and winner == '-':
        if player == 1 :
            board[row][col] = 'X' 
            draw_board()
            winner = check_win()
        if winner != '-':
            messagebox.showinfo("Game Over", f"Player {winner} wins!")
            reset_game()
        elif check_draw():
            messagebox.showinfo("Game Over", "It's a draw!")
            reset_game()
        else:
            player *= -1

            if player == -1:  # 'O' player's turn
                messagebox.showinfo("Turn O", "Computer Is Thinking")
                empty_cells = [(r, c) for r in range(3) for c in range(3) if board[r][c] == ' ']
                if empty_cells:
                    random_row, random_col = random.choice(empty_cells)
                    board[random_row][random_col] = 'O'
                    draw_board()
                    winner = check_win()
                    if winner != '-':
                        messagebox.showinfo("Game Over", f"Player {winner} wins!")
                        reset_game()
                    elif check_draw():
                        messagebox.showinfo("Game Over", "It's a draw!")
                        reset_game()
                    
                    messagebox.showinfo("Turn X", "Your Turn..\nTo Move Please Click Box 2 times")

def create_gui():
    messagebox.showinfo("Welcome To Tic Tac Toe", "You are X ... To Move Please Click Box 2 times ")
    global canvas
    canvas = tk.Canvas(root, width=300, height=300)
    canvas.pack()

    draw_board()

    canvas.bind("<Button-1>", lambda event: on_cell_click(event.y // 100, event.x // 100))

root = tk.Tk()
root.title("Tic Tac Toe")

board = initialize_board()
player = 1
winner = '-'

create_gui()

root.mainloop()
