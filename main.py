import streamlit as st

# Function to check for a win
def check_win(board):
    # Check rows, columns, and diagonals for a win
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != "":
            return True
        if board[0][i] == board[1][i] == board[2][i] != "":
            return True
    if board[0][0] == board[1][1] == board[2][2] != "":
        return True
    if board[0][2] == board[1][1] == board[2][0] != "":
        return True
    return False

# Function to check for a draw
def check_draw(board):
    for row in board:
        for cell in row:
            if cell == "":
                return False
    return True

# Function to display the game board
def display_board(board):
    for row in board:
        st.write("|".join(row))
        st.write("-----")

# Main function to run the game
def main():
    st.title("Tic-Tac-Toe Game")
    st.write("Player 1: X")
    st.write("Player 2: O")

    # Initialize the game board
    board = [["", "", ""], ["", "", ""], ["", "", ""]]
    player = 1

    # Display the initial game board
    display_board(board)

    # Main game loop
    while True:
        # Get player move
        if st.button("Make a move"):
            row = st.slider("Select row:", 0, 2)
            col = st.slider("Select column:", 0, 2)
            if board[row][col] == "":
                if player == 1:
                    board[row][col] = "X"
                    player = 2
                else:
                    board[row][col] = "O"
                    player = 1
            else:
                st.write("Invalid move! Please select an empty cell.")
                continue

            # Display updated game board
            display_board(board)

            # Check for win or draw
            if check_win(board):
                st.write(f"Player {player} wins!")
                break
            elif check_draw(board):
                st.write("It's a draw!")
                break

if __name__ == "__main__":
    main()
