from datetime import date


class AbstractMelonOrder:

    def available_now(self):
        today = date.today()
        month = today.month

        if month == 1 and "Winter" in self.seasons:
            return True
        if month == 2 and "Winter" in self.seasons:
            return True
        if month == 3 and "Winter" in self.seasons:
            return True
        if month == 4 and "Spring" in self.seasons:
            return True
        if month == 5 and "Spring" in self.seasons:
            return True
        if month == 6 and "Spring" in self.seasons:
            return True
        if month == 7 and "Summer" in self.seasons:
            return True
        if month == 8 and "Summer" in self.seasons:
            return True
        if month == 9 and "Summer" in self.seasons:
            return True
        if month == 10 and "Fall" in self.seasons:
            return True
        if month == 11 and "Fall" in self.seasons:
            return True
        if month == 12 and "Fall" in self.seasons:
            return True

        return False                                        