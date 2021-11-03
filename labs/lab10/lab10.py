"""
Name: Celine Imani
lab10.py
"""

# creates the list of numbers 1-9
def build():
    return list(range(1, 10))

# creates the method to display the board
def display(board):
    for i in range(3):
        n = i * 3
        print(str(board[n]) + '|' + str(board[n + 1]) + '|' + str(board[n + 2]))
        print(10 * "-")

# fills the spot on the board
# make sure it only allows just x and o
def place(board, pos, piece):
    if piece == "o" or piece == "x":
        board[pos - 1] = piece

#create a boolean method to make sure the spot is legal
def legal_spot(board, pos):
     if pos == board[pos - 1]:
        if pos == "":
            return True
     else:
        return False

# # a boolean method to determine if the game is won
def win_game(board, piece):
     # horizontal
      for i in range(3):
          n = i * 3
          if board[n] != piece:
              continue
          return True
      else:
          return False

      # vertical
      for i in range(3):
          if board[i] != piece:
              continue
      else:
          return False

#      # i + 3
#      # i + 6
#
    if board[0] == piece:
        if board[4]:
            if board[8]:
                return True
     else:
        return False

     if board[2] == piece:
         if board[4] == piece:
             if board[6] == piece:
     return True
     else:
        return False

# a method for playing the game
# method doesn't stop till the game is over
# will print the results until the game is over

def over(board):
    if win_game(board, "x"):
        return True
     elif "o":
         return True
     else:
         for i in range(9):
             if board[i] == itl:
                 return False
             return True

def play():
    display(board)
    while True:
        x = eval("X, where do you want your piece?: ")
        place(board, piece, x)
            win_game(board, x)

        o = eval("O, where do you want your piece: ")
        place(board, piece, o)
            win_game(board, o)

        if win_game(board, x) return True:
            print("x win")

        elif win_game(board, o) return True:
            print("o wins!")

        else:
            print ("There was a tie.")


def main():
    board = build()
    play()

main()
