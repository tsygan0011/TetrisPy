

# import
import tkinter as tk
import time
import random


# class
class tetris:

    def __init__(self, game):
        self.title()
        game.bind('<KeyPress>', lambda e: self.key_detect(e))
        self.gridframe()
        self.random_block()

    def title(self):
        title_frame = tk.Frame()
        title_frame.pack(side=tk.TOP)

        title = "TETRIS"
        title_color_list = ["red", "orange", "yellow", "green", "cyan", "purple"]
        count = 0

        for char in title:
            color = title_color_list[count]
            title_LBL = tk.Label(title_frame, text=char, font=("Arial", 70, "bold"), fg=color, anchor="n")
            title_LBL.pack(side=tk.LEFT)
            count += 1

    def gridframe(self):
        board_width = 406
        board_height = 808
        square = 4
        global check_list
        check_list = []
        check_list_nested = []

        global check_list_checked
        check_list_checked = []
        check_list_checked_nested = []

        gameboard_frame = tk.Frame(game, name="game_board", bg="gray", width=board_width, height=board_height)
        gameboard_frame.pack(side=tk.TOP, padx=20, pady=20)

        for y in range(20):
            for x in range(10):
                check_list_checked_nested.append("")
                check_list_nested.append(str(x) + "," + str(y))
                shape = tk.Label(gameboard_frame, text=str(x) + "," + str(y),
                                 name="label" + str(x) + "," + str(y),
                                 width=square, height=int(square / 2), bg="white")
                shape.place(x=6 + (40 * x), y=6 + (40 * y))
            check_list.append(check_list_nested)
            check_list_checked.append(check_list_checked_nested)
            check_list_nested = []
            check_list_checked_nested = []

    def random_block(self):
        block = [["3,-1", "4,-1", "5,-1", "6,-1", "cyan"], ["4,-1", "4,-2", "4,-3", "5,-1", "orange"],
                 ["4,-1", "5,-1", "5,-2", "5,-3", "blue"], ["4,-1", "5,-1", "4,-2", "5,-2", "yellow"],
                 ["5,-1", "5,-2", "4,-2", "4,-3", "green"], ["5,-1", "5,-2", "5,-3", "4,-2", "purple"],
                 ["4,-1", "4,-2", "5,-2", "5,-3", "red"]]

        global random_block
        random_block = block[random.randint(0, 6)]
        self.time_move_block()

    def time_move_block(self):
        flag = True

        if flag:
            for r in random_block:
                if r.count(",") == 1:
                    position = r.split(",")
                    posX = int(position[0])
                    posY = int(position[1])

                    random_block[random_block.index(r)] = str(posX) + "," + str(posY + 1)

                    try:
                        for x in range(3):
                            if posY >= -1 and posX >= -1 and posY <= 19 and posX <= 9:
                                if (game.nametowidget(".game_board.label" + check_list[posY + 1][posX]))[
                                    "bg"] != "white":
                                    flag = False
                                    raise Exception("Sorry")

                        if flag:
                            if posY >= -1 and posX >= -1 and posY <= 19 and posX <= 9:
                                if (game.nametowidget(".game_board.label" + check_list[posY + 1][posX]))["bg"] == "white":
                                    if posY >= 0:
                                        label = game.nametowidget(".game_board.label" + check_list[posY][posX])
                                        label.config(bg="white")

                                    label = game.nametowidget(".game_board.label" + check_list[posY + 1][posX])
                                    label.config(bg=random_block[len(random_block) - 1])
                                # else:
                                #     for i in range(4):
                                #         posY = (random_block[abs(3-i)].split(","))[1]
                                #         posX = (random_block[abs(3-i)].split(","))[0]
                                        # print(random_block)
                                        # print(posY >= 0)
                                        # print(posX)
                                        # if posY >= 0:
                                        #     label = game.nametowidget(".game_board.label" + random_block[abs(3-i)])
                                        #     label.config(bg="white")
                                        #
                                        # label = game.nametowidget(".game_board.label" + check_list[int(posY)][int(posX)])
                                        # label.config(bg=random_block[len(random_block) - 1])

                    except:
                        flag = False
                        break

        # self.random_block()
        if flag:
            game.after(100, self.time_move_block)
        else:
            self.random_block()

    def key_detect(self, event):
        if event.keysym == "Up" or event.keysym == "w":
            print("up")
            # ROTATE
        elif event.keysym == "Down" or event.keysym == "s":
            print("down")

        elif event.keysym == "Left" or event.keysym == "a":
            print("left")
        elif event.keysym == "Right" or event.keysym == "d":
            print("right")


# function
def main():
    global game
    game = tk.Tk()
    tetris(game)
    tk.mainloop()


# test
def test():
    return


if __name__ == '__main__':
    main()
