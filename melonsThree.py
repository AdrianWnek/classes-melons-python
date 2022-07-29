class AbstractMelonOrder:
    
    def __init__(self):
        raise NotImplementedError("Don't make instances of me")

    def get_base_price(self):
        return 5.0    