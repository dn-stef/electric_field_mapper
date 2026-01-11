class Charge:
    def __init__(self, x, y, q):
        self.x = x
        self.y = y
        self.q = q

class ChargeManager:
    def __init__(self):
        self.charge_list = []
        self.current_mode = 1

    def add_charge(self, charge):
        self.charge_list.append(charge)
    
    def get_all_charges(self):
        return self.charge_list
    
    def set_mode(self, mode):
        self.current_mode = mode