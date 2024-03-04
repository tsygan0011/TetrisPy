

# Imports
#import Values as val
import Helper as helper

# Class
class Player:
    # Length of 9 as of now
    #!!car?house? and Relationship?
    #energy random?, age 0?, health random, iq random, karma random?
    variables = ['name', 'age', 'energy', 'money', 'health', 'iq', 'karma', 'time_limit', 'difficulty']
    variables_limit = [None, 99, 100, None, 0, None, 1, 180, None]
    variables_rate = [1, 1]
    variables_rate_options = [1, 1.2, 1.5, 1.85, 2]

    # sets range of age to change rate
    # age_range = [21, 30, 40, 50, 99]
    global personalisation
    global values
    # Singleton
    __instance = None

    def __init__(self, personalisation):
        if self.__instance is None:
            # personalisation contains all the variables' values
            self.personalisation = personalisation
            self.__instance = Player

    # get variable value according to name passed in
    # to access player's data, do .get_value('energy')
    def get_value(self, var_name):
        for var in self.variables:
            if var == var_name:
                return str(self.personalisation[self.variables.index(var)])

    # set variable value according to name passed in
    def set_value(self, var_name, amt):
        if not var_name == "name":
            for var in self.variables:
                if var == var_name:
                    # get current amt for var_name passed in. E.g. energy
                    cur_amt_for_var = self.personalisation[self.variables.index(var)]

                    # get new amt for var_name passed in
                    new_amt_for_var = cur_amt_for_var + amt

                    # checks if new amt will overshoot capped limit / not enough
                    if new_amt_for_var > 0 and new_amt_for_var < self.get_value_limit(var_name):
                        self.personalisation[self.variables.index(var)] = new_amt_for_var
                    else:
                        if new_amt_for_var <= 0:
                            self.personalisation[self.variables.index(var)] = 0
                        elif new_amt_for_var > self.get_value_limit(var_name):
                            self.personalisation[self.variables.index(var)] = self.get_value_limit(var_name)

                    # # checks if new amt will overshoot capped limit / not enough
                    # if not (new_amt_for_var < 0 or new_amt_for_var > self.get_value_limit(var_name)):
                    #     self.personalisation[self.variables.index(var)] = new_amt_for_var
                    # else:
                    #
                    #     self.personalisation[self.variables.index(var)] = self.get_value_limit(var_name)

        else:
            print("You can not adjust your name!")

    # get variable limit according to name passed in
    def get_value_limit(self, var_name):
        for var in self.variables:
            if var == var_name:
                return self.variables_limit[self.variables.index(var)]

    # set variable limit according to name passed in
    def set_value_limit(self, var_name, amt):
        for var in self.variables:
            if var == var_name:
                # get current limit for var_name passed in. E.g. energy
                cur_limit_for_var = self.variables_limit[self.variables.index(var)]

                # get new limit for var_name passed in
                new_limit_for_var = cur_limit_for_var + amt
                if new_limit_for_var >= 0:
                    self.variables_limit[self.variables.index(var)] = new_limit_for_var

    def get_age_in_range(self, age):
        ages = self.personalisation[1]
        for range in self.age_range:
            if ages == age:
                return self.age_range[self.age_range.index(range)]


    # adjust rate accordingly by age
    def get_rate_of_consumption(self, var_name):
        # [1] is age
        age = self.personalisation[1]
        rate = 1

        # check age belongs to which range
        for range in self.age_range:
            if age >= self.age_range[0]:
                if range >= age > self.age_range[self.age_range.index(range) - 1]:
                    # set rate according to age in range
                    rate = helper.Switch.get_rate(helper.Switch(), self.age_range.index(range))
                    # print("rate: " + str(self.switch(age_range.index(range))))
                    # print("you are in " + str(age_range[age_range.index(range) - 1]) + "-" + str(
                    #     age_range[age_range.index(range)]))
            else:
                print("too young boy")
                break

        # can do it this way cause there's only 2 values that have different rate of consumption
        index = -1                  # initialise it with an index of -1
        if var_name == 'energy':    # if energy was passed in
            index = 0               # set index to 0
        elif var_name == 'health':
            index = 1

        # variables_rate have len of 2, 0 is energy, 1 is health
        self.variables_rate[index] = rate   # set respective rate

        return self.variables_rate[index]

    # incomplete
    def set_value_limit_by_age(self, var_name):
        age = self.personalisation[1]
        #print("age: " + str(age))
        for var in self.variables:
            if var == var_name:
                # get current limit for var_name passed in. E.g. energy
                cur_limit_for_var = self.variables_limit[self.variables.index(var)]

                # get new limit for var_name passed in
                rate = (self.personalisation[self.variables.index(var)] / ((self.get_age_in_range(age) / self.get_rate_of_consumption(var_name))))
                #print(rate)
                new_limit_for_var = round(cur_limit_for_var - rate)
                #print(new_limit_for_var)
                if new_limit_for_var >= 0:
                    self.variables_limit[self.variables.index(var)] = new_limit_for_var


                #print(self.variables_rate_options[self.variables.index(var)])
        print("--------")
        return

class Activities:
    activities = []
    def load_activities(self):
        #activities =
        pass

    def get_activity(self, activities):
        pass


