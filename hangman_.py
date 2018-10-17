while wrong < len(stage) - 1:
    print("\n")                      # \nは改行を表す
    msg = "1文字を予想してね"
    char = input(msg)r
    if char in rletters:
        cind = rletters.index(char)
        board[cind] = char
        rletters[cind] = '$'
    else:
        wrong +=1
    ptint(" ".join(board))
    e = wrong + 1
    print("\n".join(stages[0:e]))
    if "_" not in board:
        print("あなたの勝ち！")
        print("_".join(board))
        win = True
        break
        
