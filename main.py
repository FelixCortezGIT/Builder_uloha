class Pasta:
    def __init__(self, type, sauce, topping, dressing, chilli):
        self.type = type
        self.sauce = sauce
        self.topping = topping
        self.dressing = dressing
        self.chilli = chilli

class PastaBuilder:
    def __init__(self):
        self.type = None
        self.sauce = None
        self.topping = None
        self.dressing = None
    def add_type(self, type):
        self.type = type
    def add_sauce(self, sauce):
        self.sauce = sauce
    def add_topping(self, topping):
        self.topping = topping
    def add_dressing(self, dressing):
        self.dressing = dressing
    def add_chilli(self, chilli):
        self.chilli = chilli
    def build(self):
        return Pasta(self.type, self.sauce, self.topping, self.dressing, self.chilli)


pasta1 = Pasta('spaghety', 'carbonara', 'parmesan', False, 'mild')
pasta2 = Pasta('tortellini', 'tomato', 'mozzarella', False, 'strong')
pasta3 = Pasta('fusilli', 'pesto', 'parmesan', False, 'mild')

pastaBuilder = PastaBuilder()
pastaBuilder.add_type("penne")
pastaBuilder.add_sauce("tartufo")
pastaBuilder.add_topping("mushrooms")
pastaBuilder.add_dressing("parmesan")
pastaBuilder.add_chilli("mild")

pasta4 = pastaBuilder.build()
print(pasta3)
