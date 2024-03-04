

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
        global  block_list
        block_list = []
        block_list_nested = []

        gameboard_frame = tk.Frame(game, name="game_board", bg="gray", width=board_width, height=board_height)
        gameboard_frame.pack(side=tk.TOP, padx=20, pady=20)

        for y in range(20):
            for x in range(10):
                check_list_nested.append(str(6 + (40 * x)) + "," + str(6 + (40 * y)))
                block_list_nested.append("")
                shape = tk.Label(gameboard_frame, text=str(6 + (40 * x)) + "," + str(6 + (40 * y)),
                                 name="label" + str(6 + (40 * x)) + "," + str(6 + (40 * y)),
                                 width=square, height=int(square / 2), bg="white")
                shape.place(x=6 + (40 * x), y=6 + (40 * y))
            check_list.append(check_list_nested)
            block_list.append(block_list_nested)
            check_list_nested = []
            block_list_nested = []
        print(check_list)
    def random_block(self):
        block = [["3,-1", "4,-1", "5,-1", "6,-1", "cyan"], ["4,-1", "4,-2", "4,-3", "5,-1", "orange"],
                 ["4,-1", "5,-1", "5,-2", "5,-3", "blue"], ["4,-1", "5,-1", "4,-2", "5,-2", "yellow"],
                 ["5,-1", "5,-2", "4,-2", "4,-3", "green"], ["5,-1", "5,-2", "5,-3", "4,-2", "purple"],
                 ["4,-1", "4,-2", "5,-2", "5,-3", "red"]]

        global random_block
        random_block = block[random.randint(0, 6)]
        self.time_move_block()

    def bitch(self):
        self.time_flag = False
    def unBitch(self):
        self.time_flag = True

    def collided(self):
        has_collided = False
       # print("this is start of collision check")
        for i in random_block:
            try:
                position = i.split(",")

                for block in block_list:
                    for rows in block:
                        #print("check " + rows + " against " + check_list[int(position[1]) + 1][int(position[0])])
                        if rows == check_list[int(position[1]) + 1][int(position[0])] or \
                                rows == check_list[int(position[1])][int(position[0]) + 1]:
                            has_collided = True
                            print("collided")
                            return has_collided
            except:
                #print(".")
                break

        #print("this is end of collision check")
        return has_collided


    def time_move_block(self):
        # self.check_for_collision()
        if random_block[0].count("15") == 1:
            self.bitch()

        for i in random_block[0:-1]:
            try:
                position = i.split(",")

                if self.time_flag:

                    # for a in block_list:
                    #     for b in a:
                    #         if check_list[int(position[1]) + 1][int(position[0]) + 1] == b:
                    #             count += 1
                    #
                    #             print("HELOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO")
                    #             self.bitch()
                    #             collided = True
                    if self.collided():
                        #print("GET OUT GET OUT GET OUT")
                        self.bitch()

                    else:
                        #print("allow it to drop")
                        # Allow it to drop downwards
                        random_block[random_block.index(i)] = position[0] + "," + str(int(position[1]) + 1)
                        # print("first run: " + str(position[0]) + " , " + str(int(position[1]) +1))

                        if int(position[1]) == 0:

                            label = game.nametowidget(".game_board.label" + check_list[int(position[1])][int(position[0])])
                            label.config(bg="white")

                            label = game.nametowidget(".game_board.label" + check_list[int(position[1])][int(position[0])])
                            label.config(bg=random_block[len(random_block) - 1])
                        elif int(position[1]) >= 1:
                            label = game.nametowidget(
                                ".game_board.label" + check_list[int(position[1]) - 1][int(position[0])])
                            label.config(bg="white")

                            label = game.nametowidget(".game_board.label" + check_list[int(position[1])][int(position[0])])
                            label.config(bg=random_block[len(random_block) - 1])

                else:
                    print("looping count?")
                    new_list = check_list[int(position[1])][int(position[0])].split()
                    block_list.append(new_list)
                    for x in new_list:
                        print("i am trying: " + x)
                    # block_list[int(position[1])][int(position[0])] = check_list[int(position[1])][int(position[0])]
                    # print("nani: " + block_list)
                    self.bitch()


                    #print(check_list[int(position[1])][int(position[0])])


                    # else:
                    #     check_list_checked[int(position[1])-1][int(position[0])] = 1
            except:
                print("")



        if self.time_flag:
            game.after(100, self.time_move_block)
        else:
            # print(
            #     "=============================================================================================================")
            # for x in block_list:
            #     print(x)

            self.unBitch()
            self.random_block()

    def key_detect(self, event):
        if event.keysym == "Up" or event.keysym == "w":
            print("up")
            self.bitch()
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
