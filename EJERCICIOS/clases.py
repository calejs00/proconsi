#Clase para filtrar la cadena
class ItemSeparator:
    #constructor con el que separo la cadena para poder obtener nombre, precio y cantidad
    def __init__(self, rawInput = str):
        input = rawInput.split("$$##")
        if len(input) != 3:
            raise ValueError("El formato del input no es válido")
        self._name = input[0]
        self._price = input[1]
        self._quantity = input[2]

    #getters
    def get_name(self) -> str:
        return self._name

    def get_price(self) -> float:
        return self._price

    def get_quantity(self) -> int:
        return self._quantity

#Clase main para realizar la prueba
class Main:
    def __init__(self):
        stdIn = "Bread$$##12.5$$##10"
        item = ItemSeparator(stdIn)
        print("Item Name:", item.get_name())
        print("Item Price:", item.get_price())
        print("Quantity:", item.get_quantity())

if __name__ == "__main__":
    a = Main()
