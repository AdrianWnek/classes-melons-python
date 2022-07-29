class MelonOrder:
    def get_base_price(self):
        return 5.0



class WatermelonOrder(MelonOrder):
    species = "Watermelon"
    color = "green"
    imported = False
    shape = "natural"
    seasons = ["Fall", "Summer"]

    def get_price(self, qty):
        total = self.get_base_price() * qty
        if qty >= 5:
            total = total * 0.75
        return total


class OgenOrder(MelonOrder):
    species = "Ogen"
    color = "tan"
    imported = False
    shape = "natural"
    seasons = ["Spring", "Summer"]

    def get_price(self, qty):
        total = (self.get_base_price() + 1) * qty
        
        return total