board_plate = {'tl':' ', 'tm':' ', 'tr':' ',
               'ml':' ', 'mm':' ', 'mr':' ',
               'll':' ', 'lm':' ', 'lr':' '}
player_turn = 'o'
def board_view(tl,tm,tr,ml,mm,mr,ll,lm,lr):
    print("┌─────┬─────┬─────┐")
    print("│  ", tl, "  │  ", tm, "  │  ", tr, "  │", sep='')
    print("├─────┼─────┼─────┤")
    print("│  ", ml, "  │  ", mm, "  │  ", mr, "  │", sep='')
    print("├─────┼─────┼─────┤")
    print("│  ", ll, "  │  ", lm, "  │  ", lr, "  │", sep='')
    print("└─────┴─────┴─────┘")

# board_view(tl=board_plate['tl'], tm=board_plate['tm'], tr=board_plate['tr'],
#           ml=board_plate['ml'], mm=board_plate['mm'], mr=board_plate['mr'],
#           ll=board_plate['ll'], lm=board_plate['lm'], lr=board_plate['lr'])
def welcome_game():
    for item in board_plate:
        board_plate[item] = ' '
    print("Welcome to Tic Tac Toe Game!!")
    print("Please remember this number and location")
    board_view('1', '2', '3', '4', '5', '6', '7', '8', '9')
    print("Player one is x and player two is o")
    if player_turn == 'o':
        print("player one start game")
    elif player_turn == 'x':
        print("Player two start game")
    start_game()
def start_game():
    global player_turn
    game_check()
    if player_turn == 'o':
        player_turn = 'x'
    else:
        player_turn = 'o'
    play_now(player_turn)
def play_now(xoro):
    sel_num = int(input("Enter your choice: "))
    if sel_num == 1 and board_plate['tl'] == ' ':
        board_plate['tl'] = xoro
    elif sel_num == 2 and board_plate['tm'] == ' ':
        board_plate['tm'] = xoro
    elif sel_num == 3 and board_plate['tr'] == ' ':
        board_plate['tr'] = xoro
    elif sel_num == 4 and board_plate['ml'] == ' ':
        board_plate['ml'] = xoro
    elif sel_num == 5 and board_plate['mm'] == ' ':
        board_plate['mm'] = xoro
    elif sel_num == 6 and board_plate['mr'] == ' ':
        board_plate['mr'] = xoro
    elif sel_num == 7 and board_plate['ll'] == ' ':
        board_plate['ll'] = xoro
    elif sel_num == 8 and board_plate['lm'] == ' ':
        board_plate['lm'] = xoro
    elif sel_num == 9 and board_plate['lr'] == ' ':
        board_plate['lr'] = xoro
    else:
        print("Wrong choice!!!")
        play_now(player_turn)

    board_view(tl=board_plate['tl'], tm=board_plate['tm'], tr=board_plate['tr'],
               ml=board_plate['ml'], mm=board_plate['mm'], mr=board_plate['mr'],
               ll=board_plate['ll'], lm=board_plate['lm'], lr=board_plate['lr'])
    start_game()
def game_end():
    check = 0
    for item in board_plate:
        if board_plate[item] == ' ':
            check += 1
    if check == 0:
        return True
    elif check != 0:
        return False
def game_check():
    # print("Check for win")
    if board_plate['tm'] == board_plate['mm'] and board_plate['tm'] == board_plate['lm'] and board_plate['tm'] != ' ':
        who_win(board_plate['tm'])
    elif board_plate['ml'] == board_plate['mm'] and board_plate['ml'] == board_plate['mr'] and board_plate['ml'] != ' ':
        who_win(board_plate['ml'])
    elif board_plate['tl'] == board_plate['ml'] and board_plate['tl'] == board_plate['ll'] and board_plate['tl'] != ' ':
        who_win(board_plate['tl'])
    elif board_plate['tl'] == board_plate['tm'] and board_plate['tl'] == board_plate['tr'] and board_plate['tl'] != ' ':
        who_win(board_plate['tl'])
    elif board_plate['tl'] == board_plate['mm'] and board_plate['tl'] == board_plate['lr'] and board_plate['tl'] != ' ':
        who_win(board_plate['tl'])
    elif board_plate['tr'] == board_plate['mr'] and board_plate['tr'] == board_plate['lr'] and board_plate['tr'] != ' ':
        who_win(board_plate['tr'])
    elif board_plate['tr'] == board_plate['mm'] and board_plate['tr'] == board_plate['ll'] and board_plate['tr'] != ' ':
        who_win(board_plate['tr'])

    if game_end():
        print("Game is draw!!")
        yorno = input("Play again? (y/n)")
        if yorno == 'y':
            welcome_game()
        else:
            exit()
def who_win(xoro):
    if xoro == 'x':
        print("Player one win!!!")
    elif xoro == 'o':
        print("Player two win!!!!")
    yorno = input("Play again? (y/n)")
    if yorno == 'y':
        welcome_game()
    else:
        exit()
welcome_game()