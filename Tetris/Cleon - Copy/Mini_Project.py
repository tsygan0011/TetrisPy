

# import
import tkinter
import random

# class
class bitlife:
    def __init__(self, game):
        self.start_window()

    def start_window(self):
        # Main Window
        global game_window
        game_window = tkinter.Frame(game)
        game_window.pack(fill="both", expand=True)

        # Sub Window
        start_window_frame = tkinter.Frame(game_window)
        start_window_frame.pack(fill="x", expand=True)

        # Name Text and Name Textbox
        name_LBL = tkinter.Label(start_window_frame, text="Please Enter Your Name...", font=("Arial", 20))
        name_LBL.pack(anchor="center", pady=10)

        name_TB = tkinter.Text(start_window_frame, height=1, width=25, font=("Arial", 20))
        name_TB.pack(anchor="center", pady=10)

        # Randomise Gender
        gender = ['Male', 'Female']
        gender = gender[random.randint(0, 1)]

        gender_LBL = tkinter.Label(start_window_frame, height=1, width=15, text="Gender: " + gender, font=("Arial", 20))
        gender_LBL.pack(anchor="center", pady=10)

        # Confirm Name Button > Goes to Stats page (Display all Statistics)
        submit_BTN = tkinter.Button(start_window_frame, height=1, width=10, text="Confirm", font=("Arial", 20),
                                    command=lambda: self.start_stats_window(start_window_frame, name_TB, gender))
        submit_BTN.pack(anchor="center", pady=10)

    def start_stats_window(self, start_window_frame, name_TB, gender):
        # Retrive Textbox Value while removing the space at the front
        name = (name_TB.get("1.0", "end")).strip()

        # Check if name is only alphabets
        if name.isalpha():
            self.character_generator(name_TB, gender)

            # Remove the frame containing Name TextBox
            start_window_frame.destroy()

            window_frame_top = tkinter.Frame(game_window)
            window_frame_top.pack(fill="x", expand=True)

            window_frame_bottom = tkinter.Frame(game_window)
            window_frame_bottom.pack(fill="x", expand=True, side="bottom")

            # Loop through all character details and print theirs stats
            for i in character_dict.items():

                if i[0] == "name":
                    title_LBL = tkinter.Label(window_frame_top,
                                              text="Hello " + (i[1].__str__()).capitalize() + "!, welcome to SingLife",
                                              font=("Arial", 23, "bold"))
                    title_LBL.pack(anchor="center", pady=10)
                elif i[0] != "karma" and i[0] != "energy" and i[0] != "health" and i[0] != "age":
                    stats_LBL = tkinter.Label(window_frame_top, text=i[0].capitalize() + ": " + i[1].__str__(),
                                              font=("Arial", 20))
                    stats_LBL.pack(anchor="center", pady=10)
                elif i[0] == "age":
                    stats_LBL = tkinter.Label(window_frame_bottom, text=i[0].capitalize() + ": " + i[1].__str__(),
                                              font=("Arial", 20))
                    stats_LBL.pack(anchor="center", pady=10)
                elif i[0] == "karma":
                    bar_stats_frame = tkinter.Frame(window_frame_bottom, bg="gray", width=400)
                    bar_stats_frame.pack(fill="x", padx="10")

                    bar_stats_LBL_text = tkinter.Label(bar_stats_frame, text=i[0].capitalize() + ": " + i[1].__str__(),
                                                       font=("Arial", 20))
                    bar_stats_LBL_text.pack(anchor="w", pady=5, padx=5)

                    bar_stats_LBL_left = tkinter.Label(bar_stats_frame, bg="green", width=int((i[1] / 100) * 70))
                    bar_stats_LBL_left.pack(side="left", pady=5)

                    bar_stats_LBL_right = tkinter.Label(bar_stats_frame, bg="red",
                                                        width=int((abs(i[1] - 100) / 100) * 70))
                    bar_stats_LBL_right.pack(side="right", pady=5)
                else:
                    bar_stats_frame = tkinter.Frame(window_frame_bottom, bg="gray", width=400)
                    bar_stats_frame.pack(fill="x", padx="10")

                    bar_stats_LBL_text = tkinter.Label(bar_stats_frame, text=i[0].capitalize() + ": " + i[1].__str__(),
                                                       font=("Arial", 20))
                    bar_stats_LBL_text.pack(anchor="w", pady=5, padx=5)

                    bar_stats_LBL = tkinter.Label(bar_stats_frame, bg="green", width=int((i[1] / 100) * 70))
                    bar_stats_LBL.pack(anchor="w", pady=5, padx=5)

            # Click to narration
            click_continue = tkinter.Label(game, text="Click anywhere to continue...", font=("Arial", 10))
            click_continue.pack(anchor="s")

            game.bind('<Button-1>', lambda e: self.narration(window_frame_top, click_continue, window_frame_bottom))

    def narration(self, window_frame_top, click_continue, window_frame_bottom):
        window_frame_top.destroy()
        click_continue.destroy()
        game.unbind('<Button-1>')

        narration_frame = tkinter.Frame(game_window)
        narration_frame.pack(fill="x", expand=True)

        narrative_text = "I am born as a " + character_dict[
            "gender"] + " in Singapore. I am the beautiful creation from the sensational event that my parent had that night. My life starts now......\n\nDisclaimer: This whole story line is frictional. "

        narration_frame_LBL = tkinter.Label(narration_frame, bg="gray", justify="center",
                                            text=narrative_text, font=("Arial", 15), wraplengt=500)
        narration_frame_LBL.pack(anchor="center", pady=10)

        # stickman
        canvas = tkinter.Canvas(game_window)
        canvas.create_oval(225, 45, 170, 100, fill="gray")
        canvas.create_text(120, 100, text=character_dict["name"].capitalize())

        x = 197
        y = 175
        stick = canvas.create_line(x, y - 75, x, y)

        diff_x = 25
        stick_leg1 = canvas.create_line(x, y, x - diff_x, y + 50)
        stick_leg2 = canvas.create_line(x, y, x + diff_x, y + 50)

        y = 145
        stick_arm1 = canvas.create_line(x, y, x - 30, y - 20)
        stick_arm2 = canvas.create_line(x, y, x + 30, y - 10)

        canvas.pack(anchor="s", side="bottom")

        # Click to main game
        click_continue = tkinter.Label(window_frame_bottom, text="Click anywhere to continue...", font=("Arial", 10))
        click_continue.pack(anchor="s")

        game.bind('<Button-1>', lambda e: self.main_game_start(narration_frame, click_continue))

    def main_game_start(self, narration_frame, click_continue):
        click_continue.destroy()
        narration_frame.destroy()
        game.unbind('<Button-1>')

        game_frame = tkinter.Frame(game_window)
        game_frame.pack(fill="x", expand=True, anchor="n")

        # menu pop up
        menu_BTN = tkinter.Button(game_frame, text="≡", width=3, font=("Arial", 30, "bold"),
                                  command=lambda: self.menu_popup(game))
        menu_BTN.pack(side="left", anchor="n")

    def character_generator(self, name_TB, gender):
        time_limit = 0
        difficulty = 0

        energy = 100
        money = 0.0
        health = random.randint(50, 100)
        iq = random.randint(20, 150)
        karma = random.randint(1, 100)
        name = (name_TB.get("1.0", "end")).strip()
        age = 0

        global character_dict
        character_dict = {"name": name, "gender": gender, "age": age, "money": "$" + str(money),
                          "iq": iq, "health": health, "energy": energy, "karma": karma}

    def menu_popup(self, game):
        popup = tkinter.Toplevel(game)
        popup.title("Main Menu")
        popup.grab_set()
        popup.geometry("500x700")

        menu_frame = tkinter.Frame(popup)
        menu_frame.pack(fill="both", expand=True)
        menu_list = ['eat', 'sleep', 'dating app', 'marriage', 'work', '4d/toto', 'car', 'house', 'sport',
                     'driving licence', 'stats', 'suicide']

        frame= ""
        for menu_list_item in menu_list:
            if menu_list.index(menu_list_item) % 2 == 0:
                frame = tkinter.Frame(menu_frame)
                frame.pack(fill="both", expand=True)
                menu_list_BTN = tkinter.Button(frame, name=menu_list_item, text=menu_list_item.capitalize(), width=10, font=("Arial", 18))
                menu_list_BTN["command"] = lambda menu_list_BTN=menu_list_BTN: self.menu_sub_popup(popup, menu_list_BTN)
                menu_list_BTN.pack(side="left", fill="both", expand=True)
            else:
                menu_list_BTN = tkinter.Button(frame, name=menu_list_item, text=menu_list_item.capitalize(), width=10, font=("Arial", 18))
                menu_list_BTN["command"] = lambda menu_list_BTN=menu_list_BTN: self.menu_sub_popup(popup, menu_list_BTN)
                menu_list_BTN.pack(side="right", fill="both", expand=True)

    def menu_sub_popup(self, popup, menu_list_BTN):
        menu_sub_popup = tkinter.Toplevel(popup)
        menu_sub_popup.title(menu_list_BTN.cget("text"))
        menu_sub_popup.grab_set()
        menu_sub_popup.geometry("500x700")

    def incident_popup(self, popup, menu_list_BTN):
        print(menu_list_BTN)
        menu_sub_popup = tkinter.Toplevel(popup)
        menu_sub_popup.title(menu_list_BTN)
        menu_sub_popup.grab_set()
        menu_sub_popup.geometry("500x700")


# function
def main():
    global game
    game = tkinter.Tk()
    game.title("SingLife")
    game.geometry("500x700")
    game.resizable(False,False)
    bitlife(game)
    tkinter.mainloop()


# test
def test():
    return


if __name__ == '__main__':
    main()
