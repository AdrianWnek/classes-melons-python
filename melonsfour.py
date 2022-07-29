class AbstractMelonOrder:
    add_on = 0

    def __init__(self):
        raise NotImplementedError("Don't make instances of me")

    def get_base_price(self):
        return 5.0

    def get_price(self, qty):
        each = self.get_base_price() + self.add_on
        total = each * qty

        if self.imported:
            total = total * 1.5

        if self.shape == "square":
            total = total * 2

        return total

class WatermelonOrder(AbstractMelonOrder):
    species = "Watermelon"
    color = "green"
    imported = False
    shape = "natural"
    seasons = ["Fall", "Summer"]

    def get_price(self, qty):
        total = super(WatermelonOrder, self).get_price(qty)
        if qty >= 5:
            total = total * 0.75
        return total


class OgenOrder(AbstractMelonOrder):
    species = "Ogen"
    color = "tan"
    imported = False
    shape = "natural"
    seasons = ["Spring", "Summer"]

    add_on = 1                
