class Catalogue:
    def __init__(self, name: str):
        self.name = name
        self.product = []

    def add_product(self, product_name: str):
        self.product.append(product_name)

    def get_by_letter(self, first_letter: str):
        items = [i for i in self.product]
        first_letter_list = [y for y in items if y[0] == first_letter]
        return first_letter_list

    def __repr__(self):
        self.product.sort()
        final = f"Items in the {self.name} catalogue:\n" + "\n".join(self.product)
        return final


catalogue = Catalogue("Furniture")
catalogue.add_product("Sofa")
catalogue.add_product("Mirror")
catalogue.add_product("Desk")
catalogue.add_product("Chair")
catalogue.add_product("Carpet")
print(catalogue.get_by_letter("C"))
print(catalogue)
