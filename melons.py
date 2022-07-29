"""This file should have our melon-type classes in it."""


class WatermelonOrder:
    species = "Watermelon"
    color = "green"
    imported = False
    shape = "natural"
    seasons = ["Fall", "Summer"]

    def get_price(self, qty):
        tptal = 5.0 * qty
        if qty >= 5:
            total = total * 0.75
            return total

class OgenOrder:
    species = "Ogen"
    color = "tan"
    imported = False
    shape = "natural"
    seasons = ["Spring", "Summer"]

    def get_price(self, qty):
        total = 6.0 * qty
        return total            
