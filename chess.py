emptyrow = [".", ".", ".", ".", ".", ".", ".", "."]
Pawnrow = ["P","P","P","P","P","P","P","P"]
pawnrow = ["p","p","p","p","p","p","p","p"]
Mainrow = ["R", "N", "B", "Q", "K", "B", "N", "R"]
mainrow = ["r", "n", "b", "q", "k", "b", "n", "r"]
board = [mainrow,pawnrow,emptyrow,emptyrow,emptyrow,emptyrow,pawnrow,mainrow]

for i in board:
    print("".join(i))
