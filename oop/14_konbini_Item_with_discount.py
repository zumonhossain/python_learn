class Item:
    def __init__(self, name, price):
        self.name = name;
        self.price = price;

    def apply_discount(self, percent):
        discounted_price = self.price - (self.price * percent / 100);
        print(self.name, "after", str(percent) + "% discount:", discounted_price, "yen");

item1 = Item("Onigiri", 120);
item2 = Item("Green Tea", 150);

item1.apply_discount(20);
item2.apply_discount(10);