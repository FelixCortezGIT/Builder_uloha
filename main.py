class Pasta:
    def __init__(self, type, sauce, topping, dressing, chilli):
        self.type = type
        self.sauce = sauce
        self.topping = topping
        self.dressing = dressing
        self.chilli = chilli
    def __repr__(self):
        return (f"Pasta(type={self.type!r}, sauce={self.sauce!r}, topping={self.topping!r}, dressing={self.dressing!r}, chilli={self.chilli!r})")

class PastaBuilder:
    def __init__(self):
        self.type = None
        self.sauce = None
        self.topping = None
        self.dressing = None
        self.chilli = None
    def add_type(self, type):
        self.type = type
        return self
    def add_sauce(self, sauce):
        self.sauce = sauce
        return self
    def add_topping(self, topping):
        self.topping = topping
        return self
    def add_dressing(self, dressing):
        self.dressing = dressing
        return self
    def add_chilli(self, chilli):
        self.chilli = chilli
        return self
    def build(self):
        return Pasta(self.type, self.sauce, self.topping, self.dressing, self.chilli)

pasta1 = Pasta('spaghety', 'carbonara', 'parmesan', 'none', 'mild')
pasta2 = Pasta('tortellini', 'tomato', 'mozzarella', 'none', 'strong')
pasta3 = Pasta('fusilli', 'pesto', 'parmesan', 'none', 'mild')

pasta4 = (PastaBuilder()
          .add_type("penne")
          .add_sauce("tartufo")
          .add_topping("mushrooms")
          .add_dressing("parmesan")
          .add_chilli("mild")
          .build())

print(pasta1)
print(pasta2)
print(pasta3)
print(pasta4)
