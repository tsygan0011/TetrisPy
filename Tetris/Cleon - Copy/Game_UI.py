

# import
import tkinter
import random
import Player

count = {"eat": 0, "sleep": 0, "marriage": 0, "car": 0}


# class
class game:

    def start_game(self):
        game = tkinter.Tk()
        game.title("SingLife")
        game.geometry("500x700")
        game.resizable(False, False)
        return game

    def start_window(self, game, player):
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

        gender_LBL = tkinter.Label(start_window_frame, height=1, width=15, text="Gender: Male", font=("Arial", 20))
        gender_LBL.pack(anchor="center", pady=10)

        # Confirm Name Button > Goes to Stats page (Display all Statistics)
        submit_BTN = tkinter.Button(start_window_frame, height=1, width=10, text="Confirm", font=("Arial", 20),
                                    command=lambda: self.start_stats_window(start_window_frame, name_TB, game, player))
        submit_BTN.pack(anchor="center", pady=10)

    def start_stats_window(self, start_window_frame, name_TB, game, player):
        # Retrive Textbox Value while removing the space at the front
        name = (name_TB.get("1.0", "end")).strip()

        # Check if name is only alphabets
        if name.isalpha():
            player.set_value('name', name)

            # Remove the frame containing Name TextBox
            start_window_frame.destroy()

            window_frame_top = tkinter.Frame(game_window)
            window_frame_top.pack(fill="x", expand=True)

            window_frame_bottom = tkinter.Frame(game_window)
            window_frame_bottom.pack(fill="x", expand=True, side="bottom")

            # Loop through all character details and print theirs stats
            for i in player.variables:
                player.get_value(i)
                if i == "name":
                    title_LBL = tkinter.Label(window_frame_top,
                                              text="Hello " + (
                                                  player.get_value(
                                                      i).__str__()).capitalize() + "!, welcome to SingLife",
                                              font=("Arial", 23, "bold"))
                    title_LBL.pack(anchor="center", pady=10)
                elif i != "karma" and i != "energy" and i != "health" and i != "age":
                    stats_LBL = tkinter.Label(window_frame_top,
                                              text=i.capitalize() + ": " + player.get_value(i).__str__(),
                                              font=("Arial", 20))
                    stats_LBL.pack(anchor="center", pady=10)
                elif i == "age":
                    stats_LBL = tkinter.Label(window_frame_bottom, name="age",
                                              text=i.capitalize() + ": " + player.get_value(i).__str__(),
                                              font=("Arial", 20))
                    stats_LBL.pack(anchor="center", pady=10)
                elif i == "karma":
                    bar_stats_frame = tkinter.Frame(window_frame_bottom, name="bar_stats_frame", bg="gray", width=400)
                    bar_stats_frame.pack(fill="x", padx="10")

                    bar_stats_LBL_text = tkinter.Label(bar_stats_frame, name=i,
                                                       text=i.capitalize() + ": " + player.get_value(i).__str__(),
                                                       font=("Arial", 20))
                    bar_stats_LBL_text.pack(anchor="w", pady=5, padx=5)

                    bar_stats_LBL_left = tkinter.Label(bar_stats_frame, bg="green", name=i+"bargreen",
                                                       width=int((int(player.get_value(i)) / 100) * 70))
                    bar_stats_LBL_left.pack(side="left", pady=5)

                    bar_stats_LBL_right = tkinter.Label(bar_stats_frame, bg="red", name=i+"barred",
                                                        width=int((abs(int(player.get_value(i)) - 100) / 100) * 70))
                    bar_stats_LBL_right.pack(side="right", pady=5)
                else:
                    bar_stats_frame = tkinter.Frame(window_frame_bottom, name="bar_stats_frame"+i, bg="gray", width=400)
                    bar_stats_frame.pack(fill="x", padx="10")

                    bar_stats_LBL_text = tkinter.Label(bar_stats_frame, name=i,
                                                       text=i.capitalize() + ": " + player.get_value(i).__str__(),
                                                       font=("Arial", 20))
                    bar_stats_LBL_text.pack(anchor="w", pady=5, padx=5)

                    bar_stats_LBL = tkinter.Label(bar_stats_frame, bg="green", name=i+"bar", width=int((int(player.get_value(i)) / 100) * 70))
                    bar_stats_LBL.pack(anchor="w", pady=5, padx=5)

            # Click to narration
            click_continue = tkinter.Label(game, text="Click anywhere to continue...", font=("Arial", 10))
            click_continue.pack(anchor="s")

            game.bind('<Button-1>',
                      lambda e: self.narration(window_frame_top, click_continue, game, window_frame_bottom, player))

    def narration(self, window_frame_top, click_continue, game, window_frame_bottom, player):
        window_frame_top.destroy()
        click_continue.destroy()
        game.unbind('<Button-1>')

        narration_frame = tkinter.Frame(game_window)
        narration_frame.pack(fill="x", expand=True)

        narrative_text = "I am born as a Male in Singapore. I am the beautiful creation from the sensational event that my parent had that night. My life starts now......\n\nDisclaimer: This whole story line is frictional. "

        narration_frame_LBL = tkinter.Label(narration_frame, bg="gray", justify="center",
                                            text=narrative_text, font=("Arial", 15), wraplengt=500)
        narration_frame_LBL.pack(anchor="center", pady=10)

        # stickman
        canvas = tkinter.Canvas(game_window)
        canvas.create_oval(225, 45, 170, 100, fill="gray")
        canvas.create_text(120, 100, text=player.get_value("name").capitalize())

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

        game.bind('<Button-1>', lambda e: self.main_game_start(narration_frame, click_continue, game, player, window_frame_bottom))

    def main_game_start(self, narration_frame, click_continue, game, player, window_frame_bottom):
        click_continue.destroy()
        narration_frame.destroy()
        game.unbind('<Button-1>')

        game_frame = tkinter.Frame(game_window)
        game_frame.pack(fill="x", expand=True, anchor="n")

        # menu pop up
        menu_BTN = tkinter.Button(game_frame, text="≡", width=3, font=("Arial", 30, "bold"),
                                  command=lambda: self.menu_popup(game, player, window_frame_bottom))
        menu_BTN.pack(side="left", anchor="n")

        choices_BTN = tkinter.Button(game_frame, text="Choices", width=10, font=("Arial", 20, "bold"),
                                  command=lambda: self.incident_popup(player, window_frame_bottom, game))
        choices_BTN.pack(side="right", anchor="n")

        year_BTN = tkinter.Button(game_frame, text="Years Later...", width=10, font=("Arial", 20, "bold"),
                                  command=lambda: self.next_year(player, window_frame_bottom))
        year_BTN.pack(side="right", anchor="n")

    def next_year(self, player, window_frame_bottom):
        player.set_value("age", 3)
        count["eat"] = 0
        window_frame_bottom.nametowidget("age")["text"] = "Age : " + player.get_value("age")

    def refresh_statsbar(self, window_frame_bottom, player):
        frame = window_frame_bottom.nametowidget("bar_stats_frame")
        framehealth = window_frame_bottom.nametowidget("bar_stats_framehealth")
        frameenergy = window_frame_bottom.nametowidget("bar_stats_frameenergy")

        frame.nametowidget("karmabargreen")["width"] = int((int(player.get_value("karma")) / 100) * 70)
        frame.nametowidget("karmabarred")["width"] = int((abs(int(player.get_value("karma")) - 100) / 100) * 70)
        frameenergy.nametowidget("energybar")["width"] = int((int(player.get_value("energy")) / 100) * 70)
        framehealth.nametowidget("healthbar")["width"] = int((int(player.get_value("health")) / 100) * 70)

        framehealth.nametowidget("health")["text"] = "Health: " + player.get_value("health")
        frameenergy.nametowidget("energy")["text"] = "Energy: " + player.get_value("energy")
        frame.nametowidget("karma")["text"] = "karma: " + player.get_value("karma")

    def menu_popup(self, game, player, window_frame_bottom):
        popup = tkinter.Toplevel(game)
        popup.title("Main Menu")
        popup.grab_set()
        popup.geometry("500x700")

        menu_frame = tkinter.Frame(popup)
        menu_frame.pack(fill="both", expand=True)
        menu_list = ['eat', 'sleep', 'marriage', 'work', 'car', 'house', 'sport', 'stats', 'suicide']

        frame = ""
        for menu_list_item in menu_list:
            if menu_list.index(menu_list_item) % 2 == 0:
                frame = tkinter.Frame(menu_frame)
                frame.pack(fill="both", expand=True)
                menu_list_BTN = tkinter.Button(frame, name=menu_list_item, text=menu_list_item.capitalize(), width=10,
                                               font=("Arial", 18))
                menu_list_BTN["command"] = lambda menu_list_BTN=menu_list_BTN: self.menu_sub_popup(popup, menu_list_BTN,
                                                                                                   player, window_frame_bottom)
                menu_list_BTN.pack(side="left", fill="both", expand=True)
            else:
                menu_list_BTN = tkinter.Button(frame, name=menu_list_item, text=menu_list_item.capitalize(), width=10,
                                               font=("Arial", 18))
                menu_list_BTN["command"] = lambda menu_list_BTN=menu_list_BTN: self.menu_sub_popup(popup, menu_list_BTN,
                                                                                                   player, window_frame_bottom)
                menu_list_BTN.pack(side="right", fill="both", expand=True)

    def menu_sub_popup(self, popup, menu_list_BTN, player, window_frame_bottom):
        age = int(player.get_value("age"))
        menu_list_text = menu_list_BTN.cget("text")

        menu_sub_popup = tkinter.Toplevel(popup)
        menu_sub_popup.title(menu_list_BTN.cget("text"))
        menu_sub_popup.grab_set()
        menu_sub_popup.geometry("500x700")

        menu_sub_frame = tkinter.Frame(menu_sub_popup)
        menu_sub_frame.pack(fill="both", expand=True)

        if "Eat" == menu_list_BTN.cget("text"):
            # 10 time, 11>5$,15>10,20>50
            flag = 0
            count["eat"] += 1
            if count["eat"] < 11:
                if age > 11 and int(player.get_value("money")) >= 5:
                    player.set_value('money', -5)
                    flag = 1
                elif age > 15 and int(player.get_value("money")) >= 15:
                    player.set_value('money', -15)
                    flag = 1
                elif age > 20 and int(player.get_value("money")) >= 50:
                    player.set_value('money', -50)
                    flag = 1
                elif age < 11:
                    flag = 1

            if flag == 1:
                player.set_value('energy', 3)

                textlabel_energy = tkinter.Label(menu_sub_frame, text="Energy: +3", font=('Arial', 20))
                textlabel_energy.pack(anchor="n", pady=150, side="top")

                textlabel_money = tkinter.Label(menu_sub_frame,
                                                text="Money: - $" + str(float(player.get_value("money"))),
                                                font=('Arial', 20))
                textlabel_money.pack(anchor="s", pady=10)
            else:
                if count["eat"] > 10:
                    textlabel_energy = tkinter.Label(menu_sub_frame, text="You are FULL and you can not eat anymore", font=('Arial', 10))
                    textlabel_energy.pack(anchor="n", pady=150, side="top", fill="x")
                else:
                    textlabel_energy = tkinter.Label(menu_sub_frame, text="You are BROKE and you can not affort to eat anymore",
                                                     font=('Arial', 10))
                    textlabel_energy.pack(anchor="n", pady=150, side="top")


        elif "Sleep" == menu_list_BTN.cget("text"):
            # sleep 3 time per years

            flag = 0
            count["sleep"] += 1
            if count["sleep"] < 4:
                flag = 1

            if flag == 1:
                player.set_value('energy', 10)

                textlabel_energy = tkinter.Label(menu_sub_frame, text="Energy: +10", font=('Arial', 20))
                textlabel_energy.pack(anchor="n", pady=150, side="top")
            else:
                if count["sleep"] > 10:
                    textlabel_energy = tkinter.Label(menu_sub_frame, text="You slept too much",
                                                     font=('Arial', 10))
                    textlabel_energy.pack(anchor="n", pady=150, side="top", fill="x")

        elif "Marriage" == menu_list_BTN.cget("text"):
            # after 21
            flag = 0
            if int(player.get_value("age")) >= 21:
                count["marriage"] += 1
                if count["marriage"] == 1:
                    flag = 1

                if flag == 1:
                    textlabel_energy = tkinter.Label(menu_sub_frame, text="Congratulations!!!!", font=('Arial', 30))
                    textlabel_energy.pack(anchor="n", pady=150, side="top")

                    textlabel_energy = tkinter.Label(menu_sub_frame, text="Married to Amanda", font=('Arial', 20))
                    textlabel_energy.pack(anchor="n", pady=150, side="top")
                else:
                    textlabel_energy = tkinter.Label(menu_sub_frame, text="Status: Married", font=('Arial', 20))
                    textlabel_energy.pack(anchor="n", pady=100, side="top")

                    textlabel_energy = tkinter.Label(menu_sub_frame, text="Wife: Amanda", font=('Arial', 20))
                    textlabel_energy.pack(anchor="n", pady=100, side="top")

                    textlabel_energy = tkinter.Label(menu_sub_frame, text="Kids: Tom and Jerry", font=('Arial', 20))
                    textlabel_energy.pack(anchor="n", pady=100, side="top")
            else:
                textlabel_energy = tkinter.Label(menu_sub_frame, text="You are UNDERAGE!!! too young for Marriage", font=('Arial', 15))
                textlabel_energy.pack(anchor="n", pady=150, side="top")

        elif "Work" == menu_list_BTN.cget("text"):
            # C4X
                textlabel_energy = tkinter.Label(menu_sub_frame, text="You Signed on as a Competent and strong minded cyber expert in the SAF!!!!", font=('Arial', 30), wraplengt=500)
                textlabel_energy.pack(anchor="n", pady=150, side="top")

                textlabel_energy = tkinter.Label(menu_sub_frame, text="Married to Amanda", font=('Arial', 20))
                textlabel_energy.pack(anchor="n", pady=150, side="top")

        elif "Car" == menu_list_BTN.cget("text"):
            # C4X
            if count["car"] == 0:
                textlabel_energy = tkinter.Button(menu_sub_frame, text="Toyota Altis", name="c1", font=('Arial', 20), command= lambda: self.carprice(100000, player, menu_sub_frame,"Toyota Altis"))
                textlabel_energy.pack(anchor="n", pady=50, side="top")

                textlabel_energy = tkinter.Button(menu_sub_frame, text="Mercedes Benz A200", name="c2", font=('Arial', 20), command= lambda: self.carprice(250000, player, menu_sub_frame, "Mercedes Benz A200"))
                textlabel_energy.pack(anchor="n", pady=50, side="top")

                textlabel_energy = tkinter.Button(menu_sub_frame, text="Aston Martin Vantage", name="c3", font=('Arial', 20), command= lambda: self.carprice(500000, player, menu_sub_frame, "Aston Martin Vantage"))
                textlabel_energy.pack(anchor="n", pady=50, side="top")

        # elif "Dating app" == menu_list_BTN.cget("text"):
        #
        # elif "Marriage" == menu_list_BTN.cget("text"):
        #
        # elif "Work" == menu_list_BTN.cget("text"):
        #
        # elif "4D/Toto" == menu_list_BTN.cget("text"):
        #
        # elif "car" == menu_list_BTN.cget("text"):
        #
        # elif "house" == menu_list_BTN.cget("text"):
        #
        # elif "sport" == menu_list_BTN.cget("text"):
        #
        # elif "Driving licence" == menu_list_BTN.cget("text"):
        #
        # elif "Stats" == menu_list_BTN.cget("text"):
        #
        # elif "Suicide" == menu_list_BTN.cget("text"):
        popup.protocol("WM_DELETE_WINDOW", self.refresh_statsbar(window_frame_bottom, player))

    def carprice(self, value, player, menu_sub_frame, car):
        menu_sub_frame.nametowidget("c1").destroy()
        menu_sub_frame.nametowidget("c2").destroy()
        menu_sub_frame.nametowidget("c3").destroy()

        label = tkinter.Label(menu_sub_frame, text="You have $ " + str(float(player.get_value("money"))))
        label.pack(anchor="n", pady=150, side="top")

        if int(player.get_value("money")) > value:
            count["car"] = 1
            label = tkinter.Label(menu_sub_frame, text="You have bought a " + car)
            label.pack(anchor="n", pady=150, side="top")
        else:
            label = tkinter.Label(menu_sub_frame, text="You have insufficient amount of money to purchase this vehicle")
            label.pack(anchor="n", pady=150, side="top")

    def incident_popup(self, player, window_frame_bottom, game):
        menu_sub_popup = tkinter.Toplevel(game)
        menu_sub_popup.title("Choices")
        menu_sub_popup.grab_set()
        menu_sub_popup.geometry("500x300")

        descLabel = tkinter.Label(menu_sub_popup, text="", font=("Arial", 20))
        descLabel.pack()

        yesbutton = tkinter.Button(menu_sub_popup, text="Yes", bg="green")
        yesbutton.pack(side="left", fill="x", expand=True, anchor="s")

        nobutton = tkinter.Button(menu_sub_popup, text="No", bg="red")
        nobutton.pack(side="right", fill="x", expand=True, anchor="s")


    def max(self):
        age = 8
        age_lower = 0
        age_higher = 0

        energy = 100
        health = 100
        money = 100
        IQ = 100
        karma = 100

        energy_limit = 100
        health_limit = 100
        IQ_limit = 100
        karma_limit = 100

        desired_width = 320
        pd.set_option('display.width', desired_width)
        pd.set_option('display.max_columns', 12)
        df = pd.read_excel("scene.xlsx", sheet_name="scene")

        for i in range(len(df)):
            # print(df.iloc[i])

            # print(type(df.iloc[i][0]))
            split_age = df.iloc[i][0].split("-")
            age_lower = int(split_age[0])
            age_higher = int(split_age[1])

            # print(str(age_lower),"-",str(age_higher))

            if age < age_higher and age > age_lower:
                # print(str(age_lower),"-",str(age_higher))
                if type(df.iloc[i][2]) == str:
                    # print(df.iloc[i][2])
                    if '-' in str(df.iloc[i][3]):
                        energy = energy + int(df.iloc[i][3])
                        # print(energy)
                    elif '-' not in str(df.iloc[i][3]):
                        if energy > energy_limit:
                            energy = 100
                        # print(energy)

                    if '-' in str(df.iloc[i][4]):
                        money = money + int(df.iloc[i][4])
                    elif '-' not in str(df.iloc[i][4]):
                        money = money + float(df.iloc[i][4])

                    if '-' in str(df.iloc[i][5]):
                        health = health + int(df.iloc[i][5])
                    elif '-' not in str(df.iloc[i][5]):
                        if health > health_limit:
                            health = 100

                    if '-' in str(df.iloc[i][6]):
                        IQ = IQ + int(df.iloc[i][6])
                    elif '-' not in str(df.iloc[i][6]):
                        if IQ > IQ_limit:
                            IQ = 100

                    if '-' in str(df.iloc[i][7]):
                        karma = karma + int(df.iloc[i][7])
                    elif '-' not in str(df.iloc[i][7]):
                        if karma > 100:
                            karma = 100

        print(energy)
        print(money)
        print(health)
        print(IQ)
        print(karma)
