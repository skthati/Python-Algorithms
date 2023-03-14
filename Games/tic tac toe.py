import random
import sys

start_game = True
play_again = False
player_turn = True
computer_win = []
player_win = []
game_win = False
print("Welcome to tik tok toe Game!")
win_lst = [[(0, 0), (0, 1), (0, 2)], [(1, 0), (1, 1), (1, 2)], [(2, 0), (2, 1), (2, 2)],
           [(0, 0), (1, 0), (2, 0)], [(0, 1), (1, 1), (2, 1)], [(0, 2), (1, 2), (2, 2)],
           [(0, 0), (1, 1), (2, 2)], [(2, 0), (1, 1), (0, 2)]]


def check_winner():
    # print(f"Player chances: {len(player_win)} and Computer chances: {len(computer_win)}")
    if len(player_win) < 3 and len(computer_win) < 3:
        # print("\033[7A       \033[7A")
        # print(f"{row1}\n{row2}\n{row3}")
        print("Not enough data to check winner")

    else:
        print("Checking winner!")
        for item in win_lst:
            p_lst = []
            c_lst = []
            for i in player_win:
                if i in item:
                    p_lst.append(i)
            # p_lst = [i for i in player_win if i in item]

            if len(p_lst) == 3:
                print("Player wins!")
                exit()

            for j in computer_win:
                if j in item:
                    c_lst.append(j)

            if len(c_lst) == 3:
                print("Computer wins!")
                exit()
        print("No winner yet.")
            # for i in item:
            #     if i in p_lst:
            #         print("Player wins!")
            #         exit()

            # p_lst = []
            # c_lst = []
            # for i in player_win:
            #     if i in item:
            #         p_lst.append(i)
            #
            # print(p_lst)
            #
            # if p_lst == item:
            #     print("Player wins")
            #     exit()
            # else:
            #     p_lst = []
            #
            # for i in computer_win:
            #     if i in item:
            #         c_lst.append(i)
            #
            # print(c_lst)
            #
            # if c_lst == item:
            #     print("Computer wins")
            #     exit()
            # else:
            #     c_lst = []
            # player_win_lst = [i for i in player_win if i in item]
            # computer_win_lst = [i for i in computer_win if i in item]
            # print(f"computer: {computer_win_lst}, computer win: {computer_win}, item: {item}")
            # print(f"player: {player_win_lst}, player win: {player_win}, item: {item}")
            # if player_win_lst == item:
            #     print("Player wins!")
            #     exit()
            # elif computer_win_lst == item:
            #     print("Computer wins!")
            #     exit()
            # else:
            #     computer_win_lst = []
            #     player_win_lst = []

        # print(player_win_lst)
        # print(computer_win_lst)

        # for i in win_lst:
        #     print(f"Check with {i}, Player: {player_win_lst}, Computer: {computer_win_lst}")
        #     if i == player_win_lst:
        #         print("Player wins!")
        #         exit()
        #     elif i == computer_win_lst:
        #         print("Computer wins!")
        #         exit()


def random_num():
    return random.randint(0, 2)


def computer_game():
    a = random_num()
    b = random_num()
    loop = True
    while loop:
        # print("Computer turn!")
        pos = map1[a][b]
        # print(pos)
        if pos == "X" or pos == "O":
            # if pos == "⬜️️":
            a = random_num()
            b = random_num()
        else:
            map1[a][b] = "O"
            computer_win.append((a, b))
            loop = False
            print(f"{row1}\n{row2}\n{row3}")
            check_winner()


def player_game():
    a, b = input("Type your choice: ").split()
    a = int(a)
    b = int(b)
    map1[a][b] = "X"
    player_win.append((a, b))
    print(f"{row1}\n{row2}\n{row3}")
    check_winner()


while start_game:
    row1 = ["⬜️", "️⬜️", "️⬜️"]
    row2 = ["⬜️", "⬜️", "️⬜️"]
    row3 = ["⬜️️", "⬜️️", "⬜️️"]
    map1 = [row1, row2, row3]
    print(f"{row1}\n{row2}\n{row3}")

    player_turn_input = input("Press anykey to start the game or 'c' for computer to start the game: ").lower()
    if player_turn_input == "c":
        while not game_win:
            computer_game()
            player_game()
    else:
        while not game_win:
            player_game()
            computer_game()
