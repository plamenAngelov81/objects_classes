class Cars:
    def __init__(self):

        self.production = []
        self.paint_shop_1 = []
        self.paint_shop_2 = []

    def make_cars(self, model: str):
        self.production.append(model)

    def car_color(self, color: str):
        if color == "red" or color == "blue":
            self.paint_shop_1.append(color)
        elif color == "green" or color == "yellow":
            self.paint_shop_2.append(color)

    def __repr__(self):
        result = f"We made total: {len(self.production)} cars. \nRed and blue cars: {len(self.paint_shop_1)}." \
                 f" \nGreen and yellow cars: {len(self.paint_shop_2)}"
        return result


bmw = Cars()

bmw.make_cars("320i")
bmw.car_color("red")

bmw.make_cars("520i")
bmw.car_color("blue")

bmw.make_cars("430XD")
bmw.car_color("red")

bmw.make_cars("M5 Competition")
bmw.car_color("green")

bmw.make_cars("M4i50")
bmw.car_color("red")

print(bmw)
