#CASOS QUE HE TENIDO EN CUENTA
#-Que el string esté en un formato incorrecto
#-Que el string tenga un precio o cantidad no numéricos

#Clase para filtrar la cadena
class ItemSeparator:
    #constructor con el que separo la cadena para poder obtener nombre, precio y cantidad
    def __init__(self, rawInput = str):
        rawInput = rawInput.strip()
        input = rawInput.split("$$##")
        if len(input) != 3:
            raise ValueError("El formato del input no es válido")
        self._name = input[0].strip()
        self._price = input[1].strip()
        self._quantity = input[2].strip()
        if not self._name:
            raise ValueError("El nombre no puede estar vacío")
        try:
            self._price = float(self._price)
            if self._price <= 0:
                raise ValueError("El precio debe ser mayor que 0")
        except ValueError:
            raise ValueError(f"Precio inválido: {self._price}")
        try:
            self._quantity = int(self._quantity)
            if self._quantity <= 0:
                raise ValueError("La cantidad debe ser mayor que 0")
        except ValueError:
            raise ValueError(f"Cantidad inválida: {self._quantity}")

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
        stdIn = "Bread$$##12.5$$##2"
        item = ItemSeparator(stdIn)
        print("Item Name:", item.get_name())
        print("Item Price:", item.get_price())
        print("Quantity:", item.get_quantity())

if __name__ == "__main__":
    a = Main()
