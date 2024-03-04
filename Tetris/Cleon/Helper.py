

class Switch:
    def get_rate(self, index):
        default = "Invalid Option"
        return getattr(self, 'rate_' + str(index), lambda: default)()

    def rate_1(self):
        return 1.4

    def rate_2(self):
        return 1.5

    def rate_3(self):
        return 1.75

    def rate_4(self):
        return 2.0
