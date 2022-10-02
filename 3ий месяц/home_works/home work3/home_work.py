class Good():
    def __init__(self, name, unitPrice: int, amount: int):
        self.name = name
        self.unitPrice = unitPrice
        self.amount = amount
    
    def price(self):
        return self.unitPrice * self.amount

    def print_good(self):
        print(f"{self.name:<20}{self.unitPrice:>3} * {self.amount:>5} ={self.price():>8}")

class DiscountGood(Good):
    def __init__(self, name, price: int, amount: int, discount: int):
        super().__init__(name, price, amount)
        self.discount = discount

    def price_with_discount(self):
        discount = self.discount * 0.01
        totalPrice = int(super().price())
        return totalPrice - (discount * totalPrice)

    def print_with_discount(self):
        print(f"{self.name:<20}{self.unitPrice:>3} * {self.amount:>5} ={self.price_with_discount():>8}  (-{self.discount:>2})")


class Cart():
    def __init__(self, allGoods: list[Good, DiscountGood]) -> None:
        self.allGoods = allGoods
    
    def total_price(self):
        total = 0
        for good in self.allGoods:
            total += good.price()
        return total
    
    def print_check(self):
        print(f"{'Name':<20}{'PPU':>3}  {'CNT':>7}  {'PRICE':>8}  {'Disc.':>2}")
        print("="*50)
        for good in self.allGoods:
            if good.__class__ == Good:
                good.print_good()
            elif good.__class__ == DiscountGood:
                good.print_with_discount()
            else:
                pass
        print("="*50)
        print(f"{'Total':<38}{self.total_price()}")

apple = Good("apple", 16, 3)
milk = DiscountGood("milk", 100, 1, 10)
cart = Cart([apple, milk])

cart.print_check()