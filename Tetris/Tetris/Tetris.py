

# import
import tkinter as tk
import time
import random


# class
class tetris:

    time_flag = True

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

        gameboard_frame = tk.Frame(game, name="game_board", bg="gray", width=board_width, height=board_height)
        gameboard_frame.pack(side=tk.TOP, padx=20, pady=20)

        for y in range(20):
            for x in range(10):
                check_list_nested.append(str(6 + (40 * x)) + "," + str(6 + (40 * y)))
                shape = tk.Label(gameboard_frame, name="label" + str(6 + (40 * x)) + "," + str(6 + (40 * y)),
                                 width=square, height=int(square / 2), bg="white")
                shape.place(x=6 + (40 * x), y=6 + (40 * y))
            check_list.append(check_list_nested)
            check_list_nested = []

    def random_block(self):
        block = [["3,-1", "4,-1", "5,-1", "6,-1", "cyan"], ["4,-1", "4,-2", "4,-3", "5,-1", "orange"],
                 ["4,-1", "5,-1", "5,-2", "5,-3", "blue"], ["4,-1", "5,-1", "4,-2", "5,-2", "yellow"],
                 ["5,-1", "5,-2", "4,-2", "4,-3", "green"], ["5,-1", "5,-2", "5,-3", "4,-2", "purple"],
                 ["4,-1", "4,-2", "5,-2", "5,-3", "red"]]

        global random_block
        random_block = block[random.randint(0, 6)]
        self.time_move_block()

    def time_move_block(self):
        if random_block[0].count("20") == 1:
            self.time_flag = False

        for i in random_block:
            try:
                position = i.split(",")

                if self.time_flag:
                    random_block[random_block.index(i)] = position[0] + "," + str(int(position[1])+1)

                    if int(position[1]) == 0:

                        label = game.nametowidget(".game_board.label" + check_list[int(position[1])][int(position[0])])
                        label.config(bg="white")

                        label = game.nametowidget(".game_board.label" + check_list[int(position[1])][int(position[0])])
                        label.config(bg=random_block[len(random_block)-1])
                    elif int(position[1]) >= 1:
                        label = game.nametowidget(".game_board.label" + check_list[int(position[1])-1][int(position[0])])
                        label.config(bg="white")

                        label = game.nametowidget(".game_board.label" + check_list[int(position[1])][int(position[0])])
                        label.config(bg=random_block[len(random_block) - 1])
                    # else:
                    #     check_list_checked[int(position[1])-1][int(position[0])] = 1
            except:
                print("error")
        if self.time_flag:
            game.after(100, self.time_move_block)
        else:
            self.time_flag = True
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
    return


# test
def test():
    return


if __name__ == '__main__':
    main()
